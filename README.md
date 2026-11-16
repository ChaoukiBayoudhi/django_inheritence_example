# Django inheritance example

A Django project with 3 models.

## Tech stack

- Python 3
- Django
- Database: PostgreSQL

## Project structure

- `django_inheritence_example/`: project settings and root URLs
- `student/`: Django app
- Tests: `student/tests.py`

## Data model

| Model | App | Fields |
|---|---|---|
| `Student` | `student` | name, email, birthday |
| `Terminal` | `student` | espMark |
| `Bechelor` | `student` | studyYear |

## URL routes

Declared in `urls.py`:

- `/blog/`

## How to run

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install django psycopg2-binary
python manage.py migrate
python manage.py runserver
```

There is no `requirements.txt`; the packages above are the ones the settings and imports refer to.

`settings.py` is configured for PostgreSQL: create the database and use your own credentials before running `migrate`.

Then open `http://127.0.0.1:8000/`.

---

Author: [Chaouki Bayoudhi](https://github.com/ChaoukiBayoudhi)
