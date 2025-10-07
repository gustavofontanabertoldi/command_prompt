# This script is used to run

# Exit early if any commands fail
set -e

exec pipenv run python3 -u -m app.main "$@"
