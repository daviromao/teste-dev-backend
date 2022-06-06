# Olisaude Backend Developer Challenge

This project was created using the Olisaude challenge. It's an API to manage (CRUD) clients and get 10 clients with the highest health risk. Python, django and django rest framework was the technologies used in this project.

You can see the API Documentation at ---

# Installation and tests instructions

To run this project it is necessary python >= 3.8.


### Clone this repository: 

```sh
git clone git@github.com:daviromao/teste-dev-backend.git

cd teste-dev-backend
```


### Create the environment:
```sh
python3 -m venv env
```


### Activate the envirnoment:

on Windows:
```sh
.\env\Scripts\activate               
```

on Ubuntu:
```sh
source env/bin/activate
```


### Install the reqeuirements:

```
pip install requirements.txt
```


### Run migrations:

```
python manage.py makemigrations
python manage.py migrate
```


### Run project:
```sh
python manage.py runserver
```


#### Acces the local API at http://localhost:8000/


### Run tests:
```sh
python manage.py test
```

