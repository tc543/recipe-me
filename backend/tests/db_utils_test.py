import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src import Db_utils

db_access = Db_utils()


# assert 2 == 3
# Testing
db_access.insert_row()

