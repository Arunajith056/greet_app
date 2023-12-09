from flask import Flask, flash, render_template, request, redirect, url_for

app = Flask(__name__)
app.secret_key = 'aghhas-sjhjs-aaa'


@app.route('/')
def home():
    flash("What is your name?")
    return render_template('index.html')

@app.route('/greet', methods=['GET','POST'])
def greet():
    name = request.form.get('name')
    flash("Hi "+ str(name) + ", great to see you!")
    return render_template('index.html')




if __name__ == '__main__':
    app.run(debug=True)