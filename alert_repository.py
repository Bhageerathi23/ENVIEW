class AlertRepository:
    def __init__(self):
        self.alerts = []

    def save_alert(self, alert):
        self.alerts.append(alert)

    def get_alert_by_id(self, alert_id):
        for alert in self.alerts:
            if alert.alert_id == alert_id:
                return alert
        return None
