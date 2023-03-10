from flask import Blueprint, url_for, render_template, flash, request, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from ApplePie import db
from ApplePie.forms import UserCreateForm, UserLoginForm
from ApplePie.models import User

bp = Blueprint('model', __name__, url_prefix='/model')

@bp.route('/service/', methods=('GET', 'POST'))
def service():
    if request.method == 'POST' :
        from ..AI_Model import tesseract
    return render_template('model/model.html')