from flask import Blueprint

coins_bp = Blueprint('coins', __name__)

@coins_bp.route('/coins/test')
def coins_test():
    return "Coins route is working."

