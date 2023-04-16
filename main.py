from sec_api import QueryApi

queryApi = QueryApi(api_key="5f7f3eb826b71aa7a90430d11baaa3227310029752c33f27d4f4259581a84aca")

query = {
    "query": { "query_string": {
        "query": "ticker:TSLA AND filedAt:{2020-01-01 TO 2020-12-31} AND formType:\"10-Q\""
    } },
    "from": "0",
    "size": "10",
    "sort": [{ "filedAt": { "order": "desc" } }]
}

filings = queryApi.get_filings(query)

print(filings)