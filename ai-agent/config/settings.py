import os


class Settings:

    APP_NAME = "AI Kubernetes SRE Copilot"

    VERSION = "1.0.0"

    DEBUG = True

    OPENROUTER_API_KEY = os.getenv(
        "OPENROUTER_API_KEY",
        ""
    )

    OPENROUTER_MODEL = os.getenv(
        "OPENROUTER_MODEL",
        "deepseek/deepseek-chat-v3.1"
    )


settings = Settings()
