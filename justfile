# list justfile recipes
default:
    just --list

# format code
fmt:
    black .
    ruff --fix .
