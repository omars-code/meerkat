# meerkat

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
This package created with Cookiecutter and the [sourcery-ai/python-best-practices-cookiecutter](https://github.com/sourcery-ai/python-best-practices-cookiecutter) project template. Then evolved into something new and beautiful!

