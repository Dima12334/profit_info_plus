# Profit Info Plus challenge

## Installation
1. Clone repository:
```
git clone https://github.com/Dima12334/profit_info_plus.git
```
2. Create python virtual environment:
```
python3 -m venv <venv_name>
source <venv_name>/bin/activate
```
3. Install project dependencies:
```
pip install -r requirements.txt
```
4. Complete the config/.env file.
5. Run PostgreSQL using Docker container:
```
docker-compose up
```
or configure the PostgreSQL on your local machine.
6. Run migrations:
```
python manage.py migrate
```
7. Create django superuser:
```
python manage.py createsuperuser
```
8. Run server:
```
python manage.py runserver
```
9. Done. Use the App.
