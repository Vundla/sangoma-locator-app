from flask import Blueprint

ai_bp = Blueprint('ai', __name__)

@ai_bp.route('/ai/test')
def ai_test():
    return "AI route is working."

