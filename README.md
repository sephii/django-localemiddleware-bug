This is a simple project to reproduce the bug reported here:

https://code.djangoproject.com/ticket/35170

To reproduce the bug:

- Install Django the way you prefer
- Run the server (python ./manage.py runserver)
- Visit http://localhost:8000/
- You’ll be redirected to http://localhost:8000/en/foobar/ which should show
"Messages: Hello world" (it shows "Messages:" instead)

That’s because the messages are surprisingly consumed by the 404.html template.
See the bug report for more information.
