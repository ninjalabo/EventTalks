__version__ = "0.0.1"
# DataTalks/__init__.py  (add at the top)
from pathlib import Path              # cleaner path handling than os.path
from dotenv import load_dotenv        # function that loads a .env file
from .arena import *


load_dotenv(Path(__file__).parent.parent / ".env", override=False)