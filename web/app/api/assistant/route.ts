// Portal assistant endpoint: moderates the question, then answers it.
import { askAssistant } from "@/lib/assistant";
import { isAllowed } from "@/lib/moderation";

export async function POST(req: Request) {
  const { question } = await req.json();
  if (!(await isAllowed(question))) {
    return new Response("Please contact the clinic directly.", { status: 400 });
  }
  const answer = await askAssistant(question);
  return new Response(JSON.stringify({ answer }));
}
