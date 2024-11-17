
# ----------------------------------------------------------------------------------------------------------
# File: query_functions.py
#
#   Description: property query functions
#
#   Rules:
#       - All temporary code should be included in #[TODO] Begin and #[TODO] End
#       - Where possible use multiple import statements if making multiple imports
#       - Adhere to comments on where to place imports and fixture code
#       - if requesting a fixture but the fixture does not require a reference within the
#         function, do not pass as argument. Pass fixture using 'pytest.mark.useFixtures()'
# ----------------------------------------------------------------------------------------------------------

# ---------------------------------------- Standard library imports ----------------------------------------
# * imports here 

# ----------------------------------------------------------------------------------------------------------

# ---------------------------------------- Third party imports ---------------------------------------------
from sqlalchemy.orm import Session
# ----------------------------------------------------------------------------------------------------------

# ---------------------------------------- Local Application imports ---------------------------------------
from app.config.database import get_session
from app.models import db_models
from app.schemas.property_schema import Property
from app.schemas import property_schema
# ----------------------------------------------------------------------------------------------------------

# ---------------------------------------- Global declarations (variables & const) -------------------------
# * declarations here
# ----------------------------------------------------------------------------------------------------------

def insert_property(db: Session, payload: property_schema):
    db_property = db_models.Property(**payload.model_dump())
    db.add(db_property)
    db.commit()
    db.refresh(db_property)

    return db_property

# --------------------------------------------------------

def get_properties(db: Session) -> list:
    return db.query(db_models.Property).all()

# --------------------------------------------------------

def get_a_property(db: Session, id: int):
    return db.query(db_models.Property).filter(db_models.Property.id == id).first()

# --------------------------------------------------------

def remove_property(db: Session, property: Property):
    db.delete(property)
    db.commit()

# ----------------------------------------------------------------------------------------------------------
# End of File
# ----------------------------------------------------------------------------------------------------------