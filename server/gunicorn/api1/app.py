from flask import Flask, render_template, requests
#from flask_restful import Resource, Api
from markupsafe import escape

app = Flask(__name__, static_url_path='')
#api = Api(app)

#class HelloWorld(Resource):
#    def get(self):
#        return {'hello': 'world'}

#api.add_resource(HelloWorld, '/')
@app.route('/index')
def index():
    return app.send_static_file('index.html')

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'do the login'
    else:
        return 'show the form'

if __name__ == '__main__':
    app.run(debug=True)
