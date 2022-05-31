install:
	poetry install

dev:
	poetry run scrapy crawl pop_api

notebook:
	poetry run jupyter-lab

split_csv_by_dpt:
	poetry run python -m exports.split_csv_by_dpt $(csv_path)

prepare_sqlite:
	poetry run csvs-to-sqlite $(csv_path) exports/datasette.sqlite --index DPT

datasette:
	poetry run datasette exports/datasette.sqlite

publish_datasette:
	poetry run datasette publish cloudrun exports/datasette.sqlite --memory 1024Mi --service datasette
