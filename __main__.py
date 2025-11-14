"""
    SerperAPI Testing Module
"""

from serper import SerperClient
import os
from dotenv import load_dotenv

load_dotenv()

serper_client = SerperClient(api_key=os.getenv("SERPER_API_KEY"))

if __name__ == "__main__":
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