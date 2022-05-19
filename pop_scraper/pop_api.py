from pop_scraper.settings import ITEMS_PER_REQUEST

def build_query(cursor, exact_ref=None):
  return {
    "query": {
      "bool": {
        "should": build_shouldas(exact_ref)
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

def build_shouldas(exact_ref):
  if exact_ref is None:
    return [
        {
        "regexp": {
          "REF.keyword": "[Pp][Mm].*"
        }
      }
    ]
  else:
    return [
      {
        "term": {
          "REF.keyword": exact_ref
        }
      }
    ]
