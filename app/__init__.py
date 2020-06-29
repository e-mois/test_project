from flask import Flask, abort
from app.get_list_posts import make_list_post, make_list_comments

app = Flask(__name__)

@app.route('/')
def index():
    list_posts = make_list_post('app/post.json', 'app/comments.json')
    return {'posts': list_posts['posts'], 'posts_count': list_posts['posts_count']}


@app.route('/post/<int:post_id>')
def get_post(post_id):
    list_comments = make_list_comments('app/post.json', 'app/comments.json', post_id)
    if list_comments:
        return list_comments
    else:
        abort(404, description="Resource not found")

if __name__ == "__main__":
    app.run()