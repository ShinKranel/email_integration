from dotenv import load_dotenv

from pydantic_settings import SettingsConfigDict, BaseSettings

load_dotenv()


class Settings(BaseSettings):
    PROJECT_TITLE: str

    DB_HOST: str
    DB_PORT: str
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    STATIC_DIR: str
    TEMPLATES_DIR: str

    BACKEND_CORS_ORIGINS: list[str]

    @property
    def DATABASE_URL_ASYNC(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def DATABASE_URL(self):
        return f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
