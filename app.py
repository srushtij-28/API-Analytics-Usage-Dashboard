from flask import Flask, request, jsonify
from models import db, ApiLog

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = \
    "sqlite:///analytics.db"

db.init_app(app)

with app.app_context():
    db.create_all()


@app.after_request
def log_request(response):

    log = ApiLog(
        endpoint=request.path,
        method=request.method,
        status_code=response.status_code
    )

    db.session.add(log)
    db.session.commit()

    return response


@app.route("/")
def home():

    return jsonify({
        "message": "API Analytics Demo"
    })


@app.route("/dashboard")
def dashboard():

    total = ApiLog.query.count()

    errors = ApiLog.query.filter(
        ApiLog.status_code >= 400
    ).count()

    return jsonify({
        "total_requests": total,
        "total_errors": errors
    })


@app.route("/health")
def health():

    return jsonify({
        "status": "healthy"
    })


if __name__ == "__main__":
    app.run(debug=True)
