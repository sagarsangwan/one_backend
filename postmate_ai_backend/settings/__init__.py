from .base_settings import *
import os

if os.environ["mod"] == "production":
    from .prod_settings import *

else:
    from .local_settings import *
