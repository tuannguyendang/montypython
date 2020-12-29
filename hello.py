from flask import Flask, url_for, request, jsonify
from markupsafe import escape

app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return 'Hello, World!'


@app.route('/')
def index():
    return 'Index Page'


@app.route('/user/<user_name>')
def get_user(user_name):
    return 'User %s' % escape(user_name)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id


@app.route('/money/<float:money_amount>')
def cal_money(money_amount):
    return 'Money %f' % money_amount


@app.route('/path/<path:sub_path>')
def sub_path(sub_path):
    return 'Path %s' % escape(sub_path)


@app.route('/find/<uuid:index_id>')
def find_index(index_id):
    return "Index %s" % escape(index_id)


@app.route('/project/')
def project_page():
    return 'Project Page'


@app.route('/about')
def about_page():
    return 'About Page'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return 'GET Login'
    else:
        return 'POST Login'


@app.route('/api')
def api():
    response = {
        "message": "hi hi",
        "image" : "http://dbc.png"
    }
    return jsonify(response)


USERS = [{
    'name': 'tuan nguyen',
    'age': 28,
    'address': 'nguyen duy trinh'
},{
    'name': 'hoang nguyen',
    'age': 4,
    'address': 'nguyen duy trinh'
}]


@app.route('/user/<int:index>')
def get_user_by_index(index):
    try:
        return USERS[index]
    except IndexError as e:
        print(e)
        return jsonify({'error': 'index not found'})


with app.test_request_context():
    print(url_for('login'))
    print(url_for('index'))
    print(url_for('login', next='/'))
    # print(url_for('profile', username='John Doe'))


# if __name__ == '__main__':
#     app.run()
