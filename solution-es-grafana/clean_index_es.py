from elasticsearch import Elasticsearch
import constants

import os
from dotenv import load_dotenv

load_dotenv()

# Create an Elasticsearch client
es = Elasticsearch("http://localhost:9200",
                   api_key=(os.getenv("USERNAME"), os.getenv("PASSWORD")))
es.options(ignore_status=[400, 404]).indices.delete(index=constants.INDEX_NAME)
