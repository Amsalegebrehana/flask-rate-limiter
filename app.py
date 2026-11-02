from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/health-check', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200


@app.route('/api/resource', methods=['GET'])
def get_resource():
    return jsonify({"message": "Resource accessed successfully"}), 200

