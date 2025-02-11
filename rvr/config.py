"""
Configuration for various Flask plugins
"""
# Some of these can be overridden in local_settings.py
WTF_CSRF_TIME_LIMIT = None  # No time limit on form submission (minor risk)
SECRET_KEY = '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'  # Overridden in local_settings
DEBUG = True
RELOADER = False
OPENID_FS_STORE_PATH = 'openid-store'
OIDC_CLIENT_SECRETS = 'client_secrets.json'