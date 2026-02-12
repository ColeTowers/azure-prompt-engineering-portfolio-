import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AZURE_OPENAI_KEY,
  baseURL: "https://YOUR-RESOURCE.openai.azure.com/openai/deployments/YOUR-MODEL"
});

async function extract(text: string) {
  const response = await client.chat.completions.create({
    model: "gpt-4o-mini",
    messages: [{ role: "user", content: text }],
    functions: [
      {
        name: "product_info",
        parameters: {
          type: "object",
          properties: {
            product: { type: "string" },
            price: { type: "number" }
          },
          required: ["product", "price"]
        }
      }
    ],
    function_call: { name: "product_info" }
  });

  console.log(response.choices[0].message.function_call.arguments);
}

extract("The new Contoso SmartLamp costs 129 euros.");
