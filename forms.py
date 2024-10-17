from wtforms import BooleanField, StringField, PasswordField, validators
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import Form, SelectField, SubmitField

# Without any configuration, the FlaskForm will be a session secure form with csrf protection. We encourage you not to change this.
#
# But if you want to disable the csrf protection, you can pass:
#
# form = FlaskForm(meta={'csrf': False})

#
# The FileField provided by Flask-WTF differs from the WTForms-provided field.
# It will check that the file is a non-empty instance of FileStorage, otherwise data will be None.
#
#


class ItemForm(FlaskForm):
    name = StringField('Name', [validators.Length(min=4, max=25)])
    hobby = SelectField('Choose the hobby type',
        choices=[ ('', ''), ('singing', 'singing'), ('dancing', 'dancing'), ('swimming', 'swimming'),
        ('painting', 'painting')])
    color = SelectField('Choose the favorite color',
        choices=[ ('', ''), ('red', 'red'), ('green', 'green'), ('blue', 'blue'),
        ('yellow', 'yellow')])
    photo = FileField('Best Image', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
    submit=SubmitField(label='Submit information')
