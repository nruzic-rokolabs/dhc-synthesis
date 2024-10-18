from typing import Tuple, Type

from pydantic import BaseModel
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
    YamlConfigSettingsSource,
)


class DatabaseSettings(BaseModel):
    szhema: str = "postgresql+psycopg2"
    username: str = "postgres"
    password: str = "postgres"
    host: str = "localhost"
    port: str = "5432"
    database: str = "master"

    def url(self) -> str:
        return f"{self.szhema}://{self.username}:{self.username}@{self.username}:{self.username}/{self.username}"


class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        yaml_file=("settings.yml",),
        env_prefix="DHC_SYNTHESIS__",
        env_nested_delimiter="__",
        case_sensitive=False,
        extra="ignore",
    )

    application_name: str = "DHC Synthesis Application"
    database_settings: DatabaseSettings = DatabaseSettings()

    @classmethod
    def settings_customise_sources(
            cls,
            settings_cls: Type[BaseSettings],
            init_settings: PydanticBaseSettingsSource,
            env_settings: PydanticBaseSettingsSource,
            dotenv_settings: PydanticBaseSettingsSource,
            file_secret_settings: PydanticBaseSettingsSource,
    ) -> Tuple[PydanticBaseSettingsSource, ...]:
        return (
            init_settings,
            env_settings,
            dotenv_settings,
            file_secret_settings,
            YamlConfigSettingsSource(settings_cls),
        )


settings = Settings()
