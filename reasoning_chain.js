import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AZURE_OPENAI_KEY,
  baseURL: "https://YOUR-RESOURCE.openai.azure.com/openai/deployments/YOUR-MODEL"
});

async function classify(text) {
  const system = `
  You perform multi-step reasoning internally.
  Only output the final classification label.
  Labels: Positive, Neutral, Negative.
  `;

  const response = await client.chat.completions.create({
    model: "gpt-4o-mini",
    messages: [
      { role: "system", content: system },
      { role: "user", content: text }
    ]
  });

  console.log(response.choices[0].message.content);
}

classify("The product was okay, nothing special.");
