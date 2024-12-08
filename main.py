from flask import Flask, render_template, request, session, redirect, url_for, flash



app = Flask(__name__)
app.secret_key = '1KMsm112KMI8Fd45v8bvr56878mnc5XXZcV8878'


@app.route('/')
def index():
    name = 'Роджер'
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)  
