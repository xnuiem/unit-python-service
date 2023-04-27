import os


class Config(object):
    logging_level = os.getenv('UNIT_PY_LOGGING_LEVEL', 'DEBUG')
    logging_file = os.getenv('UNIT_PY_LOGGING_FILE', '')
    cache_host = os.getenv('UNIT_PY_DATA_HOST', 'localhost')
    cache_port = os.getenv('UNIT_PY_DATA_PORT', 6307)
    cache_user = os.getenv('UNIT_PY_DATA_USER', 'admin')
    cache_pass = os.getenv('UNIT_PY_DATA_PASS', 'admin')
    cache_db = os.getenv('UNIT_PY_DATA_DB', 0)
    init_key = os.getenv('UNIT_PY_INIT_KEY', '6432asedfw34fraw')
    local_spec_path = os.getenv('UNIT_PY_SPEC_FILE', 'docs/openapi.yaml')
    spec_format = os.getenv('UNIT_PY_SPEC_FORMAT', 'yaml')
