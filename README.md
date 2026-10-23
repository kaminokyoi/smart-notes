# SmartNotes

A personal **note-taking web app** built with **Django**. Users sign up, log in and manage their own notes (create, read, edit, delete) in a clean Tailwind / daisyUI interface.

> Learning project (Django, spring 2025).

## Features

- User registration, login and logout (Django authentication)
- Landing page and a private notes area
- Each user sees only their own notes in the list
- Create, view, edit and delete notes
- Tailwind CSS + daisyUI styling through `django-tailwind`
- `django-browser-reload` for auto-reload in development

## Tech stack

- Python 3, Django 5.1+
- SQLite
- Tailwind CSS 3, daisyUI (built with npm via `django-tailwind`)
- Class-based views (`ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView`)

## Project structure

```
smartnotes/   project settings and root URLs
home/         landing page, login and logout
notes/        Notes model, forms, views and templates
theme/        Tailwind app (sources in theme/static_src)
```

## Data model

`Notes`: `title`, `text`, `created` (auto timestamp), `user` (foreign key to Django's `User`).

## Routes

| URL                      | Description                  |
| ------------------------ | ---------------------------- |
| `/`                      | Welcome page                 |
| `/signup/`               | Create an account            |
| `/login`, `/logout`      | Authentication               |
| `/notes/`                | List of your notes           |
| `/notes/new`             | Create a note                |
| `/notes/<id>/`           | Note detail                  |
| `/notes/<id>/edit/`      | Edit a note                  |
| `/notes/<id>/delete/`    | Delete a note                |
| `/admin/`                | Django admin                 |

## Getting started

Requirements: Python 3.10+ and Node.js / npm (for Tailwind).

```bash
git clone <repo-url>
cd <repo-folder>

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

python manage.py migrate
python manage.py tailwind install
python manage.py runserver
```

In a second terminal, run `python manage.py tailwind start` to rebuild the CSS while developing.

> `NPM_BIN_PATH` in `smartnotes/settings.py` currently points to a Windows install of npm. Update it to match your machine (for example `/usr/bin/npm`).

## Known limitations / next steps

- The detail, edit and delete views do not yet check that the note belongs to the logged-in user — adding ownership checks (and `LoginRequiredMixin`) is the next step
- Environment-based settings (secret key, `DEBUG`, allowed hosts)
- Automated tests
- Search and tags for notes
