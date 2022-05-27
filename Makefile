install:
	poetry install

dev:
	poetry run scrapy crawl pop_api

notebook:
	poetry run jupyter-lab
