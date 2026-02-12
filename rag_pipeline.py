from openai import AzureOpenAI
import requests

SEARCH_URL = "https://YOUR-SEARCH.search.windows.net/indexes/docs/docs/search?api-version=2023-07-01-Preview"
SEARCH_KEY = "YOUR_SEARCH_KEY"

def retrieve(query):
    headers = {"Content-Type": "application/json", "api-key": SEARCH_KEY}
    payload = {"search": query, "top": 2}
    return requests.post(SEARCH_URL, headers=headers, json=payload).json()

client = AzureOpenAI(
    api_key="YOUR_KEY",
    api_version="2024-02-01",
    azure_endpoint="https://YOUR-RESOURCE.openai.azure.com"
)

query = "What is the warranty policy?"
docs = retrieve(query)
context = "\n".join([d["content"] for d in docs["value"]])

prompt = f"""
Answer using ONLY the context below.

Context:
{context}

Question: {query}
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}]
)

print(response.choices[0].message["content"])
