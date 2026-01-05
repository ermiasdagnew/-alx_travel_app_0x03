# Celery configuration
CELERY_BROKER_URL = 'amqp://guest@localhost//'
CELERY_RESULT_BACKEND = 'rpc://'  # optional, for task results
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_password'
DEFAULT_FROM_EMAIL = 'noreply@alxtravel.com'
