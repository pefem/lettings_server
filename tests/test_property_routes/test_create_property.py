# ----------------------------------------------------------------------------------------------------------
# File: test_create_property.py
#
#   Description: create property tests
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
# imports here
# ----------------------------------------------------------------------------------------------------------

# ---------------------------------------- Local Application imports ---------------------------------------
# imports here
# ----------------------------------------------------------------------------------------------------------

# ---------------------------------------- Global declarations (variables & const) -------------------------
# * declarations here
# ----------------------------------------------------------------------------------------------------------


def test_create_property_200(client, register_and_login, property_details):
    """
    Test will create a property succesfully
    """

    response = client.post(
        "/property/create-property",
        json=property_details,
        headers={
            "Authorization": f"{register_and_login['token_type']} {register_and_login['access_token']}"
        }
    )
    assert response.status_code == 201

# --------------------------------------------------------

def test_create_property_without_auth_headers_400(client, property_details):
    """
    Test will try to create a property without authenticating
    """

    response = client.post(
        "/property/create-property/",
        json=property_details,
    )

    assert response.status_code == 401

# ----------------------------------------------------------------------------------------------------------
# End of File
# ----------------------------------------------------------------------------------------------------------
