all: clean_to_parquet run_python run_haskell

clean_to_parquet:
	python pipelines/clean_to_parquet.py data/sample.csv data_clean/

run_python:
	jupyter nbconvert --to notebook --execute notebooks/discovery.ipynb --output notebooks/discovery.out.ipynb

run_haskell:
	ihaskell notebook --notebook-dir=notebooks
