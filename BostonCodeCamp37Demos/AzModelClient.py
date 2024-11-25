# AzModelClient.py
from autogen_ext.models import AzureOpenAIChatCompletionClient
import os

"""
Creates an instance of AzureOpenAIChatCompletionClient with the specified configuration.

The function reads the API key and Azure endpoint from environment variables.
Ensure that the environment variables 'API_KEY' and 'AZURE_ENDPOINT' are set before calling this function.

Returns:
    AzureOpenAIChatCompletionClient: An instance of AzureOpenAIChatCompletionClient configured with the specified model, API version, endpoint, and capabilities.
"""
def create_azure_openai_client() -> AzureOpenAIChatCompletionClient:
    return AzureOpenAIChatCompletionClient(
        model="gpt-4o-2024-08-06",
        api_version="2024-02-15-preview",
        azure_endpoint= os.getenv('AZURE_ENDPOINT'),
        api_key=os.getenv('API_KEY'),
        model_capabilities={
            "vision": True,
            "function_calling": True,
            "json_output": True,
        },
    )
