# Test Django JWT

## Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
```

## Running
```bash
source venv/bin/activate
python manage.py runserver
```

## Testing
```bash
source venv/bin/activate
python manage.py test
```

### TODO
1. Create a django app
2. Create a user model
3. Create admin for this model
4. /login enpoint which accepts username, password and return jwt
5. /profile endpoint which accepts jwt in header and return firstname and lastname

6. Create a middleware which will check if the user is authenticated or not
7. Create a decorator which will check if the user is authenticated or not

8. /update-profile to return the firstname and lastname from the request object
