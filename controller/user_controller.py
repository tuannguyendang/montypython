import sys

from flask import Flask, jsonify, request, url_for
from slugify import slugify

from entity import User, db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../resources/user.db"
db.init_app(app)


@app.route('/<name>')
def get_user(name):
    user = User.query.filter(User.name == name).first_or_404()
    output = {
        'name': user.name,
        'address': user.address,
        'image_url': user.image_url
    }

    return jsonify(output)


@app.route('/', methods=['POST'])
def create_user():
    name = request.form.get('name')
    if not name:
        return 'name required', 400
    image_url = request.form.get('image_url')
    if not image_url:
        return 'image url required', 400
    address = request.form.get('address')

    slug = slugify(name)
    print(slug)

    user = User(name=name, image_url=image_url, address=address)
    db.session.add(user)
    db.session.commit()

    location = url_for("get_user", name=name)
    resp = jsonify({'message': 'created'})
    resp.status_code = 201
    resp.headers['location'] = location

    return resp


if __name__ == "__main__":
    if "createdb" in sys.argv:
        with app.app_context():
            db.create_all()
        print("Database created!")

    elif "seeddb" in sys.argv:
        with app.app_context():
            p1 = User(address="205 nguyen duy trinh", name="hoang",
                      image_url="http://example.com/rover.jpg")
            db.session.add(p1)
            p2 = User(address="truong quang trach", name="tuan",
                      image_url="http://example.com/spot.jpg")
            db.session.add(p2)
            db.session.commit()
        print("Database seeded!")

    else:
        app.run(debug=True)
