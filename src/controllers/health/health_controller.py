# Health endpoint with JSON response for Tusk Drift setup. Remove this endpoint if not needed (and update ./.tusk/config.yaml accordingly).
from flask import jsonify
from src import app

@app.route('/health', methods=['GET'])
def health_check():
    """Simple health check endpoint that returns JSON"""
    return jsonify({"status": "ok", "service": "2ndcareers-api"}), 200
