# ----------------------------------------------------------------------------------------------------------
# File: user_schema.py
#
#   Description: user model class
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

# ----------------------------------------------------------------------------------------------------------

# ---------------------------------------- Third party imports ---------------------------------------------
from pydantic import BaseModel, EmailStr

# ----------------------------------------------------------------------------------------------------------

# ---------------------------------------- Local Application imports ---------------------------------------
from app.utils.enums.user_level import UserLevel

# ----------------------------------------------------------------------------------------------------------

# ---------------------------------------- Global declarations (variables & const) -------------------------
# * declarations here
# ----------------------------------------------------------------------------------------------------------


class UserBase(BaseModel):
    email: EmailStr
    username: str
    level: UserLevel = UserLevel.NORMAL


# --------------------------------------------------------


class UserIn(UserBase):
    password: str


# --------------------------------------------------------


class UserInDBBase(UserBase):
    id: int

    class Config:
        orm_mode = True


# --------------------------------------------------------


class UserInDB(UserInDBBase):
    hashed_password: str


# --------------------------------------------------------


class TokenData(BaseModel):
    username: Optional[str] = None


# --------------------------------------------------------


class Token(BaseModel):
    access_token: str
    token_type: str


# ----------------------------------------------------------------------------------------------------------
# End of File
# ----------------------------------------------------------------------------------------------------------
