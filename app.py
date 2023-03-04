from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
	return render_template('homepage.html')

@app.route('/homepage.html')
def home():
	return render_template('homepage.html')

@app.route('/dragon.html')
def dragon():
	return render_template('dragon.html')

@app.route('/keter.html')
def keter():
	return render_template('keter.html')

@app.route('/darkstates.html')
def darkstates():
	return render_template('darkstates.html')

@app.route('/brandtgate.html')
def brandtgate():
	return render_template('brandtgate.html')

@app.route('/stoichiea.html')
def stoichiea():
	return render_template('stoichiea.html')

if __name__=='__main__':
	app.run(debug=True, host='0.0.0.0')


