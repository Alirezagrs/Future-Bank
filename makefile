.PHONY: make_app
make_app:
    # dynamic argument
	uv run python manage.py startapp $(appname) 


.PHONY: run
run:
	uv run python manage.py runserver


.PHONY: check
check:
	uv run python manage.py check


.PHONY: makemigrations
makemigrations:
	uv run python manage.py makemigrations


.PHONY: migrate
migrate:
	uv run python manage.py migrate


.PHONY: createsuperuser
createsuperuser:
	uv run python manage.py createsuperuser