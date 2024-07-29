# Picture Gallery

## Install and run the project

To run the project first you have to set up your database credentials in a .env file. An example of a .env file would be:

```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
POSTGRES_DB=database
DATABASE_URL=postgresql+psycopg2://postgres:password@db:5432/database
```

Then you can use docker with:

```sh
docker-compose up --build
```

### Try the project

The API consists of two main endpoints:

#### User endpoint

The prefix is `api/user`, and the available methods are:

- POST `/register`: Receives a user data and insert it into the database.
- DELETE `/delete/<user_id>`: Receives a user id and deletes it from the database
- GET `/`: Returns all users registered
- POST `/login`: Receives an username and a password and if correct, returns user information.
- GET `/<username.>`: Receives an user username and retrieves the data from that user.

I leave examples to test this endpoint with curl:

- register:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"email": "email@example.com","username": "user1", "password": "pass"}' http://localhost:5000/api/user/register
```

- login:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"username": "user1", "password": "pass"}' http://localhost:5000/api/user/login
```

- delete a user:

```bash
curl -X DELETE http://localhost:5000/api/user/delete/1
```

- get a user:

```bash
curl -X GET http://localhost:5000/api/user/user1
```

- get all users:

```bash
curl -X GET http://localhost:5000/api/user/
```

#### Picture endpoint

The prefix is `api/picture`, and the available methods are:

- `upload/<username.>`: Receives an username an new picture information, if correct adds it to the database.
- `/delete/<picture_id>`: Receives a picture id and a user id and delete the picture from the database.

I leave examples to test this endpoint with curl:

- upload a picture

```bash
curl -X POST -F "picture=@path_to_picture.jpg" http://localhost:5000/api/picture/upload/user1
```

- delete a picture

```bash
curl -X DELETE http://localhost:5000/api/picture/delete/picture_id
```
