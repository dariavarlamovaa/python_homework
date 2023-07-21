from flask import Flask, render_template, request

app = Flask(__name__)

menu = [
    {'name': 'Home', 'url': '/'},
    {'name': 'About', 'url': 'about'},
    {'name': 'Contact me', 'url': 'contacts'},
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home', menu=menu)


@app.route('/about')
def about():
    return render_template('about.html', title='About me', menu=menu)


@app.route('/contacts', methods=['GET', 'POST'])
def contacts():
    if request.method == "POST":
        return render_template('home.html', title='Home', menu=menu)
    return render_template('contacts.html', title='Contact me', menu=menu)


if __name__ == '__main__':
    app.run(debug=True)

