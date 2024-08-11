# Command line interface docs

Some commands what i used for this project:

```sh
pyenv install 3.12.0
pyenv versions
pyenv global 3.12
```

Install the poetry library

```sh
pip install poetry
```

Initialize the project in already existing directory

```sh
poetry init [args]
```

Initialize the project

```sh
poetry new example [args]
```

Set python version

```sh
pyenv local 3.12 [args]
poetry env use python3.12 [args]
```

Create a virtual environment and all dependencies

```sh
poetry install [args]
```

Start virtual environment

```sh
poetry shell [args]
poetry deactivate [args]
```

Run your program with

```sh
poetry run python run.py [args]
poetry pytest [args]
```

Additional commands

```sh
poetry env info [args]
```

```sh
poetry add request [args]
poetry add -D pytest
```

```sh
poetry remove request [args]
```

```sh
poetry show -tree [args]
```

```sh
poetry show --latest [args]
```

```sh
poetry config virtualenvs.in-project true [args]
```

```sh
pytest -v
```
