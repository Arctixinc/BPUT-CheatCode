from flask import jsonify, Blueprint, request, render_template
from .all_fun import *

details = Blueprint('details', __name__)

BASE_URL = "https://results.bput.ac.in"

@details.route('/details', methods=['GET'])
def get_details():
    roll_no = request.args.get('rollno')
    if not roll_no:
        return jsonify({"error": "rollno query parameter is required"}), 400

    params = {"rollNo": roll_no}
    url = f"{BASE_URL}/student-detsils-results"
    return make_request(url, params)
