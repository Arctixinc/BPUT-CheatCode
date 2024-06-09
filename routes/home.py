from flask import jsonify, Blueprint, request, render_template
from .all_fun import *

home_bp = Blueprint('home', __name__)



@home_bp.route('/')
def home():
    return render_template('index.html')