# ==============================
# PRODUCTION SETTINGS
# ==============================

import os

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "_change_this_in_production_")

DEBUG = False

ALLOWED_HOSTS = [
    "siddsy.pro",
    "www.siddsy.pro",
]

# Tell Django it's behind Traefik (HTTPS proxy)
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Force HTTPS
SECURE_SSL_REDIRECT = True

# Secure cookies
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Fix CSRF behind HTTPS
CSRF_TRUSTED_ORIGINS = [
    "https://siddsy.pro",
    "https://www.siddsy.pro",
]

# Security headers
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"

# Static files (important for production)
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")