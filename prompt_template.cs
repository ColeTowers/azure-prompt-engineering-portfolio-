using Azure.AI.OpenAI;
using Azure;

var client = new OpenAIClient(
    new Uri("https://YOUR-RESOURCE.openai.azure.com/"),
    new AzureKeyCredential("YOUR_KEY")
);

string tone = "friendly";
string topic = "cloud security best practices";

string prompt = $@"
Write a {tone} explanation about: {topic}.
Keep it under 120 words.
";

var response = client.GetChatCompletions(
    "gpt-4o-mini",
    new ChatCompletionsOptions
    {
        Messages = { new ChatMessage(ChatRole.User, prompt) }
    }
);

Console.WriteLine(response.Value.Choices[0].Message.Content);
