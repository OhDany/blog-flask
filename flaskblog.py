from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Dany Ortega',
        'title': 'My first post in the blog',
        'content': 'My first post content in the news',
        'date_posted': 'April 20, 2020'
    },
    {
        'author': 'Joe Ortega',
        'title': 'My second post in the blog',
        'content': 'My second post content in the news',
        'date_posted': 'April 21, 2020'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)