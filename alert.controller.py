from flask import Flask, jsonify
from app.services.rule_engine import RuleEngine

app = Flask(__name__)
rule_engine = RuleEngine()

@app.route('/alert/<int:alert_id>', methods=['GET'])
def get_alert(alert_id):
    alert = rule_engine.get_alert(alert_id)
    return jsonify(alert.serialize()), 200 if alert else 404
