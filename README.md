# Simple App with Django



A simple project with user singup and export to differents types, made with <a href="https://www.djangoproject.com/download/">Django Framework.</a>

<a href="https://pipenv.pypa.io/en/latest/">Pipenv</a> used for packaging.

## Requirements

You gonna need Python in your machine and <a href="https://pipenv.pypa.io/en/latest/">Pipenv</a> to install the dependencies

Read the Pipfile file for more info.

## Installing

Get the package from source:

```
    git clone https://github.com/mayronH/desafio-frexco
```

Install requirements with pipenv

```
    pipenv install
```

Create the SuperUser with: 

```
    python manage.py createsuperuser 
```

Run all migrations: 

```
    python manage.py migrate
```

## Features

- Custom User
- Export users with JSON, XLSX and CSV

## Built With

- <a href="https://www.djangoproject.com/download/">Django</a>
- Python 3.10
- <a href="https://xlsxwriter.readthedocs.io/index.html">XlsxWriter</a>

## Authors

- **Mayron Henrique Sousa Carvalho**

## License

[MIT license](https://opensource.org/licenses/MIT).