# POMODORO

This is a podomodoro timer created using Flask-RESTful. To run the app, you will need to:

1. Create a venv folder:

```
$ python3 -m venv venv
```

2. Activate venv:

```
$ source venv/bin/activate
```

3. Install dependencies:

```
$ pip install -r requirements.txt
```

4. Run the app:

```
$ ./db_creation.sh
$ ./db_migration.sh
$ ./start_api.sh
```

To try the api, you can use Postman with the following endpoints:

1. GET:
   http://127.0.0.1:5000/config

2. POST:
   http://127.0.0.1:5000/config

Body example:

{
"pomodoro":1501,
"short_break":150,
"long_break": 333
}

3. POST:
   http://127.0.0.1:5000/task

Body example:

{
"name": "task 1",
"description": "do many things",
"state": "ongoing"
}

4. GET:
   http://127.0.0.1:5000/task

5. GET:
   http://127.0.0.1:5000/task/<task_id>
