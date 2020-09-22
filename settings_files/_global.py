import os

SETTINGS_DIR=os.path.dirname(os.path.abspath(__file__))
ROOT_DIR=os.path.dirname(SETTINGS_DIR)
DATA_DIR=os.path.join(ROOT_DIR,'data')

DTOKEN=os.getenv("DTOKEN",False)

REDDIT_ID=os.getenv("REDDIT_ID",False)
REDDIT_SECRET=os.getenv("REDDIT_SECRET",False)


#permissions

MODERATOR_ROLE="Moderator"