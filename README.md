# Portfolio-Generator
A webapp made in Django to generate a portfolio.  

A sample portfolio built using hoxnox can be seen at [https://hoxnox.herokuapp.com/AnupamDagar/26/](http://hoxnox.herokuapp.com/AnupamDagar/26/)

## Please note that currently only Google oauth is working on the hosted app at [https://hoxnox.herokuapp.com](https://hoxnox.herokuapp.com)

# Generate your portfolio in 3 easy steps:
1. Login or signup
2. Enter required details.
3. View your generated portfolio.
## Download dependencies
Always use virtual environment  
``` pip install -r requirements.txt ```
## Running project locally
1. After cloning the repo you need to generate a Secret Key to run this project locally.
2. Generate a Secret Key using [Django Secret Key Generator](http://www.miniwebtool.com/django-secret-key-generator/).
3. Copy the Secret Key to your clipboard and paste in the Line 25 of settings.py file in myproject folder.
4. After installing the dependencies, in the terminal run  ```python manage.py makemigrations```
5. After that run ``` python manage.py migrate``` to apply the migartions.
6. To run the server type ```python manage.py runserver```.
7. The server will start running on port 8000 of your localhost.
8. To create an admin account type ```python manage.py createsuperuser``` in the terminal and fill in the details.
9. Now you can login using those credentials
