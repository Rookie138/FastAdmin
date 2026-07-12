from pydantic_settings import BaseSettings, SettingsConfigDict

from functools import lru_cache
import os

from app.config.path_conf import ENV_DIR


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=os.path.join(ENV_DIR , f".env.{os.getenv('ENVIRONMENT',"dev")}"),
                                      env_file_encoding="utf-8",
                                      extra="ignore",
                                      case_sensitive=True)

    # ================================================= #
    # ******************** 数据库配置 ******************* #
    # ================================================= #

    DATABASE_ECHO: bool = True
    EXPIRE_ON_COMMIT: bool = False

    DATABASE_TYPE: str = "mysql"
    DATABASE_HOST: str = "localhost"
    DATABASE_PORT: int = 3306
    DATABASE_USER: str = "root"
    DATABASE_PASSWORD: str = ""
    DATABASE_NAME: str = "fastadmin"

    # ================================================= #
    # ******************** 密码哈希加密 ******************* #
    # ================================================= #
    SECRET_KEY: str = ""
    ALGORITHM: str = "HS256"



    @property
    def ASYNC_DB_URI(self) -> str:
        db_connect: str = f"mysql+asyncmy://{self.DATABASE_USER}:{self.DATABASE_PASSWORD}@{self.DATABASE_HOST}:{self.DATABASE_PORT}/{self.DATABASE_NAME}?charset=utf8mb4"
        return db_connect

    @property
    def DB_URI(self) -> str:
        db_connect: str = f"mysql+pymysql://{self.DATABASE_USER}:{self.DATABASE_PASSWORD}@{self.DATABASE_HOST}:{self.DATABASE_PORT}/{self.DATABASE_NAME}?charset=utf8mb4"
        return db_connect



@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()

settings = get_settings()
