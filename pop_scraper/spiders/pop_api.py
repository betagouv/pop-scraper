import scrapy
import json
import logging
from pop_scraper.items import Objet
from pop_scraper.pop_api import build_query

class PopApiSpider(scrapy.Spider):
  name = 'pop_api'
  allowed_domains = ['api.pop.culture.gouv.fr']
  start_urls = ['http://api.pop.culture.gouv.fr/']

  def start_requests(self):
    return [self.build_request(0)]

  def build_request(self, cursor=0, **kwargs):
    query = build_query(cursor, **kwargs)
    return scrapy.Request(
      "https://api.pop.culture.gouv.fr/search/palissy/_msearch",
      method="POST",
      headers={"Content-Type": "application/x-ndjson"},
      body='{"preference":"res"}\n' + json.dumps(query) + '\n',
      meta={ "cursor": cursor }
    )

  def parse(self, response):
    res = response.json()
    total_hits = res["responses"][0]["hits"]["total"]
    if response.meta["cursor"] == 0:
      logging.info(f"STARTING CRAWL, total hits: {total_hits}")
    hits = res["responses"][0]["hits"]["hits"]
    if len(hits) == self.settings.get("ITEMS_PER_REQUEST") and response.meta["cursor"] < self.settings.getint("MAX_ITEMS", 1000000):
      yield self.build_request(response.meta["cursor"] + self.settings.get("ITEMS_PER_REQUEST"))
    for hit in hits:
      objet = Objet()
      for field in objet.fields:
        objet[field] = hit["_source"].get(field)
      yield objet

