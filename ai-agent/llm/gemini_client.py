import google.generativeai as genai

from config.settings import settings


class GeminiClient:

    def __init__(self):

        genai.configure(api_key=settings.GEMINI_API_KEY)

        self.model = genai.GenerativeModel(
            model_name=settings.GEMINI_MODEL
        )

    def generate(self, prompt: str) -> str:

        try:

            response = self.model.generate_content(
                prompt,
                generation_config={
                    "temperature": 0.2,
                    "top_p": 0.95,
                    "max_output_tokens": 2048,
                }
            )

            if hasattr(response, "text") and response.text:
                return response.text

            if (
                hasattr(response, "candidates")
                and response.candidates
                and response.candidates[0].content.parts
            ):
                return response.candidates[0].content.parts[0].text

            return "Gemini returned an empty response."

        except Exception as e:

            return f"""
================ GEMINI ERROR ================

{str(e)}

==============================================
"""
