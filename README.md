## Django-Blueprint

Django-Blueprint is a project template designed for the Django 3.0 Web Framework,
which allows a Python / Django Developer to kickstart a new project without the
hassle of all the mundane setup and configuration.

#### Features
1. Popular Frameworks
..* [Bootstrap4](https://getbootstrap.com/)
..* [FontAwesome](https://fontawesome.com/)
..* [jQuery 3.5](https://jquery.com/)
2. Optimized Settings Files
..* Separate files for each environment
..* Hardened security baseline
3. Utility Scripts

#### Dependencies
* Python >= 3.8

#### Usage

1. Create a Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install Django Web Framework
```bash
pip3 install Django
```

3. Create your Project
```bash
django-admin.py startproject --template=https://github.com/SquirrelBrain/django-blueprint/archive/master.zip --extension=py,js,css <project_name>
```

4. Install dependencies and complete project setup
```bash
cd <project_name>
pip3 install -r requirements/development.txt
python3 scripts/environment/persona.py
python3 manage.py migrate --run-syncdb
python3 manage.py createsuperuser
python3 manage.py runserver 0.0.0.0:8000
```

5. Login to your [Development Instance - Admin Portal](http://localhost:8000/admin)

#### License & Copyright
Copyright (c) 2020, Justin Keith. Licensed under the [MIT LICENSE](LICENSE)