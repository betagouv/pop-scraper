BOT_NAME = 'pop_scraper'
SPIDER_MODULES = ['pop_scraper.spiders']
NEWSPIDER_MODULE = 'pop_scraper.spiders'
DOWNLOAD_DELAY = 1
CONCURRENT_REQUESTS_PER_DOMAIN = 1
AUTOTHROTTLE_ENABLED = True
ITEMS_PER_REQUEST = 1000

FEEDS = {
  'tmp/palissy.csv': {
    'format': 'csv', 'encoding': 'utf8', 'store_empty': False, 'overwrite': True,
    'item_classes': ['pop_scraper.items.ItemPalissy']
  },
  'tmp/palissy_to_merimee.csv': {
    'format': 'csv', 'encoding': 'utf8', 'store_empty': False, 'overwrite': True,
    'item_classes': ['pop_scraper.items.ItemPalissyToMerimee']
  },
  'tmp/palissy_to_memoire.csv': {
    'format': 'csv', 'encoding': 'utf8', 'store_empty': False, 'overwrite': True,
    'item_classes': ['pop_scraper.items.ItemPalissyToMemoire']
  },
  'tmp/merimee.csv': {
    'format': 'csv', 'encoding': 'utf8', 'store_empty': False, 'overwrite': True,
    'item_classes': ['pop_scraper.items.ItemMerimee']
  },
  'tmp/merimee_to_memoire.csv': {
    'format': 'csv', 'encoding': 'utf8', 'store_empty': False, 'overwrite': True,
    'item_classes': ['pop_scraper.items.ItemMerimeeToMemoire']
  }
}
