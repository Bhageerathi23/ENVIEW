class Alert:
    def __init__(self, alert_id, timestamp, location_type):
        self.alert_id = alert_id
        self.timestamp = timestamp
        self.location_type = location_type

    def serialize(self):
        return {
            "alert_id": self.alert_id,
            "timestamp": self.timestamp,
            "location_type": self.location_type
        }
