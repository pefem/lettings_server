# ----------------------------------------------------------------------------------------------------------
# File: security.py
#
#   Description: security helper functions
#
#   Rules:
#       - All temporary code should be included in #[TODO] Begin and #[TODO] End
#       - Where possible use multiple import statements if making multiple imports
#       - Adhere to comments on where to place imports and fixture code
#       - if requesting a fixture but the fixture does not require a reference within the
#         function, do not pass as argument. Pass fixture using 'pytest.mark.useFixtures()'
# ----------------------------------------------------------------------------------------------------------

# ---------------------------------------- Standard library imports ----------------------------------------
from typing import Optional
from datetime import datetime, timedelta

# ----------------------------------------------------------------------------------------------------------

# ---------------------------------------- Third party imports ---------------------------------------------
from jose import JWTError, jwt
from passlib.context import CryptContext

# ----------------------------------------------------------------------------------------------------------

# ---------------------------------------- Local Application imports ---------------------------------------
from app.config.settings import get_settings

# ----------------------------------------------------------------------------------------------------------

# ---------------------------------------- Global declarations (variables & const) -------------------------
settings = get_settings()

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# ----------------------------------------------------------------------------------------------------------


def get_password_hash(password: str) -> str:
    """ """
    return pwd_context.hash(password)


# --------------------------------------------------------


def create_access_token(
    *, data: dict, expires_delta: Optional[timedelta] = None
) -> str:
    """ """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# ----------------------------------------------------------------------------------------------------------
# End of File
# ----------------------------------------------------------------------------------------------------------
