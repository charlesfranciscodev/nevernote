# Notebook

A note taking web application.

## TODO

* "WYSIWYG" editor
* notebooks
* tags
* favorites
* sorting
* searching

## Completed API Routes

### Users
* **GET** `/users/`
* **POST** `/rest-auth/registration/`
* **POST** `/rest-auth/login/`
* **GET** `/users/{:id}/`
* **PUT** `/users/{:id}/`
* **DELETE** `/users/{:id}`

### Notebooks
* **GET** `/notebooks/`
* **POST** `/notebooks/`
* **GET** `/notebooks/{:id}/`
* **PUT** `/notebooks/{:id}/`
* **DELETE** `/notebooks/{:id}/`

### Notes
* **POST** `/notes/`
* **GET** `/notes/{:id}/`
* **PUT** `/notes/{:id}/`
* **DELETE** `/notes/{:id}/`

### Tags
* **GET** `/tags/`
* **POST** `/tags/`
* **GET** `/tags/{:id}/`
* **PUT** `/tags/{:id}/`
* **DELETE** `/tags/{:id}/`

## Completed User Stories

Coming soon...

## Dependencies

### Server (Django)

* python 3.7

To install the dependencies, run the following commands:

```bash
cd server
pip3 install -r requirements.txt
```

### Client (Node.js)

* node 12.3.1
* npm 6.9.0

To install the dependencies, run the following command:

```bash
cd client
npm install
```

## Links
* [Trello Board](https://trello.com/b/kUy04psi/notebook)
* [Django REST framework](https://www.django-rest-framework.org/)
* [Format suffixes](https://www.django-rest-framework.org/api-guide/format-suffixes/)
* [Official Django REST Framework Tutorial - A Beginners Guide](https://wsvincent.com/official-django-rest-framework-tutorial-beginners-guide/)
* [Django Rest Framework User Authentication Tutorial - Custom User Model + Social Auth](https://wsvincent.com/django-rest-framework-user-authentication-tutorial/)
