from flask import Flask
from routes.home import home_bp
from routes.details import details
from routes.examinfo import examinfo
from routes.results import results
from routes.sgpa import sgpa


app = Flask(__name__)

# Register route blueprints here
app.register_blueprint(home_bp)
app.register_blueprint(details)
app.register_blueprint(examinfo)
app.register_blueprint(results)
app.register_blueprint(sgpa)

if __name__ == '__main__':
    app.run(debug=True)
    
