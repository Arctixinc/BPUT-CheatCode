from flask import jsonify, Blueprint, request
from .all_fun import map_session_code

results = Blueprint('results', __name__)

BASE_URL = "https://results.bput.ac.in"

import requests

def make_request(url, params=None, method='GET'):
    try:
        if method == 'GET':
            response = requests.get(url, params=params)
        elif method == 'POST':
            response = requests.post(url, data=params)
        else:
            return {"error": f"Unsupported method: {method}"}

        response.raise_for_status()  # Raise an exception for HTTP errors (status codes >= 400)

        # Extract and return JSON data from the response
        return response.json()
    except requests.RequestException as e:
        # Handle request exceptions (e.g., connection errors, timeouts)
        raise Exception(f"Request failed: {e}")


@results.route('/results', methods=['GET'])
def get_results():
    roll_no = request.args.get('rollno')
    sem_id = request.args.get('semid', default='4')
    session = request.args.get('session', default='E24')
    html_output = 'html' in request.args  # Check if 'html' parameter is present

    if not roll_no:
        return jsonify({"error": "rollno query parameter is required"}), 400

    if html_output:
        session = map_session_code(session)
        if session is None:
            return jsonify({"error": "Invalid session code"}), 400

        params = {
            "rollNo": roll_no,
            "semid": sem_id,
            "session": session
        }
        url = f"{BASE_URL}/student-results-subjects-list"

        try:
            response = make_request(url, params, method='POST')
            return convert_to_html(response), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        # Return JSON response as before
        session = map_session_code(session)
        params = {
            "rollNo": roll_no,
            "semid": sem_id,
            "session": session
        }
        url = f"{BASE_URL}/student-results-subjects-list"
        try:
            response = make_request(url, params, method='POST')
            return jsonify(response), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

def convert_to_html(response_data):
    # Assuming your response_data structure is similar to the JSON response in your previous code
    html = """
    <html>
    <head>
        <title>Student Results</title>
        

 <style>
    body {
        font-family: Arial, sans-serif;
        background-color: #f2f2f2;
        margin: 0;
        padding: 0;
    }

    .container {
        max-width: 800px;
        margin: 20px auto;
        padding: 20px;
        background-color: #fff;
        border-radius: 8px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }

    table {
        width: 100%;
        border-collapse: collapse;
    }

    th, td {
        padding: 12px 15px;
        text-align: left;
        border-bottom: 1px solid #ddd;
    }

    th {
        background-color: #4CAF50;
        color: white;
        text-transform: uppercase;
    }

    tr:nth-child(even) {
        background-color: #f2f2f2;
    }

    tr:hover {
        background-color: #ddd;
    }
</style>
    </head>
    <body>
    <table>
        <tr>
            <th>S.No</th>
            <th>Subject Code</th>
            <th>Subject Name</th>
            <th>Type</th>
            <th>Credits</th>
            <th>Final Grade</th>
        </tr>
    """

    # Add table rows
    for i, result in enumerate(response_data, start=1):
        html += f"""
        <tr>
            <td>{i}</td>
            <td>{result['subjectCODE']}</td>
            <td>{result['subjectName']}</td>
            <td>{result['subjectTP']}</td>
            <td>{result['subjectCredits']}</td>
            <td>{result['grade']}</td>
        </tr>
        """

    # Close the table and HTML
    html += """
    </table>
    </body>
    </html>
    """

    return html
