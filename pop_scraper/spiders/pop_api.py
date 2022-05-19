import scrapy
import json
import logging
from pop_scraper.items import ItemPalissy, ItemMemoire
from pop_scraper.pop_api import build_query

class PopApiSpider(scrapy.Spider):
  name = 'pop_api'
  allowed_domains = ['api.pop.culture.gouv.fr']
  start_urls = ['http://api.pop.culture.gouv.fr/']

  def __init__(self, base_pop="palissy", max_items=None, ref=None, *args, **kwargs):
    super(PopApiSpider, self).__init__(*args, **kwargs)
    self.max_items_from_args = max_items
    self.base_pop = base_pop
    if base_pop not in ["palissy", "memoire"]:
      raise "unsupported base_pop (should be palissy or memoire)"
    self.build_request_kwargs = { "exact_ref": ref }

  def start_requests(self):
    return [self.build_request(0)]

  def build_request(self, cursor=0):
    query = build_query(self.base_pop, cursor, **self.build_request_kwargs)
    return scrapy.Request(
      f"https://api.pop.culture.gouv.fr/search/{self.base_pop}/_msearch",
      method="POST",
      headers={"Content-Type": "application/x-ndjson", "Referer": f"cursor {cursor}"},
      body='{"preference":"res"}\n' + json.dumps(query) + '\n',
      meta={ "cursor": cursor }
    )

  def parse(self, response):
    res = response.json()
    if "responses" not in res:
      logging.error(f"error while parsing {res}")
      raise Exception("error!")
    total_hits = res["responses"][0]["hits"]["total"]
    if response.meta["cursor"] == 0:
      logging.info(f"STARTING CRAWL, total hits: {total_hits}")
    hits = res["responses"][0]["hits"]["hits"]
    next_cursor = response.meta["cursor"] + self.settings.getint("ITEMS_PER_REQUEST")
    if len(hits) == self.settings.get("ITEMS_PER_REQUEST") and next_cursor < self.get_max_items():
      yield self.build_request(next_cursor)
    for hit in hits:
      if self.base_pop == "palissy":
        item = ItemPalissy()
        for field in item.fields:
          if field in ["MEMOIRE_REFS"]:
            continue
          item[field] = self.serialize_value(hit["_source"].get(field))
        memoire_fields = hit["_source"].get("MEMOIRE", [])
        item["MEMOIRE_REFS"] = self.serialize_value([f["ref"] for f in memoire_fields])
        item["MEMOIRE_URLS"] = self.serialize_value([f["url"] for f in memoire_fields])
        yield item

        # photo = Photo(ref_palissy=objet["REF"], position=idx)
        # for field in photo.fields:
        #   if field in ["ref_palissy", "position"]:
        #     continue
        #   photo[field] = memoire_fields.get(field)
        # yield photo

  def serialize_value(self, value):
    if isinstance(value, list) and all(isinstance(e, str) for e in value):
      return ";".join(value)
    return value

  def get_max_items(self):
    if self.max_items_from_args:
      return int(self.max_items_from_args)

    return self.settings.getint("MAX_ITEMS", 1000000)

