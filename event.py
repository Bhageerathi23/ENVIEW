class Event:
    def __init__(self, timestamp, is_driving_safe, vehicle_id, location_type):
        self.timestamp = timestamp
        self.is_driving_safe = is_driving_safe
        self.vehicle_id = vehicle_id
        self.location_type = location_type
