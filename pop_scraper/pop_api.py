from pop_scraper.settings import ITEMS_PER_REQUEST

def build_query(cursor):
  return {
    "query": {
      "bool": {
        "must": [
          {
            "bool": {
              "must": [
                {
                  "bool": {
                    "must": [
                      {
                        "bool": {
                          "should": [
                            {
                              "regexp": {
                                "REF.keyword": "[Pp][Mm].*"
                              }
                            }
                          ]
                        }
                      }
                    ],
                    "must_not": [],
                    "should": [],
                    "should_not": []
                  }
                }
              ]
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
