# meerkat

What do I get out of the box ?

-   Clean Architecture in Python

-   Falcon Framework RESTful API example

-   Health endpoint example

-   Marshmallow integration

-   Docker example



-   Github actions example runs the following

-   Tests

-   Black

-   Flake8

-   Mypy

-   isort

But what does it mean ?

-   Means it can be a starter project for your next project, whether falcon or CLI or * seriously any.

Now let's get started.

Installing the precommit/prepush hooks

## Setup
```sh
# Install dependencies
pipenv install --dev

# Setup pre-commit and pre-push hooks
pipenv run pre-commit install -t pre-commit
pipenv run pre-commit install -t pre-push
```

running tests:
```shell
make test
```
coverage found at: htmlcov/index.html
## Credits
- [sourcery-ai/python-best-practices-cookiecutter](https://github.com/sourcery-ai/python-best-practices-cookiecutter) project template. 