INSTALLED_APPS = [
    'rest_framework',
    'rest_framework.authtoken',
    'api', 'barcode_payment_app'
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}