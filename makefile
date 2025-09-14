.PHONY: make_app
make_app:
    # dynamic argument
	uv run python manage.py startapp $(appname) 


.PHONY: run
run:
	uv run python manage.py runserver