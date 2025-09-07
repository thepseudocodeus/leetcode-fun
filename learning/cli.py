#!/usr/bin/env python3
import logging
import uuid
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any

import cli

from psb.modules.cli.components import dashboard, pdf
from psb.modules.cli.core.config_manager import (
    enable_feature,
    list_config,
    reset_config,
    set_config_value,
)
from psb.modules.cli.tasks import manager

# -----------------------------------------------------------------------------
# Core Application Class (Encapsulates all state and logic)
# -----------------------------------------------------------------------------


class PSBCLIState:
    """Manages the state and data for the PSB CLI application."""

    def __init__(self):
        self.files: List[Path] = []
        self.id_files: List[Dict[str, Path]] = []
        self.config: Dict[str, Any] = {}

    def get_id_files(self) -> List[Dict[str, Path]]:
        """Adds unique IDs to files and returns the list."""
        if not self.id_files:
            self.id_files = [
                {"id": str(uuid.uuid4()), "file": file} for file in self.files
            ]
        return self.id_files


# -----------------------------------------------------------------------------
# Typer CLI Application Setup
# -----------------------------------------------------------------------------

# Create the Typer app instance and the application state object
app = cli.Typer(help="PSB Hyper-CLI: Guided antifragile problem solving")
state = PSBCLIState()

# -----------------------------------------------------------------------------
# CLI Commands (Functions that operate on the state)
# -----------------------------------------------------------------------------


@app.command()
def config():
    """Show current configuration."""
    list_config()


@app.command()
def enable(feature: str):
    """Enable a specific feature."""
    enable_feature(feature, True)


@app.command()
def disable(feature: str):
    """Disable a specific feature."""
    enable_feature(feature, False)


@app.command()
def set_config(path: str, value: str):
    """Set a specific configuration value."""
    # Convert value to appropriate type
    if value.lower() == "true":
        typed_value = True
    elif value.lower() == "false":
        typed_value = False
    elif value.isdigit():
        typed_value = int(value)
    elif value.replace(".", "", 1).isdigit() and value.count(".") == 1:
        typed_value = float(value)
    else:
        typed_value = value

    set_config_value(path, typed_value)


@app.command()
def reset():
    """Reset configuration to defaults."""
    reset_config()


@app.command()
def new_task(name: str):
    """Create a new guided PSB task from template."""
    manager.create_task(name)


@app.command()
def find_pdfs(path: str):
    """Find PDFs in a directory and cache them."""
    print("Finding PDFs started...")
    if not state.files:
        state.files = pdf.find_pdfs_cmd(path)

    id_files = state.get_id_files()
    print(f"Found {len(id_files)} PDF(s).")
    return id_files


@app.command()
def extract_page(pdf_path: str, page: int = 0):
    """Extract text from a specific PDF page."""
    pdf.extract_page_cmd(pdf_path, page)


@app.command()
def validate(pdf_path: str, page: int = 0, headers: str = cli.Option(None)):
    """Validate a table in a PDF."""
    pdf.validate_table_cmd(pdf_path, page, headers)


@app.command()
def evolve(
    path: str,
    pages: str = cli.Option(None),
    headers: str = cli.Option(None),
    threshold: float = cli.Option(0.9),
):
    """Run evolutionary improvement of PDF extraction."""
    pg = [int(p) for p in pages.split(",")] if pages else None
    hd = [h.strip() for h in headers.split(",")] if headers else None
    pdf.evolve_cmd(path, pg, hd, threshold)


@app.command()
def dashboard_it():
    """Show the PSB dashboard."""
    dashboard.show()


@app.command()
def select_file(file_name: str):
    """Select a file by name."""
    print(f"File selection for '{file_name}' not yet implemented.")


# -----------------------------------------------------------------------------
# Main Execution Block
# -----------------------------------------------------------------------------


def main():
    """The main entry point for the CLI."""
    # Place all setup and initialization logic here
    log_dir = Path("data/logs")
    log_dir.mkdir(exist_ok=True, parents=True)

    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_dir / "psb_cli.log"),
            logging.StreamHandler(),
        ],
    )

    logger = logging.getLogger(__name__)

    try:
        from psb.modules.cli.core.initialization import (
            get_config,
            initialize_psb_environment,
        )

        initialize_psb_environment()
        state.config = get_config()
        logger.info(
            f"PSB CLI started with config version {state.config.get('version', 'unknown')}"
        )
    except ImportError:
        logger.warning("Initialization module not yet implemented.")

    app()


if __name__ == "__main__":
    main()
