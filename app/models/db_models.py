# ----------------------------------------------------------------------------------------------------------
# File: db_models.py
#
#   Description: model class for user and property
#
#   Rules:
#       - All temporary code should be included in #[TODO] Begin and #[TODO] End
#       - Where possible use multiple import statements if making multiple imports
#       - Adhere to comments on where to place imports and fixture code
#       - if requesting a fixture but the fixture does not require a reference within the
#         function, do not pass as argument. Pass fixture using 'pytest.mark.useFixtures()'
# ----------------------------------------------------------------------------------------------------------

# ---------------------------------------- Standard library imports ----------------------------------------
# imports here

# ----------------------------------------------------------------------------------------------------------

# ---------------------------------------- Third party imports ---------------------------------------------
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Enum as SQLEnum
from sqlalchemy_serializer import SerializerMixin
# ----------------------------------------------------------------------------------------------------------

# ---------------------------------------- Local Application imports ---------------------------------------
from app.config.database import Base
from app.utils.enums.user_level import UserLevel
# ----------------------------------------------------------------------------------------------------------

# ---------------------------------------- Global declarations (variables & const) -------------------------
# * declarations here
# ----------------------------------------------------------------------------------------------------------


class Property(Base, SerializerMixin):
    __tablename__ = "property"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, unique=True)
    postcode = Column(String)
    city = Column(String)
    number_of_rooms = Column(Integer)
    user_id = Column(Integer, ForeignKey("user.id"))

    user = relationship("User")

# --------------------------------------------------------

class User(Base, SerializerMixin):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    level = Column(SQLEnum(UserLevel))

# ----------------------------------------------------------------------------------------------------------
# End of File
# ----------------------------------------------------------------------------------------------------------