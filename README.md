# SerperAPI

# Example Code Link
```python
from serper import SerperClient

serper_client = SerperClient(api_key="SERPERAPIKEY")

query = "Latest advancements in ai technology"

response = serper_client.search(
    query=query, 
    country="us", 
    location="New York, United States",
    language="en",
    date_range="qdr:y",
    page=1
)

print(response)
print(response.organic[0])
```