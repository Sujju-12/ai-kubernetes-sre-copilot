import os


class Settings:
    """
    Application configuration.
    Reads values from environment variables.
    """

    # -----------------------------
    # Gemini Configuration
    # -----------------------------
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
    
    GEMINI_MODEL = os.getenv(
        "GEMINI_MODEL",
        "gemini-2.0-flash"
)
    
    # -----------------------------
    # Application
    # -----------------------------
    APP_NAME = "AI Kubernetes SRE Copilot"

    VERSION = "1.0.0"

    DEBUG = True


settings = Settings()
