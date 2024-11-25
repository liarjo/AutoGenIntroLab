# BostonCodeCamp37Demos

This folder contains demonstration code for the Boston Code Camp 37. The demos showcase various applications of AI agents using the Azure OpenAI service. Below is a brief description of each demo:

## Demo1_SingleAgent.ipynb
This notebook demonstrates the use of a single AI agent to perform tasks. The agent is configured to provide weather information for a given city using a randomly generated temperature and predefined weather conditions.

## Demo2_LiteratureReview.ipynb
This notebook demonstrates a multi-agent system designed to perform a literature review. The agents include:
- **Google Search Agent**: Searches Google for information and returns results with snippets and body content.
- **Arxiv Search Agent**: Searches Arxiv for academic papers related to a given topic and includes abstracts.
- **Report Agent**: Synthesizes data extracted by other agents into a high-quality literature review with correct references.

## Demo3_TravelAgent.ipynb
This notebook demonstrates a travel assistant agent that helps users with travel-related queries. The agent can handle tasks such as booking flights and providing travel information. The system includes a human-in-the-loop component to ensure accurate and helpful responses.

## AzModelClient.py
This script contains the `create_azure_openai_client` function, which creates an instance of `AzureOpenAIChatCompletionClient` using the specified configuration. The function reads the API key and Azure endpoint from environment variables.
