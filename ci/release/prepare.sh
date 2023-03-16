#!/usr/bin/env bash

set -euo pipefail

version="${1}"

# set version
poetry version "$version"

# build artifacts
poetry build

echo "built artifacts:"

ls -l dist

echo "Thats whats in dist"

# ensure that the built wheel has the correct version number
unzip -p "dist/glasswool-${version}-py3-none-any.whl" glasswool/__init__.py | \
  grep -q "__version__ = \"$version\""