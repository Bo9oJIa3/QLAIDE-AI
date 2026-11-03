import os
import anthropic


class ClaudeClient:
    def __init__(self):
        api_key = os.environ.get("ANTHROPIC_API_KEY")

        if not api_key:
            raise RuntimeError("ANTHROPIC_API_KEY не найден")

        self.client = anthropic.Anthropic(
            api_key=api_key
        )

        self.model = os.environ.get(
            "CLAUDE_MODEL",
            "claude-sonnet-4-5"
        )

    def ask(self, instructions, message):
        response = self.client.messages.create(
            model=self.model,
            max_tokens=2048,
            system=instructions,
            messages=[
                {
                    "role": "user",
                    "content": message
                }
            ]
        )

        return "\n".join(
            block.text
            for block in response.content
            if block.type == "text"
        )
