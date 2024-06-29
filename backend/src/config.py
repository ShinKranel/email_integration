from dotenv import load_dotenv

from pydantic_settings import SettingsConfigDict, BaseSettings

load_dotenv()


class Settings(BaseSettings):
    PROJECT_TITLE: str

    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_NAME: str

    @property
    def DATABASE_URL_ASYNC(self):
        return f"postgres+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}%{self.POSTGRES_HOST}:\
                                    {self.POSTGRES_PORT}/{self.POSTGRES_NAME}"

    @property
    def DATABASE_URL(self):
        return f"postgres+psycopg2://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}%{self.POSTGRES_HOST}:\
                                    {self.POSTGRES_PORT}/{self.POSTGRES_NAME}"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
