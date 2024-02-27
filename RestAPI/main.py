from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
import uuid

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://marsellino.halim@bankmandiri.co.id:password@10.123.64.102:5432/dbname'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email_address = db.Column(db.String(500))

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(first_name=data['first_name'], last_name=data['last_name'], email_address=data['email_address'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'New user created!'}), 201

@app.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    output = []
    for user in users:
        user_data = {'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name, 'email_address': user.email_address}
        output.append(user_data)
    return jsonify({'users': output})

@app.route('/users/<id>', methods=['GET'])
def get_one_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({'message': 'No user found!'}), 404
    user_data = {'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name, 'email_address': user.email_address}
    return jsonify({'user': user_data})

if __name__ == '__main__':
    app.run(debug=True)