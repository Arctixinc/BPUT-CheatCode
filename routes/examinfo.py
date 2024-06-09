from flask import jsonify, Blueprint, request, render_template
from .all_fun import *

examinfo = Blueprint('examinfo', __name__)

BASE_URL = "https://results.bput.ac.in"

@examinfo.route('/examinfo', methods=['GET'])
def get_exam_info():
    roll_no = request.args.get('rollno')
    dob = request.args.get('dob', default='2009-07-14')
    session = request.args.get('session', default='E24')

    if not roll_no:
        return jsonify({"error": "rollno query parameter is required"}), 400

    session = map_session_code(session)
    params = {
        "rollNo": roll_no,
        "dob": dob,
        "session": session
    }
    url = f"{BASE_URL}/student-results-list"
    return make_request(url, params, method='POST')
