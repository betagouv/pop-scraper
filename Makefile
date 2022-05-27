install:
	poetry install

dev:
	poetry run scrapy crawl pop_api

notebook:
	poetry run jupyter-lab

split_csv_by_dpt:
	poetry run python -m exports.split_csv_by_dpt $(csv_path)
