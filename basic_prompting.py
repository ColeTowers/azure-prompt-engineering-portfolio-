from openai import AzureOpenAI

client = AzureOpenAI(
    api_key="YOUR_KEY",
    api_version="2024-02-01",
    azure_endpoint="https://YOUR-RESOURCE.openai.azure.com"
)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a concise assistant that answers with bullet points only."},
        {"role": "user", "content": "Explain vector embeddings."}
    ],
    temperature=0.3
)

print(response.choices[0].message["content"])
