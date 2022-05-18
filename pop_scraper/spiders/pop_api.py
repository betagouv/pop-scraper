import scrapy
import json
from pop_scraper.items import Objet
from pop_scraper.pop_api import build_query

class PopApiSpider(scrapy.Spider):
  name = 'pop_api'
  allowed_domains = ['api.pop.culture.gouv.fr']
  start_urls = ['http://api.pop.culture.gouv.fr/']


  def start_requests(self):
    query = build_query()
    return [
      scrapy.Request(
        "https://api.pop.culture.gouv.fr/search/palissy/_msearch",
        method="POST",
        headers={
          "Content-Type": "application/x-ndjson",
        },
        body='{"preference":"res"}\n' + json.dumps(query) + '\n'
      )
    ]


  def parse(self, response):
    res = response.json()
    total_hits = res["responses"][0]["hits"]["total"]
    hits = res["responses"][0]["hits"]["hits"]
    for hit in hits:
      objet = Objet()
      for field in objet.fields:
        objet[field] = hit["_source"].get(field)
      yield objet
    pass
