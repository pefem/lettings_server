# ----------------------------------------------------------------------------------------------------------
# File: settings.py
#
#   Description: setting helper class
#
#   Rules:
#       - All temporary code should be included in #[TODO] Begin and #[TODO] End
#       - Where possible use multiple import statements if making multiple imports
#       - Adhere to comments on where to place imports and fixture code
#       - if requesting a fixture but the fixture does not require a reference within the
#         function, do not pass as argument. Pass fixture using 'pytest.mark.useFixtures()'
# ----------------------------------------------------------------------------------------------------------

# ---------------------------------------- Standard library imports ----------------------------------------
from pathlib import Path
from functools import lru_cache

# ----------------------------------------------------------------------------------------------------------

# ---------------------------------------- Third party imports ---------------------------------------------
from pydantic_settings import BaseSettings

# ----------------------------------------------------------------------------------------------------------

# ---------------------------------------- Local Application imports ---------------------------------------
from dotenv import load_dotenv

# ----------------------------------------------------------------------------------------------------------

# ---------------------------------------- Global declarations (variables & const) -------------------------
env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)
# ----------------------------------------------------------------------------------------------------------


class Settings(BaseSettings):

    # DATABASE SETTINGS
    postgres_user: str
    server_name: str
    port: int
    postgres_password: str
    postgres_db: str
    pg_admin_email: str
    pgadmin_password: str

    # JWT SETTINGS
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int


# --------------------------------------------------------


@lru_cache()
def get_settings() -> Settings:
    return Settings()


# ----------------------------------------------------------------------------------------------------------
# End of File
# ----------------------------------------------------------------------------------------------------------
