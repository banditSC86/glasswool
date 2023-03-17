# list justfile recipes
default:
    just --list

# format code
fmt:
    black .
    ruff --fix .

# run pytest for ci; additional arguments are forwarded to pytest
ci-check *args:
    poetry run pytest --junitxml=junit.xml --cov=glasswool --cov-report=xml:coverage.xml {{ args }}

#    poetry run pytest  --cov=glasswool --cov-report=xml:coverage.xml {{ args }}
