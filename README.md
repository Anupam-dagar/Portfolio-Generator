# Portfolio-Generator
A webapp made in Django to generate a portfolio  
# Generate your portfolio in 3 easy steps:
1. Login or signup
2. Enter required details.
3. View your generated portfolio.
## Download dependencies
Always use virtual environment  
``` pip install -r requirements.txt ```
## Running project locally
1. Create a file sensitive_email_data.py and place it in "myproject" directory.
2. There is a template sensitive_email_data(template).md which includes data to include in sensitive_email_data.py.
3. Cloned repo will not work unless you provide your secret key.
4. Create a file secret_keys.py and place it in "myproject" directory.
5. There is a template secret_keys(template).md which includes data to be included in secret_keys.py
6. Generate a secret key using Django secret key generator.
7. Paste the key generated in secret_keys.py created using template.
8. Create a file oauth_keys.py and place it in "myproject" directory.
9. There is a template for oauth_keys(template).md which includes data to be included in oauth_keys.py
10. Install the requirements from requirements.txt
11. `pip install -r requirements.txt`
12. Full documentation can be found [here](https://github.com/Anupam-dagar/Portfolio-Generator/wiki)
