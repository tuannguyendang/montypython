from flask import Flask, jsonify, url_for

app = Flask(__name__)


@app.route('/v1/api')
class ApiController(object):
    USERS = [{
        'name': 'tuan nguyen',
        'address': 'nguyen duy trinh'
    },
        {
            'name': 'nguyen hoang',
            'address': 'usa'
        }]

    # def __init__(self):

    @app.route('/get_user/<int:index>')
    def get_user(self, index):
        return jsonify(self.USERS[index])

    with app.test_request_context():
        print(url_for('get_user', index=1))
        app.run(debug=True)
