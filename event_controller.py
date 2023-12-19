from flask import Flask, request, jsonify
from app.services.rule_engine import RuleEngine

app = Flask(__name__)
rule_engine = RuleEngine()

@app.route('/event', methods=['POST'])
def handle_event():
    data = request.get_json()
    rule_engine.process_event(data)
    return jsonify({"message": "Event processed successfully"}), 200
