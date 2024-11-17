# ----------------------------------------------------------------------------------------------------------
# File: api.py
#
#   Description: property router
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
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status, Body, Path

# ----------------------------------------------------------------------------------------------------------

# ---------------------------------------- Local Application imports ---------------------------------------
from app.config import auth
from app.schemas import user_schema
from app.schemas import property_schema
from app.config import database
from app.models import db_models
from app.property_management.database.query_functions import (
    insert_property,
    get_properties,
    get_a_property,
    remove_property
)
from app.property_management.response_bodies.get_properties import GetProperties
from app.property_management.response_bodies.get_single_property import GetSingleProperty
from app.utils.response_bodies.response_message import ResponseMessage

# ----------------------------------------------------------------------------------------------------------

# ---------------------------------------- Global declarations (variables & const) -------------------------
# * declarations here
# ----------------------------------------------------------------------------------------------------------


def create_property_router() -> APIRouter:
    """
    create and configure the property router

    Args:
        none

    Returns:
        APIRouter: Configured APIRouter instance
    """

    # ----------------------------------------
    router = APIRouter()
    # ----------------------------------------

    @router.post("/create-property", status_code=status.HTTP_201_CREATED, response_model=GetSingleProperty)
    async def create_property(
        current_user: user_schema.UserInDB = Depends(auth.get_current_user),
        body: property_schema.Property = Body(..., title="Request Body"),
        db: Session = Depends(database.get_session),
    ):
        if current_user.id != body.user_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="provided user id does not match logged in user id",
            )

        property_obj = insert_property(db=db, payload=body)
        property = property_obj.to_dict()
        del property["user"]


        return GetSingleProperty(
            success=True,
            message="project created successfully",
            property=property
        )
    
    # --------------------------------------------------------

    @router.get("/get-all-properties", response_model=GetProperties)
    async def get_all_properties(
        db: Session = Depends(database.get_session)
    ):
        property_list = get_properties(db=db)

        if not property_list:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No properties were found"
            )

        properties = [property_dict.to_dict() for property_dict in property_list]

        for item in properties:
            del item["user"]

        return GetProperties(
            success=True,
            message="all properties returned succesfully",
            total=len(properties),
            properties=properties
        )


    # --------------------------------------------------------

    @router.get("/get-property/{property_id}", response_model=GetSingleProperty)
    async def get_property(
        db: Session = Depends(database.get_session),
        property_id: int = Path(..., description="id of the property")
    ):
        property_obj = get_a_property(db=db, id=property_id)
        property = property_obj.to_dict()
        del property["user"]

        if not property:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"property with id {str(property_id)} was not found"
            )
        
        return GetSingleProperty(
            success=True,
            message=f"property with id {property_id} retrieved successfully",
            property=property
        )

    # --------------------------------------------------------

    @router.delete("/{property_id}", response_model=ResponseMessage)
    async def delete_property(
        db: Session = Depends(database.get_session),
        property_id: int = Path(..., description="id of the property")
    ):
        # [TODO]
        # enquire about making this a protected route

        property = get_a_property(db=db, id=property_id)

        if not property:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"property with id {str(property_id)} was not found"
            )
        
        remove_property(db=db, property=property)

        return ResponseMessage(
            success=True,
            message=f"property with id = {property_id}, deleted succesfully"
        )


    return router


# ----------------------------------------------------------------------------------------------------------
# End of File
# ----------------------------------------------------------------------------------------------------------
