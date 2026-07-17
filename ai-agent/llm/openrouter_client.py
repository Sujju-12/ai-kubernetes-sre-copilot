import requests
from config.settings import settings


class OpenRouterClient:

    def __init__(self):

        self.url = "https://openrouter.ai/api/v1/chat/completions"
        self.api_key = settings.OPENROUTER_API_KEY
        self.model = settings.OPENROUTER_MODEL

    def generate(self, prompt):

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/Sujju-12/ai-kubernetes-sre-copilot",
            "X-Title": "AI Kubernetes SRE Copilot"
        }

        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You are a Senior Kubernetes Site Reliability Engineer. "
                        "Always provide evidence-based troubleshooting. "
                        "Never invent Kubernetes resources or logs. "
                        "If evidence is insufficient, clearly state that."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0.2,
            "max_tokens": 2000
        }

        try:

            print(f"\n🤖 Using OpenRouter Model: {self.model}")

            response = requests.post(
                self.url,
                headers=headers,
                json=payload,
                timeout=300
            )

            response.raise_for_status()

            data = response.json()

            if "choices" not in data:
                raise Exception(f"Unexpected OpenRouter response: {data}")

            return data["choices"][0]["message"]["content"]

        except requests.exceptions.Timeout:
            raise Exception("OpenRouter request timed out.")

        except requests.exceptions.HTTPError as e:

            try:
                error = response.json()
                raise Exception(f"OpenRouter HTTP Error: {error}")
            except Exception:
                raise Exception(f"OpenRouter HTTP Error: {e}")

        except requests.exceptions.RequestException as e:
            raise Exception(f"OpenRouter Connection Error: {e}")
