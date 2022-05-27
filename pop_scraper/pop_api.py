def build_query(base_pop, search_after=None, exact_ref=None, items_per_request=100):
  q = {
    "query": {
      "bool": {
        "should": build_shouldas(base_pop, exact_ref)
      }
    },
    "size": items_per_request,
    "sort": "_id"
  }
  if search_after is not None:
    q["search_after"] = [search_after]
  return q

def build_shouldas(base_pop, exact_ref):
  if exact_ref is not None:
    return [
      {
        "term": {
          "REF.keyword": exact_ref
        }
      }
    ]
  elif base_pop == "palissy":
    return [
        {
        "regexp": {
          "REF.keyword": "[Pp][Mm].*"
        }
      }
    ]
  return []
