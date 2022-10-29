from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()
class Settings(BaseSettings):
    database_hostname: str
    database_port: str 
    database_password: str 
    database_name: str = 'africatradetoday'
    database_username: str 
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int = 30

    class Config:
        env_file = ".env"

settings = Settings()