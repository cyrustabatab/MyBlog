from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    url="https://api.npoint.io/5abcca6f4e39b4955965"
    response = requests.get(url)
    posts = response.json()
    return render_template("index.html",posts=posts)


@app.route('/post/<int:blog_id>')
def get_blog_post(blog_id):

    url = "https://api.npoint.io/5abcca6f4e39b4955965"
    response = requests.get(url)
    posts = response.json()
    for post in posts:
        if post["id"] == blog_id:
            break
    return render_template("post.html",post=post)

if __name__ == "__main__":
    app.run(debug=True)
