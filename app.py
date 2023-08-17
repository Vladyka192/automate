from flask import Flask, request, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__, template_folder='F:/Programming/site/')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Article %r' % self.id
@app.route('/')
@app.route('/home')
def index():
    return "Hello World"


@app.route('/about')
def about():
    return "About page"

@app.route('/posts')
def posts():
    articles = Article.query.order_by(Article.date.desc()).all()
    return render_template("posts.html", articles = articles)

@app.route('/posts/<int:id>')
def post_detail(id):
    article = Article.query.get(id)
    return render_template("post-detail.html", article=article)

@app.route('/posts/<int:id>/del')
def post_delete(id):
    article = Article.query.get_or_404(id)

    try:
        db.session.delete(article)
        db.session.commit()
        return redirect("/posts")
    except:
        return "При удалении статьи произошла ошибка"
@app.route('/create-article', methods=['POST', 'GET'])
def create_article():
    if request.method == "POST":
        title = request.form['title']

        article = Article(title=title)

        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/create-article')
        except:
            return "При добавлении стаьи произошла ошибка"
    else:
        return render_template("create-article.html")
@app.route('/user/<string:name>/<int:id>')
def user(name,id):
    return "User page: " + name + " - " + str(id)
if __name__ == "__main__":
    app.run(debug=True)