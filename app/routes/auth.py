from flask import Blueprint, request, jsonify, render_template
from werkzeug.utils import secure_filename
from app.models import User
from app import db
import os

auth_bp = Blueprint('auth', __name__)

UPLOAD_FOLDER = 'app/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Show HTML form
@auth_bp.route('/auth/register', methods=['GET'])
def show_register_form():
    return render_template('register.html')

# Handle form submission
@auth_bp.route('/auth/register', methods=['POST'])
def register():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    role = request.form.get('role')
    files = request.files

    # Check if username/email exists
    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username already taken"}), 400
    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Email already registered"}), 400

    # Check uploaded files
    id_file = files.get('id_document')
    bank_file = files.get('bank_statement')

    if not (id_file and bank_file):
        return jsonify({"error": "ID document and bank statement required"}), 400

    if not (allowed_file(id_file.filename) and allowed_file(bank_file.filename)):
        return jsonify({"error": "Invalid file type"}), 400

    # Save files securely
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    id_filename = secure_filename(f"{username}_id_{id_file.filename}")
    bank_filename = secure_filename(f"{username}_bank_{bank_file.filename}")

    id_file.save(os.path.join(UPLOAD_FOLDER, id_filename))
    bank_file.save(os.path.join(UPLOAD_FOLDER, bank_filename))

    # Create user
    user = User(
        username=username,
        email=email,
        role=role,
        id_document=os.path.join(UPLOAD_FOLDER, id_filename),
        bank_statement=os.path.join(UPLOAD_FOLDER, bank_filename)
    )
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "Registration successful, pending approval"}), 201

