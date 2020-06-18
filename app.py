from flask import Flask, render_template, redirect, request, url_for
from pymongo import MongoClient
from datetime import datetime

url = "mongodb+srv://1a-alo:HbzqniuBBgqvgz6j@comments-fbgkx.mongodb.net/comments?retryWrites=true&w=majority"
dbname = 'comments'

client = pymongo.MongoClient(url)
db = client[dbname]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/article/<id>')
def article(id):
    comments = db.comments.find({ 'article_id': id})
    return render_template('article.html', comments=comments, id=id)

@app.route('/add/<id>', methods=['POST'])
def add(id):
    author = request.form['author']
    content = request.form['content']
    created_at = datetime.now()
    if content and author:
        db.comments.insert_one({'content': content, 'author': author, 'article_id': id, 'created_at': created_at})
    return redirect(url_for('article', id=id))

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')












# from flask import Flask, render_template, request, redirect, flash

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('home.html')


# def pr():
#     print('123asdasdWEF')

# @app.route('/signup', methods=['POST'])
# def signup():
#     name = request.form['name']
#     print(request.form['email'])
#     message="Cześć, " + name + "fajnie, że zapisałeś się do nas."
#     return render_template('home.html', message=message )



# if __name__ == '__main__':
#     app.run(debug=True)
