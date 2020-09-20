import os

DEBUG=os.getenv("DEBUG",True)

if DEBUG:
    print("We Are In Debug")
    from pathlib import Path
    from dotenv import load_dotenv
    env_path=Path(".")/".env.debug"
    load_dotenv(dotenv_path=env_path)
    from settings_files.development import *
    print(DTOKEN)
else:
    print("We are in Production")
    from settings_files.production import *
    print(DTOKEN)