from flask import Flask, render_template, url_for, flash, redirect

from form import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '3ec21fa6f45f386a0180d36049499bd7'

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


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unseccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)