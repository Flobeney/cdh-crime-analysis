from elasticsearch import AsyncElasticsearch
import requests
import asyncio
import aiohttp
import json
import constants
from datetime import date
import pandas as pd

from dotenv import load_dotenv
import os

load_dotenv()


async def get_data(data_force_id: str, es: AsyncElasticsearch, date: date):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://data.police.uk/api/crimes-no-location?force={data_force_id}&date={date}") as response:
            data = await response.read()  # Read the response
            data = json.loads(data)  # Convert the response to a JSON object

            for crime in data:
                # Insert the force id in the each element of the list
                crime['force'] = data_force_id
                # Insert the data in Elasticsearch
                await es.index(index=constants.INDEX_NAME, body=crime)
            return data


async def main():
    # Create an Elasticsearch client
    es = AsyncElasticsearch("http://localhost:9200",
                            api_key=(os.getenv("USERNAME"), os.getenv("PASSWORD")))

    # Getting the data from forces from Police UK API
    data_forces = requests.get("https://data.police.uk/api/forces").json()
    # Getting the data from crimes without location from Police UK API
    print("Got the forces !")

    # Create a list of tasks
    tasks = []
    print("Creating tasks...")
    task_count = 1
    date_range = pd.date_range(
        start=constants.START_DATE, end=constants.END_DATE, freq="MS")
    for date in date_range:
        date_month = date.strftime("%Y-%m")
        for force in data_forces:
            # Add a task to the list of tasks using asyncio
            tasks.append(asyncio.create_task(
                get_data(force['id'], es, date_month)))
            print(f"Tasks created {task_count} !")
            task_count += 1
            await asyncio.sleep(1)

    # Wait for all tasks to complete
    await asyncio.gather(*tasks)

    await es.close()


if __name__ == "__main__":
    asyncio.run(main())
