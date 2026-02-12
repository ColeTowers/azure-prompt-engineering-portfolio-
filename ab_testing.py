from openai import AzureOpenAI

client = AzureOpenAI(
    api_key="YOUR_KEY",
    api_version="2024-02-01",
    azure_endpoint="https://YOUR-RESOURCE.openai.azure.com"
)

prompts = {
    "A": "Summarize the text in one sentence.",
    "B": "Provide a concise single-sentence summary."
}

text = "Azure OpenAI enables secure, enterprise-grade access to advanced language models."

for label, p in prompts.items():
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"{p}\n\n{text}"}]
    )
    print(f"{label}: {response.choices[0].message['content']}")
