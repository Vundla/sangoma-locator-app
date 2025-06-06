from flask import Blueprint

call_bp = Blueprint('call', __name__)

@call_bp.route('/call/test')
def call_test():
    return "Call route is working."

