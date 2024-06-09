from flask import jsonify, request, render_template
import requests

BASE_URL = "https://results.bput.ac.in"

def make_request(url, params, method='POST'):
    try:
        if method == 'POST':
            response = requests.post(url, data=params)
        else:
            response = requests.get(url, params=params)
        
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Failed to retrieve data: {str(e)}"}), 500

def map_session_code(session_code):
    session_mapping = {
        "E24": "Even (2023-24)",
        "O24": "Odd (2023-24)"
    }
    return session_mapping.get(session_code, session_code)

def register_routes(app):
    @app.route('/details', methods=['GET'])
    def get_details():
        roll_no = request.args.get('rollno')
        if not roll_no:
            return jsonify({"error": "rollno query parameter is required"}), 400

        params = {"rollNo": roll_no}
        url = f"{BASE_URL}/student-detsils-results"
        return make_request(url, params)

    @app.route('/results', methods=['GET'])
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

    @app.route('/examinfo', methods=['GET'])
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

    @app.route('/sgpa', methods=['GET'])
    def get_sgpa():
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
        url = f"{BASE_URL}/student-results-sgpa"
        return make_request(url, params, method='POST')
    @app.route('/')
    def home():
        return render_template('index.html')