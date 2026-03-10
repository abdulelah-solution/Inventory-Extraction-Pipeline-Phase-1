import sys
import os
import logging
from pathlib import Path
from dotenv import load_dotenv
from utils import get_wsl_host_ip

load_dotenv()

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / 'data'
OUTPUT_DIR = BASE_DIR / 'output'

DATA_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

file_path = str(DATA_DIR / 'app.log')

logging.basicConfig(
                    filename=file_path,
                    filemode='w',
                    format='%(asctime)s | %(name)s | %(levelname)s | %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S %p',
                    level=logging.INFO,
                    encoding='utf-8-sig'
            )

logger.info('--- Start loading environment variables ---')

try:
    DB_SERVER = os.getenv('DB_SERVER') or get_wsl_host_ip()
    DB_NAME = os.getenv('DB_NAME')
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')

    if not all([DB_SERVER, DB_NAME, DB_USER, DB_PASSWORD]):
        raise ValueError('One or more environment variables are missing in .env file!')

    logger.info('--- ✅ All values loaded successfully ---')
    
except ValueError as e:
    logger.critical(f'❌ Critical Setup Error: {e}')
    print(f'\n[ERROR]: {e}')
    sys.exit(1)

except Exception as e:
    logger.error(f'❌ Unexpected Error: {e}')
    sys.exit(1)