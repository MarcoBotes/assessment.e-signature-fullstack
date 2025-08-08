"""
Here is just a little sample of something I like to do.

This is a problem I have always had as a python developer? Where do I put my constants and environment variables.
Typically, we store them in json with C# but for Python I choose the minimal approach to embed it in the python directly.

Gross overkill for this assessment but my take is - if you use 1 literal on at least 2 places = variable.
If you happen to use that in 2 different files = external module
"""
from enum import Enum, auto

class Constants:
    directory = 'signed_docs'

class Runtime(Enum):
    DEVELOPMENT = auto()
    TESTING = auto()
    PRODUCTION = auto()

class Environment:
    runtime = Runtime.TESTING
    # Trying something here, but basically - this is an immutable portion of startup, initially had this as a function but changed it to a property to avoid a comparison operation every request
    is_production = runtime == Runtime.PRODUCTION