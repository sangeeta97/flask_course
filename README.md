# webapp
Lucky web app with random sampling of first letter of name to determine whether name is lucky or not.
It has 2 script files.

Each file uses flask microframework to create instances to be used in the app.


# main.py
The entry point file, which will create the app instance for flask. This Flask class has (methods, attributes) all the functionalities.
The flask object created with Flask class implements a WSGI application and acts as the central object. 
The Flask class takes the name of the module or package of the application. 
Once it is created it will act as a central registry for the view functions, the URL rules, template configuration and much more.


# forms.py

* The Flask-WTF extension expands on this pattern and adds a few little helpers that make working with forms and Flask more fun.
* It defines a form class with different attributes and their validators.



# templates

* it is front view with rendered instructions.
* import css file and inherite from the base template
* connects to three views and has two html pages


