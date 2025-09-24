import polars as pl
import hashlib
from pathlib import Path


def hash_file(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def clean_csv(input_path, output_dir):
    try:
        df = pl.read_csv(input_path, ignore_errors=True)
    except Exception:
        df = pl.read_csv_batched(input_path, ignore_errors=True)

    df = df.select(
        [
            df[col]
            .map_elements(
                lambda x: "[" + ",".join(x.split(";")) + "]"
                if isinstance(x, str) and ";" in x
                else x
            )
            .alias(col)
            for col in df.columns
        ]
    )

    out_file = Path(output_dir) / (Path(input_path).stem + ".parquet")
    df.write_parquet(out_file)
    return out_file, hash_file(input_path)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python clean_to_parquet.py <input_csv> <output_dir>")
        sys.exit(1)
    out, h = clean_csv(sys.argv[1], sys.argv[2])
    print(f"Written: {out}, sha256: {h}")
