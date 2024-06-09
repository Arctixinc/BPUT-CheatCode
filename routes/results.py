from flask import jsonify, Blueprint, request, render_template
from .all_fun import *

results = Blueprint('results', __name__)

BASE_URL = "https://results.bput.ac.in"

@results.route('/results', methods=['GET'])
def get_results():
    roll_no = request.args.get('rollno')
    sem_id = request.args.get('semid', default='4')
    session = request.args.get('session', default='E24')

    if not roll_no:
        return jsonify({"error": "rollno query parameter is required"}), 400

    session = map_session_code(session)
    params = {
        "rollNo": roll_no,
        "semid": sem_id,
        "session": session
    }
    url = f"{BASE_URL}/student-results-subjects-list"
    return make_request(url, params, method='POST')

