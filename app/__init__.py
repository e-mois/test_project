from flask import Flask
from app.get_list_posts import make_list_post

app = Flask(__name__)

@app.route('/')
def hello_world():
    list_posts = make_list_post('app/post.json', 'app/comments.json')
    return list_posts


if __name__ == "__main__":
    app.run()