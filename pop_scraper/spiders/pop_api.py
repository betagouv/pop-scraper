import scrapy
import json
import logging
from pop_scraper.items import ItemPalissy, ItemMemoire
from pop_scraper.pop_api import build_query

class PopApiSpider(scrapy.Spider):
  name = 'pop_api'
  allowed_domains = ['api.pop.culture.gouv.fr']
  start_urls = ['http://api.pop.culture.gouv.fr/']

  def __init__(self, base_pop="palissy", max_items=None, items_per_request=None, ref=None, *args, **kwargs):
    super(PopApiSpider, self).__init__(*args, **kwargs)
    self.max_items_from_args = max_items
    self.items_per_request_from_args = items_per_request
    self.base_pop = base_pop
    self.exact_ref = ref
    if base_pop not in ["palissy", "memoire"]:
      raise "unsupported base_pop (should be palissy or memoire)"

  def start_requests(self):
    return [self.build_request(current_items_count=0)]

  def build_request(self, search_after=None, current_items_count=0):
    query = build_query(
      self.base_pop,
      search_after=search_after,
      items_per_request=self.get_items_per_request(),
      exact_ref=self.exact_ref
    )
    return scrapy.Request(
      f"https://api.pop.culture.gouv.fr/search/{self.base_pop}/_msearch",
      method="POST",
      headers={"Content-Type": "application/x-ndjson", "Referer": f"search_after {search_after}"},
      body='{"preference":"res"}\n' + json.dumps(query) + '\n',
      meta={ "search_after": search_after, "current_items_count": current_items_count }
    )

  def parse(self, response):
    res = response.json()
    # logging.debug(f"got response {res}")
    if "responses" not in res or len(res["responses"]) < 1 or "hits" not in res["responses"][0]:
      logging.error(f"error while parsing {res}")
      raise Exception("error!")
    total_hits = res["responses"][0]["hits"]["total"]
    if response.meta["search_after"] is None:
      logging.info(f"STARTING CRAWL, total hits: {total_hits}")
    hits = res["responses"][0]["hits"]["hits"]
    next_current_items_count = response.meta["current_items_count"] + self.get_items_per_request()
    if len(hits) >= self.get_items_per_request() and next_current_items_count < self.get_max_items():
      yield self.build_request(search_after=hits[-1]["sort"][0], current_items_count=next_current_items_count)
    for hit in hits:
      if self.base_pop == "palissy":
        item = ItemPalissy()
        for field in item.fields:
          if field in ["MEMOIRE_REFS", "MEMOIRE_URLS"]:
            continue
          item[field] = hit["_source"].get(field)
        memoire_fields = hit["_source"].get("MEMOIRE", [])
        item["MEMOIRE_REFS"] = [f["ref"] for f in memoire_fields]
        item["MEMOIRE_URLS"] = [f["url"] for f in memoire_fields]
        yield item
      elif self.base_pop == "memoire":
        item = ItemMemoire()
        for field in item.fields:
          item[field] = hit["_source"].get(field)
        yield item

  def get_max_items(self):
    if self.max_items_from_args:
      return int(self.max_items_from_args)

    return self.settings.getint("MAX_ITEMS", 1000000)

  def get_items_per_request(self):
    if self.items_per_request_from_args:
      return int(self.items_per_request_from_args)

    return self.settings.getint("ITEMS_PER_REQUEST", 1000)

