from flask import Flask, render_template, url_for
app = Flask(__name__, template_folder="template")

posts = [
    {
     'author':'Tanu',
     'title':'Blog Post',
     'content':'Posted checking',
     'date_posted': 'April20,2020'
     },
    {
     'author':'Bineeta',
     'title':'Blog Posting Second',
     'content':'Post checking!',
     'date_posted': 'April20,2022'
     } 
    ]
@app.route('/')
@app.route('/home') 
def homee():
    return render_template('homee.html', posts=posts) 

@app.route('/about') 
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug = False) 

