"""Configuration from environment variables; never store credentials in source."""
import os

def required(name):
    value = os.environ.get(name, '').strip()
    if not value:
        raise RuntimeError(f'Set {name} in your environment before starting the voice client')
    return value

ARK_API_KEY = required('ARK_API_KEY')
APP_ID = required('SPEECH_APP_ID')
APP_TOKEN = required('SPEECH_APP_TOKEN')
LLM_MODEL = required('ARK_MODEL')
