## ----------------------------------------------------------------------
## Makefile is to manage Django project.
## ----------------------------------------------------------------------
include docker/envs/equipment.env
export

compose_files=-f docker-compose.yml

help:     ## Show this help.
		@sed -ne '/@sed/!s/## //p' $(MAKEFILE_LIST)

start:  ## Start project
		cd docker && DOCKER_BUILDKIT=1 docker-compose $(compose_files) up -d --build --force-recreate

stop:
		cd docker && DOCKER_BUILDKIT=1 docker-compose $(compose_files) down

init:  ## First and full initialization. Create database, superuser and collect static files
		docker exec -it equip_django bash -c \
		'python manage.py migrate && python manage.py createsuperuser --noinput && python manage.py collectstatic --noinput'

loaddata:  ## Load demo data
		docker exec -it muzcat_django bash -c \
		'python manage.py loaddata demo/demo_data.json'

migrate:
		cd app && \
		python manage.py makemigrations --settings=config.settings_dev && \
		python manage.py migrate --settings=config.settings_dev

runserver:
		cd app && python manage.py runserver --settings=config.settings_dev

superuser:
		cd app && python manage.py createsuperuser --settings=config.settings_dev

shell:
		cd app && python manage.py shell --settings=config.settings_dev

lint-install:
		pip install lxml mypy wemake-python-styleguide flake8-html types-requests types-pytz

lint:
		isort app/
		flake8 app/ --show-source
		mypy app/ --ignore-missing-imports --no-strict-optional --exclude /migrations/ --exclude /tests/

test:
		cd app/tests && pytest . -vvs