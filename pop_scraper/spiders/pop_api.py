import scrapy
import json
import logging
from pop_scraper.items import ItemPalissy, ItemPalissyToMerimee, ItemPalissyToMemoire, ItemMemoire, ItemMerimee, ItemMerimeeToMemoire
from pop_scraper.pop_api import build_query

class PopApiSpider(scrapy.Spider):
  name = 'pop_api'
  allowed_domains = ['api.pop.culture.gouv.fr']
  start_urls = ['http://api.pop.culture.gouv.fr/']

  def __init__(
    self,
    base_pop="palissy",
    max_items=None,
    items_per_request=None,
    ref=None,
    search_after=None,
    *args,
    **kwargs
  ):
    super(PopApiSpider, self).__init__(*args, **kwargs)
    self.max_items_from_args = max_items
    self.items_per_request_from_args = items_per_request
    self.base_pop = base_pop
    self.exact_ref = ref
    self.initial_search_after = search_after
    if base_pop not in ["palissy", "memoire", "merimee"]:
      raise "unsupported base_pop (should be palissy, memoire or merimee)"

  def start_requests(self):
    return [
      self.build_request(
        current_items_count=0,
        search_after=self.initial_search_after
      )
    ]

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

    if "responses" not in res or len(res["responses"]) < 1:
      logging.error(f"error while parsing {res}")
      raise Exception("error!")

    elif "error" in res["responses"][0] and res["responses"][0].get("status") == 429:
      logging.error(f"error 429 too many requests : {res}")
      raise Exception("error!")

    elif "hits" not in res["responses"][0]:
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
          item[field] = hit["_source"].get(field)
        yield item
        self.crawler.stats.inc_value("main_item_scraped_count", 1)
        for memoire in hit["_source"].get("MEMOIRE", []):
          if memoire and "ref" in memoire:
            yield ItemPalissyToMemoire(
              REF_PALISSY=item["REF"],
              REF_MEMOIRE=memoire.get("ref"),
              NAME=memoire.get("name"),
              COPY=memoire.get("copy"),
              URL=memoire.get("url")
            )
          else:
            logging.warning(f"ref not in {memoire}")
        for ref_merimee in hit["_source"].get("REFA", []):
          yield ItemPalissyToMerimee(REF_PALISSY=item["REF"], REF_MERIMEE=ref_merimee)
      elif self.base_pop == "memoire":
        item = ItemMemoire()
        for field in item.fields:
          item[field] = hit["_source"].get(field)
        yield item
        self.crawler.stats.inc_value("main_item_scraped_count", 1)
      elif self.base_pop == "merimee":
        item = ItemMerimee()
        for field in item.fields:
          if field in ["MEMOIRE_REFS", "MEMOIRE_URLS"]:
            continue
          item[field] = hit["_source"].get(field)
        for memoire in hit["_source"].get("MEMOIRE", []):
          if memoire and "ref" in memoire:
            yield ItemMerimeeToMemoire(
              REF_MERIMEE=item["REF"],
              REF_MEMOIRE=memoire.get("ref"),
              NAME=memoire.get("name"),
              COPY=memoire.get("copy"),
              URL=memoire.get("url")
            )
          else:
            logging.warning(f"ref not in {memoire}")
        yield item
        self.crawler.stats.inc_value("main_item_scraped_count", 1)

    logging.info(f"page scrapped, now at {self.crawler.stats.get_stats().get('main_item_scraped_count')} {self.base_pop} items scraped")


  def get_max_items(self):
    if self.max_items_from_args:
      return int(self.max_items_from_args)

    return self.settings.getint("MAX_ITEMS", 1000000)

  def get_items_per_request(self):
    if self.items_per_request_from_args:
      return int(self.items_per_request_from_args)

    return self.settings.getint("ITEMS_PER_REQUEST", 1000)
