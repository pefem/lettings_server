# ----------------------------------------------------------------------------------------------------------
# File: user_level.py
#
#   Description: UserLevel enum class
#
#   Rules:
#       - All temporary code should be included in #[TODO] Begin and #[TODO] End
#       - Where possible use multiple import statements if making multiple imports
#       - Adhere to comments on where to place imports and fixture code
#       - if requesting a fixture but the fixture does not require a reference within the
#         function, do not pass as argument. Pass fixture using 'pytest.mark.useFixtures()'
# ----------------------------------------------------------------------------------------------------------

# ---------------------------------------- Standard library imports ----------------------------------------
from enum import Enum

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


class UserLevel(str, Enum):
    ADMIN = "admin"
    NORMAL = "normal"


# ----------------------------------------------------------------------------------------------------------
# End of File
# ----------------------------------------------------------------------------------------------------------
