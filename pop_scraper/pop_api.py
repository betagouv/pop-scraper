from pop_scraper.settings import ITEMS_PER_REQUEST

def build_query(cursor):
  return {
    "query": {
      "bool": {
        "should": [
          {
            "regexp": {
              "REF.keyword": "[Pp][Mm].*"
            }
          }
        ]
      }
    },
    "size": ITEMS_PER_REQUEST,
    "from": cursor,
    "_source": {
      "excludes": [
        "ADRS2",
        "COM2",
        "EDIF2",
        "EMPL2",
        "INSEE2",
        "LBASE2"
      ]
    }
  }
