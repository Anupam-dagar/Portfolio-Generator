#Create a file in my project sensitive_email_data.py
-- Add the following lines in it.
```
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = '-----------------'
EMAIL_HOST_PASSWORD = '---------------'
SERVER_EMAIL = '-------------------'
DEFULT_FROM_EMAIL = "-------------"
```
#Fill the field
```
EMAIL_HOST_USER = '-----------------'
SERVER_EMAIL = '-------------------'
DEFULT_FROM_EMAIL = "-------------"
```
-- with your gmail which will be used to send account confirmation email.
```
EMAIL_HOST_PASSWORD = '---------------'
```
-- with your gmail account password.
