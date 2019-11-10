[![Build Status](https://travis-ci.org/Bonifase/online-store.svg?branch=master)](https://travis-ci.org/Bonifase/online-store) [![Test Coverage](https://api.codeclimate.com/v1/badges/c840fc677f2993f86bbb/test_coverage)](https://codeclimate.com/github/Bonifase/online-store/test_coverage) [![Maintainability](https://api.codeclimate.com/v1/badges/c840fc677f2993f86bbb/maintainability)](https://codeclimate.com/github/Bonifase/online-store/maintainability)

#### Setup

Install virtuals environment with Python dependancies:

```
$ pipenv shell

$ pipenv install
```

#### Running the application

Run migartions then start the server

```

$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver

```

#### Running tests

```

$ python manage.py test

```
