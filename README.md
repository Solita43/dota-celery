# DotaPro

## Deployment
### Build Command
- `./build.sh`
### Start Command
- `cd server && gunicorn wsgi:application`

## Version Control
- `pipenv run pip freeze --local > requirements.txt`

## Project Structure
- https://django-project-skeleton.readthedocs.io/en/latest/structure.html
- https://github.com/Mischback/django-project-skeleton

project_name/
├── config/
│   ├── settings/
│   │   ├── base.py
│   │   ├── local.py
│   │   ├── development.py
│   │   ├── staging.py
│   │   ├── production.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│
├── apps/
│   ├── app1/
│   │   ├── migrations/
│   │   ├── templates/
│   │   ├── static/
│   │   ├── tasks/
│   │   ├── utils/
│   │   ├── management/
│   │   ├── api/
│   │   │   ├── v1/
│   │   │   │   ├── serializers.py
│   │   │   │   ├── views.py
│   │   │   │   ├── filters.py
│   │   │   ├── v2/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── choices.py
│   │   ├── models.py
│   │   ├── signals.py
│   │   ├── urls.py
│   │   ├── views.py
│   ├── app2/
│   ├── app3/│
│
├── static/
│   ├── css/
│   ├── js/
│   ├── img/
│
├── media/
│
├── templates/
│
├── utils/
│
├── tasks/
│
├── management/
│
├── manage.py
│
