from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.script import Manager
from flask.ext.moment import Moment
from datetime import datetime

app=Flask(__name__)
manager=Manager(app)
bootstrap=Bootstrap(app)
moment=Moment(app)

@app.route('/')
def index():
	return render_template('base.html', current_time=datetime.utcnow())
#	return '<h1>hahaha</h1>'

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'),500

if __name__=='__main__':
	manager.run()

