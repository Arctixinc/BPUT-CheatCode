from flask import jsonify, request, render_template
import requests

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
