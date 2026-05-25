from pydantic_settings import BaseSettings,SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env",extra="ignore")

    DB_CONNECTION:str
    RAZORPAY_KEY:str
    RAZORPAY_SECRET:str
    


settings  = Settings()  