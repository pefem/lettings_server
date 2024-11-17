# ----------------------------------------------------------------------------------------------------------
# File: main.py
#
#   Description: program entry point
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
from fastapi import FastAPI

# ----------------------------------------------------------------------------------------------------------

# ---------------------------------------- Local Application imports ---------------------------------------
from app.config.database import engine
from app.models import db_models
from app.user_management.api import create_user_router
from app.property_management.api import create_property_router
from app.utils.logging.logger import logger

# ----------------------------------------------------------------------------------------------------------

# ---------------------------------------- Global declarations (variables & const) -------------------------
# * declarations here
# ----------------------------------------------------------------------------------------------------------


def create_app() -> FastAPI:
    """
    create and configure the fastapi app

    Args:
        none

    Returns:
        FastAPI: Configured fastapi app instance
    """
    # ----------------------------------------
    # Create the tables
    db_models.Base.metadata.create_all(bind=engine)

    app = FastAPI()
    logger.info("Starting API...")

    # ----------------------------------------

    @app.get("/")
    async def health_check():
        return True

    user_router = create_user_router()
    property_router = create_property_router()

    app.include_router(user_router, prefix="/users", tags=["users"])
    app.include_router(property_router, prefix="/property", tags=["property"])

    return app


# ----------------------------------------------------------------------------------------------------------
# End of File
# ----------------------------------------------------------------------------------------------------------
