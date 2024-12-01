python -m black app
python -m black tests

autoflake --recursive app
autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place app --exclude=__init__.py
autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place tests --exclude=__init__.py

isort --combine-as app
isort --combine-as tests
