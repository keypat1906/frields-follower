# Friends and Followers

Install virtualenv
```
pip install virtualenv
```
On the project directory,

Create virtual environment
```
virtualenv venv
```
Activate
```
source venv/bin/activate
```

Install requirements including dependencies
```
pip install -r requirements.txt
```

Do Database migrations
```
./manage.py makemigrations
./manage.py migrate
```

Try creating a superuser for user management
```
./manage.py createsuperuser
```

Give necessary inputs

Run development server

```
./manage.py runserver 0.0.0.0:8080
```


API Endpoints


1. List all Users

GET http://localhost:8080/api/users/


2. Create new Users

POST http://localhost:8080/api/users/

payload {"name": "myname"}


3. Display all the followers for a given user

GET  http://localhost:8080/api/users/1/relations/


4. Follow a friend 

POST http://localhost:8080/api/relations/

payload {"follower_id":1, "following_id": 5}

User id 1 follow a friend with id 5


5. Unfollow the specific friend for a given user

DELETE  http://localhost:8080/api/users/1/relations/?following_id=4

User 1 unfollow the friend with id 4




