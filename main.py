from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', page='home')

@app.route('/crocheting')
def crocheting():
    return render_template('index.html', page='crocheting')

@app.route('/swimming')
def swimming():
    return render_template('index.html', page='swimming')

@app.route('/about')
def about():
    return render_template('index.html', page='about')

if __name__ == '__main__':
    app.run(debug=True)