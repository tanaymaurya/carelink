"""Visit note summaries for clinicians."""
from lib.llm_gateway import chat


class NoteSummarizer:
    def _prompt(self, note):
        return [{"role": "user", "content": f"Summarise for the clinician:\n{note}"}]

    def summarize(self, note):
        return chat(model="gpt-4o-mini", messages=self._prompt(note), feature="visit-notes")


def summarize_note(note):
    return NoteSummarizer().summarize(note)
