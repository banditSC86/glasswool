#!/usr/bin/env bash

set -euo pipefail

curdir="$PWD"
worktree="$(mktemp -d)"
branch="$(basename "$worktree")"

git worktree add "$worktree"

function cleanup() {
  cd "$curdir" || exit 1
  git worktree remove --force "$worktree"
  git worktree prune
  git branch -D "$branch"
}

trap cleanup EXIT ERR

cd "$worktree" || exit 1

node <<< 'console.log(JSON.stringify(require("./.releaserc.js")))' |
  jq '.plugins |= [.[] | select(.[0] != "@semantic-release/github")]' > .releaserc.json

git rm .releaserc.js
git add .releaserc.json
git commit -m 'test: semantic-release dry run' --no-verify --no-gpg-sign

# If this is set then semantic-release will assume the release is running
# against a PR.
#
# Normally this would be fine, except that most of the release process that is
# useful to test is prevented from running, even in dry-run mode, so we `unset`
# this variable here and pass `--dry-run` ourselves
unset GITHUB_ACTIONS

npx --yes \
  -p semantic-release \
  -p "@semantic-release/commit-analyzer" \
  -p "@semantic-release/release-notes-generator" \
  -p "@semantic-release/changelog" \
  -p "@semantic-release/exec" \
  -p "@semantic-release/git" \
  -p "@google/semantic-release-replace-plugin" \
  -p "conventional-changelog-conventionalcommits" \
  semantic-release \
  --ci \
  --dry-run \
  --branches "$branch" \
  --repository-url "file://$PWD"