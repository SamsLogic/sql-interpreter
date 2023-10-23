import os
import sys
from dotenv import load_dotenv

if os.environ.get('LOAD_FROM_ENV_FILE', '1') == '1':
    load_dotenv(override=True)

# OpenAI config
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', None)
OPENAI_BASE_URL = os.environ.get('OPENAI_BASE_URL', None)
OPENAI_API_TYPE = os.environ.get('OPENAI_API_TYPE', None)
TEMPERATURE = int(os.environ.get('TEMPERATURE', 0))
STOP = os.environ.get('STOP', "")
MAX_TOKENS = int(os.environ.get('MAX_TOKENS', 500))
TOP_P = int(os.environ.get('TOP_P', 1))
FREQUENCY_PENALTY = int(os.environ.get('FREQUENCY_PENALTY', 0))
PRESENCE_PENALTY = int(os.environ.get('PRESENCE_PENALTY', 0))
N_RESP = int(os.environ.get('N_RESP', 1))
TIMEOUT = int(os.environ.get('TIMEOUT', 60))

# DATABASE config
DB_HOST = os.environ.get('DB_HOST', None)
DB_PORT = os.environ.get('DB_PORT', None)
DB_USER = os.environ.get('DB_USER', None)
DB_PASSWORD = os.environ.get('DB_PASSWORD', None)
DB_NAME = os.environ.get('DB_NAME', None)

if OPENAI_API_KEY is None:
    print("OPENAI_API_KEY is not set")
    sys.exit(1)

if OPENAI_API_TYPE is None:
    print("OPENAI_API_TYPE is not set")
    sys.exit(1)

if OPENAI_API_TYPE == 'azure':
    if OPENAI_BASE_URL is None:
        print("OPENAI_BASE_URL is not set")
        sys.exit(1)

if DB_HOST is None:
    print("DB_HOST is not set")
    sys.exit(1)

if DB_PORT is None:
    print("DB_PORT is not set")
    sys.exit(1)

if DB_USER is None:
    print("DB_USER is not set")
    sys.exit(1)

if DB_PASSWORD is None:
    print("DB_PASSWORD is not set")
    sys.exit(1)

if DB_NAME is None:
    print("DB_NAME is not set")
    sys.exit(1)