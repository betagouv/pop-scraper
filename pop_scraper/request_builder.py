import scrapy
import json


class RequestBuilder(object):
    def __init__(self, base_pop):
        self.base_pop = base_pop

    def build_request(self, ref_start, ref_end, start_from):
        return self.build_request_from_query(
            {
                "query": {
                    "bool": {
                        "must": [
                            {
                                "range": {
                                    "REF.keyword": {
                                        "gte": ref_start,
                                        "lte": ref_end
                                    }
                                }
                            }
                        ]
                    }
                },
                "size": self.items_per_request,
                "from": start_from
            },
            ref_start,
            ref_end,
            start_from
        )

    def build_request_from_query(self, query, ref_start, ref_end, start_from):
        return scrapy.Request(
            f"https://api.pop.culture.gouv.fr/search/{self.base_pop}/_msearch",
            method="POST",
            headers={"Content-Type": "application/x-ndjson"},  # add referer ?
            body='{"preference":"res"}\n' + json.dumps(query) + '\n',
            meta={"ref_start": ref_start, "ref_end": ref_end,
                  "current_items_count": start_from},
        )


class RequestBuilderPalissy(RequestBuilder):
    def __init__(self, items_per_request):
        RequestBuilder.__init__(self, "palissy")
        self.items_per_request = items_per_request

    def build_initial_requests(self):
        # useful SQL query to get the number of items per department in datasette :
        # select substr(REF,0,7) as ref_start, count(*) as notices_count from palissy WHERE substr(REF,0,5) == "PM50" GROUP BY ref_start;
        initial_requests = []
        for code_departement in [
            "01", "02", "03", "04", "05", "06", "07", "08", "09", "10",
            "11", "12", "13", "14", "15", "16", "17", "18", "19", "2A",
            "2B", "21", "22", "23", "24", "25", "26", "27", "28", "29",
            "30", "31", "32", "33", "34", "35", "36", "37", "38", "39",
            "40", "41", "42", "43", "44", "45", "46", "47", "48", "49",
            # "50", il y a malheureusement un peu plus de 10k objets dans la manche
            "51", "52", "53", "54", "55", "56", "57", "58", "59",
            "60", "61", "62", "63", "64", "65", "66", "67", "68", "69",
            "70", "71", "72", "73", "74", "75", "76", "77", "78", "79",
            "80", "81", "82", "83", "84", "85", "86", "87", "88", "89",
            "90", "91", "92", "93", "94", "95", "971", "972", "973", "974", "976"
        ]:
            initial_requests.append(
                self.build_request(
                    f"PM{code_departement.ljust(3, '0')}00001",
                    f"PM{code_departement.ljust(3, '0')}99999",
                    0
                )
            )
        initial_requests.append(
            self.build_request(
                "PM5000001",
                "PM5001000",
                0
            )
        )
        initial_requests.append(
            self.build_request(
                "PM5001000",
                "PM5009999",
                0
            )
        )
        return initial_requests


class RequestBuilderMerimee(RequestBuilder):
    def __init__(self, items_per_request):
        RequestBuilder.__init__(self, "merimee")
        self.items_per_request = items_per_request

    def build_initial_requests(self):
        for prefix in [
            # select substr(REF,1,2) as ref_start, count(*) as notices_count from merimee WHERE SUBSTR(REF,3,1) IN ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9") GROUP BY ref_start HAVING notices_count < 10000;
            "DN", "EA", "MI",
            # select substr(REF,1,3) as ref_start, count(*) as notices_count from merimee WHERE SUBSTR(REF,3,1) NOT IN ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9") GROUP BY ref_start
            "ACR", "JAR", "SPR",
            # select substr(REF,0,3) as ref_start, count(*) as notices_count from merimee GROUP BY ref_start HAVING notices_count >= 10000
            # => IA & PA
            # select substr(REF,0,5) as ref_start, count(*) as notices_count from merimee WHERE substr(REF,0,3) IN ('IA') GROUP BY ref_start HAVING notices_count < 10000;
            "IA01", "IA02", "IA03", "IA04", "IA05", "IA06", "IA07", "IA08", "IA09", "IA10", "IA11", "IA12", "IA13", "IA14", "IA15", "IA16", "IA17", "IA18", "IA19", "IA21", "IA23", "IA24", "IA25", "IA26", "IA27", "IA28", "IA29", "IA2A", "IA2B", "IA30", "IA31", "IA32", "IA33", "IA34", "IA36", "IA37", "IA38", "IA39", "IA40", "IA41", "IA42", "IA43", "IA44", "IA45", "IA46", "IA47", "IA48", "IA49", "IA50", "IA51", "IA52", "IA53", "IA54", "IA55", "IA56", "IA57", "IA58", "IA59", "IA60", "IA61", "IA62", "IA63", "IA64", "IA65", "IA66", "IA67", "IA68", "IA69", "IA70", "IA71", "IA72", "IA73", "IA74", "IA75", "IA76", "IA77", "IA78", "IA79", "IA80", "IA81", "IA82", "IA83", "IA84", "IA85", "IA86", "IA87", "IA88", "IA89", "IA90", "IA91", "IA92", "IA93", "IA94", "IA95", "IA97", "IA99",
            # select substr(REF,0,7) as ref_start, count(*) as notices_count from merimee WHERE substr(REF,0,5) IN ('IA00', 'IA22', 'IA35') GROUP BY ref_start;
            "IA0000", "IA0001", "IA0002", "IA0003", "IA0004", "IA0005", "IA0006", "IA0007", "IA0008", "IA0009", "IA0010", "IA0011", "IA0012", "IA0013", "IA0014", "IA2200", "IA2201", "IA2213", "IA3500", "IA3501", "IA3502", "IA3503", "IA3504", "IA3505", "IA3513",
            # select substr(REF,0,4) as ref_start, count(*) as notices_count from merimee WHERE substr(REF,0,3) IN ('PA') GROUP BY ref_start ;
            # all but PA0
            "PA1", "PA2", "PA3", "PA4", "PA5", "PA6", "PA7", "PA8", "PA9",
            # select substr(REF,0,7) as ref_start, count(*) as notices_count from merimee WHERE substr(REF,0,4) IN ('PA0') GROUP BY ref_start;,
            "PA0007", "PA0008", "PA0009", "PA0010", "PA0011", "PA0012", "PA0013", "PA0100", "PA0200", "PA0300", "PA0400", "PA0500", "PA0600", "PA0700", "PA0800", "PA0900"
        ]:
            yield self.build_request(
                prefix.ljust(10, "0"),
                prefix.ljust(10, "9"),
                0
            )
