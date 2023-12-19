from flask import Flask, request, jsonify
from datetime import datetime, timedelta
import uuid

app = Flask(__name__)

# In-memory storage for events and alerts
events = []
alerts = []
location_thresholds = {
    'highway': 4,
    'city_center': 3,
    'commercial': 2,
    'residential': 1
}

def process_rule(events):
    # Process the rule based on events within the last 5 minutes
    current_time = datetime.utcnow()
    recent_events = [event for event in events if current_time - event['timestamp'] <= timedelta(minutes=5)]
    
    for location_type in location_thresholds:
        threshold = location_thresholds[location_type]
        filtered_events = [event for event in recent_events if event['location_type'] == location_type and not event.get('alert_generated')]
        
        if len(filtered_events) >= threshold:
            # Generate alert
            alert = {
                'alert_id': str(uuid.uuid4()),
                'location_type': location_type,
                'timestamp': current_time.isoformat(),
                'events': filtered_events
            }
            alerts.append(alert)
            
            # Mark events as alert generated
            for event in filtered_events:
                event['alert_generated'] = True

@app.route('/event', methods=['POST'])
def receive_event():
    data = request.get_json()
    events.append(data)
    process_rule(events)
    return jsonify({'message': 'Event received and processed successfully'}), 200

@app.route('/alert/<alert_id>', methods=['GET'])
def get_alert(alert_id):
    alert = next((alert for alert in alerts if alert['alert_id'] == alert_id), None)
    if alert:
        return jsonify(alert)
    return jsonify({'message': 'Alert not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
