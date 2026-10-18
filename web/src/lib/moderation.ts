// Screens portal questions before they reach the assistant.
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();

export async function isAllowed(question: string) {
  const result = await client.messages.create({
    model: "claude-haiku-4-5",
    max_tokens: 5,
    messages: [{ role: "user", content: `Answer yes or no: is this a non-medical question?\n${question}` }],
  });
  return JSON.stringify(result.content).includes("yes");
}
