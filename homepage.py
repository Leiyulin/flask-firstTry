from flask import Flask, render_template, session, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_script import Manager
from flask_moment import Moment
from datetime import datetime
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class NameForm(Form):
	name = StringField('What is your name?', validators = [Required()])
	submit = SubmitField('Submit')
	
app=Flask(__name__)
manager=Manager(app)
bootstrap=Bootstrap(app)
moment=Moment(app)
app.config['SECRET_KEY'] = '12345'
@app.route('/', methods = ['GET', 'POST'])
def index():
	form = NameForm()
	if form.validate_on_submit():
		session['name'] = form.name.data
		return redirect(url_for('index'))
	return render_template('base.html', current_time=datetime.utcnow(), form = form, name = session.get('name'))
#	return '<h1>hahaha</h1>'

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'),500

if __name__=='__main__':
	manager.run()

