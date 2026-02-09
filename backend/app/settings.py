from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    JWT_SECRET: str
    CORS_ORIGINS: str = ""
    ADMIN_EMAIL: str = "admin@carbi.play"
    ADMIN_PASSWORD: str = "admin123"

    @property
    def cors_list(self):
        if not self.CORS_ORIGINS:
            return ["*"]
        return [x.strip() for x in self.CORS_ORIGINS.split(",") if x.strip()]

settings = Settings()
