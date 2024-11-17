# ----------------------------------------------------------------------------------------------------------
# File: api.py
#
#   Description: user router
#
#   Rules:
#       - All temporary code should be included in #[TODO] Begin and #[TODO] End
#       - Where possible use multiple import statements if making multiple imports
#       - Adhere to comments on where to place imports and fixture code
#       - if requesting a fixture but the fixture does not require a reference within the
#         function, do not pass as argument. Pass fixture using 'pytest.mark.useFixtures()'
# ----------------------------------------------------------------------------------------------------------

# ---------------------------------------- Standard library imports ----------------------------------------
from datetime import timedelta

# ----------------------------------------------------------------------------------------------------------

# ---------------------------------------- Third party imports ---------------------------------------------
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

# ----------------------------------------------------------------------------------------------------------

# ---------------------------------------- Local Application imports ---------------------------------------
from app.config import auth, security, database
from app.models import db_models
from app.schemas import user_schema

# ----------------------------------------------------------------------------------------------------------

# ---------------------------------------- Global declarations (variables & const) -------------------------
# * declarations here
# ----------------------------------------------------------------------------------------------------------


def create_user_router() -> APIRouter:
    """
    create and configure the user router

    Args:
        none

    Returns:
        APIRouter: Configured APIRouter instance
    """
    # ----------------------------------------
    router = APIRouter()
    # ----------------------------------------

    @router.post("/register/", response_model=user_schema.UserInDBBase)
    async def register(
        user_in: user_schema.UserIn, db: Session = Depends(database.get_session)
    ):
        db_user = auth.get_user(db, username=user_in.username)
        if db_user:
            raise HTTPException(status_code=400, detail="Username already registered")
        db_user = (
            db.query(db_models.User)
            .filter(db_models.User.email == user_in.email)
            .first()
        )
        if db_user:
            raise HTTPException(status_code=400, detail="Email already registered")

        hashed_password = security.get_password_hash(user_in.password)
        db_user = db_models.User(
            **user_in.model_dump(exclude={"password"}), hashed_password=hashed_password
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return db_user

    # --------------------------------------------------------

    @router.post("/token", response_model=user_schema.Token)
    async def login_for_access_token(
        form_data: OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(database.get_session),
    ):
        user = auth.get_user(db, username=form_data.username)
        if not user or not security.pwd_context.verify(
            form_data.password, user.hashed_password
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        access_token_expires = timedelta(minutes=security.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = security.create_access_token(
            data={"sub": user.username}, expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}

    return router


# ----------------------------------------------------------------------------------------------------------
# End of File
# ----------------------------------------------------------------------------------------------------------
