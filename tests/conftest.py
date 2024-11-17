# ----------------------------------------------------------------------------------------------------------
# File: conftest.py.py
#
#   Description: conftest fixtures
#
#   Rules:
#       - All temporary code should be included in #[TODO] Begin and #[TODO] End
#       - Where possible use multiple import statements if making multiple imports
#       - Adhere to comments on where to place imports and fixture code
#       - if requesting a fixture but the fixture does not require a reference within the
#         function, do not pass as argument. Pass fixture using 'pytest.mark.useFixtures()'
# ----------------------------------------------------------------------------------------------------------

# ---------------------------------------- Standard library imports ----------------------------------------
from datetime import datetime
import sys
import os
from typing import Generator

# ----------------------------------------------------------------------------------------------------------

# ---------------------------------------- Third party imports ---------------------------------------------
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

# ----------------------------------------------------------------------------------------------------------
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.run import app
from app.config.database import Base, get_session
from app.models.db_models import User

# ---------------------------------------- Local Application imports ---------------------------------------
# imports here
# ----------------------------------------------------------------------------------------------------------

# ---------------------------------------- Global declarations (variables & const) -------------------------
engine = create_engine("sqlite:///./fastapi.db")
SessionTesting = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ----------------------------------------------------------------------------------------------------------


@pytest.fixture(scope="function")
def test_session() -> Generator:
    session = SessionTesting()
    try:
        yield session
    finally:
        session.close()


# ----------------------------------------


@pytest.fixture(scope="function")
def app_test():
    Base.metadata.create_all(bind=engine)
    yield app
    Base.metadata.drop_all(bind=engine)


# ----------------------------------------


@pytest.fixture(scope="function")
def client(app_test, test_session):
    def _test_db():
        try:
            yield test_session
        finally:
            pass

    app_test.dependency_overrides[get_session] = _test_db

    return TestClient(app_test)


# ----------------------------------------


@pytest.fixture()
def user_registration_details():

    return {
        "email": "user@example.com",
        "username": "userme",
        "level": "normal",
        "password": "string",
    }


# ----------------------------------------


@pytest.fixture()
def user_login_details():

    return {"username": "userme", "password": "string"}


# ----------------------------------------


@pytest.fixture()
def property_details():

    return {
        "address": "string",
        "postcode": "string",
        "city": "string",
        "number_of_rooms": 3,
        "user_id": 1,
    }


# ----------------------------------------


@pytest.fixture()
def register_user(client, user_registration_details):

    client.post("/users/register/", json=user_registration_details)


# ----------------------------------------


@pytest.fixture()
def register_and_login(client, register_user, user_login_details):

    response = client.post("/users/token", data=user_login_details)
    return response.json()

# ----------------------------------------

@pytest.fixture()
def create_property(client, register_and_login, property_details):

    response = client.post(
        "/property/create-property",
        json=property_details,
        headers={
            "Authorization": f"{register_and_login['token_type']} {register_and_login['access_token']}"
        }
    )

    return response


# ----------------------------------------------------------------------------------------------------------
# End of File
# ----------------------------------------------------------------------------------------------------------
