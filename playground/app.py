from flask import Flask, render_template

app = Flask (__name__)

@app.route('/') 
def index():
    return render_template('helloWorld.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/dynamic')
def dynamic():
    greeting = "Welcome"
    name = "Megatron"
    decepticons = ["Megatron", "Starscream", "Soundwave", "Shockwave", "Jetfire"]
    return render_template('dynamic.html', greeting=greeting, name=name, decepticons=decepticons)


if __name__ == '__main__':
     app.run(debug=True, host= '0.0.0.0')