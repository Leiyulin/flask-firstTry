from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.script import Manager


app=Flask(__name__)
manager=Manager(app)
bootstrap=Bootstrap(app)

@app.route('/')
def index():
	return render_template('homepage.html')
#	return '<h1>hahaha</h1>'
if __name__=='__main__':
	manager.run()

