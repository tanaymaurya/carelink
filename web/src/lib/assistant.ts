// Answers portal questions directly with the Vercel AI SDK (not through the gateway).
import { generateText } from "ai";

export async function askAssistant(question: string) {
  const { text } = await generateText({
    model: "gpt-4o-mini",
    system: "You help patients with appointments and billing. Never give medical advice.",
    prompt: question,
  });
  return text;
}
