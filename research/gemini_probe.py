"""Research spike: compare Gemini on public FAQ questions."""
import google.generativeai as genai

model = genai.GenerativeModel(model_name="gemini-1.5-pro")


def ask(question):
    return model.generate_content(question)
