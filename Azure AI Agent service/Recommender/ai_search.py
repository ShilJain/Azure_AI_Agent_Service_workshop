import json
import os

from azure.identity import DefaultAzureCredential, AzureCliCredential
from azure.search.documents import SearchClient
from dotenv import load_dotenv
from azure.search.documents.models import VectorizedQuery, VectorizableTextQuery
from azure.core.credentials import AzureKeyCredential

load_dotenv()

# Function to create the AI search client
def get_search_client(endpoint, index_name):
    credential = AzureKeyCredential(os.environ("AZURE_SEARCH_KEY"))
    #token = credential.get_token("https://cognitiveservices.azure.com/.default")

    # print("TOKEN", token.token)

    client = SearchClient(
        endpoint=endpoint, index_name=index_name, credential=credential
    )
    return client

# Function to search the AI search index
def search(query: str, k: int = 2):
    client = get_search_client(
        endpoint=os.environ("AZURE_SEARCH_SERVICE_ENDPOINT"), index_name=os.environ("AZURE_SEARCH_INDEX")
    )

    # Hybrid search

    vector_query = VectorizableTextQuery(
        text=query, k_nearest_neighbors=k, fields="text_vector"
    )
    response = client.search(
        search_text=query,
        vector_queries=[vector_query],
        top=k,
        vector_filter_mode="preFilter",
        query_type="semantic",
        semantic_configuration_name=os.environ("AZURE_SEARCH_SEMANTIC_SEARCH_CONFIG"),
        select="title,chunk",
        # query_caption="extractive",
    )
    response = list(response)

    output = []
    final_response=""
    for result in response:
        # result.pop("contentVector")
        output.append(result)
    print(f"Output length = {len(output)}")
    for i in output:
        final_response+=i["chunk"]
    print(final_response)
    return final_response




