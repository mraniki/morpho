import os
import logging
from dynaconf import Dynaconf

ROOT = os.path.dirname(__file__)

settings = Dynaconf(
    envvar_prefix="MORPHO",
    root_path=os.path.dirname(ROOT),
    settings_files=[
        os.path.join(ROOT, "default_settings.toml"),
        'settings.toml',
        '.secrets.toml'
        ],
    load_dotenv=True,
    environments=True,
    merge=True,
    default_env="default",
)

#  🧐LOGGING
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=settings.loglevel
)
logger = logging.getLogger("FORM")
if settings.loglevel == "DEBUG":
    logging.getLogger("websockets.client").setLevel(logging.WARNING)
    logging.getLogger("pyppeteer").setLevel(logging.WARNING)
