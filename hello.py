from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms import validators
from wtforms.fields.html5 import EmailField


class NameForm(Form):
	name = StringField('What is your name?', validators=[DataRequired()])    
	email = EmailField('What is your UofT email address?', [validators.DataRequired(), validators.Email()])
	submit = SubmitField('Submit')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
moment = Moment(app)
Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
	name = None
	email = None    
	form = NameForm()
	if form.validate_on_submit():
		name = form.name.data
		email = form.email.data
		form.name.data = ''
	return render_template('index.html', form=form, name=name, email=email)

@app.route('/user/<name>')
def user(name):
	return render_template('user.html', name=name)

if __name__ == '__main__':
	app.run(debug=True)

