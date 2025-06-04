# Getting Started

## Installation

Python 3.13 is required. If you don't have Python 3.13 or higher, download [here](https://www.python.org/downloads/).

Then install [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

Create a virtualenv in this directory and activate it:
```shell
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

Install the project dependencies:

```shell
pip install -r requirements.txt
```

Set up the database. Locally, this will create a new SQLite database:

```shell
python transactionapi/manage.py migrate
```

Run the Django server:

```shell
python transactionapi/manage.py runserver
```

Your Django project is now live, locally. In your browser, go to: http://127.0.0.1:8000/.