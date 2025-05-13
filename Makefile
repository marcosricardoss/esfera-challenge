all: cleanpyc install run

# installing

install:	
	pip install --upgrade pip
	pip install -r requirements.txt
	pip install -r requirements.dev.txt
	pip install -e .	

pip-compile:
	pip install pip-tools==7.1.0
	pip-compile requirements.in	 
	pip-compile requirements.dev.in

pip-sync:
	pip install pip-tools==7.1.0
	pip-sync requirements.txt
	pip-sync requirements.dev.txt
	pip install -e .

install-pre-commit:
	pre-commit install

# running

run:
	docker-compose up

makemigrations:
	alembic revision --autogenerate -m "cria tabela users"

migrate:
	alembic upgrade head

# testing

test: 	
	coverage run -m pytest -vv
	coverage xml
	coverage html
	coverage report

# versioning

bump:
	cz bump	
	cz changelog

changelog:	
	cz changelog

# misc

cleanpyc:
	find . -name "*.pyc" -exec rm -f {} \;
