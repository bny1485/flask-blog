from flask import Flask, render_template, url_for

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)