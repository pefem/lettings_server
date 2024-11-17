# ----------------------------------------------------------------------------------------------------------
# File: test_get_property.py
#
#   Description: get property tests
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

def test_get_all_properties_200(client, create_property):
    response = client.get(
        "/property/get-all-properties"
    )

    assert response.status_code == 200
    assert response.json()["success"] is True
    assert response.json()["properties"][0] == create_property.json()["property"]


# --------------------------------------------------------

def test_get_property_200(client, create_property):
    response = client.get(
        "/property/get-property/1"
    )

    assert response.status_code == 200
    assert response.json()["success"] is True


# ----------------------------------------------------------------------------------------------------------
# End of File
# ----------------------------------------------------------------------------------------------------------