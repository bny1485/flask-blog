from flask import Flask, render_template, url_for, flash, redirect
from forms import RegisterationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'fb29cf854cc3642cc510c2f7f7284ba6 '


posts = [
    {
        'author': 'Benyamin Mahmoudyan',
        'title': 'Blog post 1',
        'content':'fist content',
        'date_posted': 'April 20, 2020',
    },
    {
        'author': 'Benyamin Mahmoudyan',
        'title': 'Blog post 2',
        'content':'2nd content',
        'date_posted': 'March 20, 2020',
    },
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
        # url_for get function name
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@glog.com' and form.password.data == 'password':
            flash(f'you haved be loged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'login unsuccessful. please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)