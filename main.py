from flask import Flask ,redirect,render_template,request,url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename
import os
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from flask import Flask, flash, request, redirect, url_for
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField
from forms import *
import numpy as np

basedir = os.path.abspath(os.path.dirname(__file__))

import secrets
SECRET_KEY = secrets.token_hex()

context = {"message": None, "name": None, "hobby": None, "color": None, "filename": None}

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000
app.config['UPLOADS'] = os.path.join(basedir, 'uploads') # you'll need to create a folder named uploads




def lucky_name(name):
    lucky = False
    name = name.capitalize()
    All_alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    All_alphabets = np.array(list(All_alphabets))
    chosen = np.random.choice(All_alphabets, 13)
    lucky_initial = chosen
    for i in lucky_initial:
        if name.startswith(i):
            lucky = True
    return lucky



# Logic to decide which template file to call based on 'name' variable
# The 'team' variable will be passed to the appropriate view function
# url_for method here calls the appropriate view function and
# passes the parameter required


@app.route('/', methods=['POST', 'GET'])
def home_page():
    form = ItemForm()
    if form.validate_on_submit():
        name = request.form['name']
        name = name.strip()
        name1 = name.replace(" ", "")
        lucky = lucky_name(name)
        hobby = request.form['hobby']
        color = request.form['color']
        f = form.photo.data
        filename = secure_filename(f.filename)
        # filename = photos.save(form.photo.data)

        # filename1 = secure_filename(file.filename)
        path_file = os.path.join(app.config['UPLOADS'], filename)
        f.save(path_file)
        message = flash(f"The data for user {name} has been submitted.")
        context["message"] = message
        context["name"] = name
        context["hobby"] = hobby
        context["color"] = color,
        context["filename"] = filename
        if lucky:
            return redirect(url_for('lucky_last', name1 = name1))
        return redirect(url_for('just_last', name1 = name1))
    return render_template('home.html', form= form)



@app.route('/Lucky/<name1>', methods=['POST', 'GET'])
def lucky_last(name1):
    lucky = True
    return render_template('lucky.html', context = context, lucky = lucky, name1 = name1)



@app.route('/just_normal/<name1>', methods=['POST', 'GET'])
def just_last(name1):
    lucky = False
    return render_template('lucky.html', context = context, lucky = lucky, name1 = name1)



@app.route('/uploads/<filename>')
def send_uploaded_file(filename=''):
    from flask import send_from_directory
    return send_from_directory(app.config["UPLOADS"], filename)


if __name__ == "__main__":
    app.run(debug=True)
