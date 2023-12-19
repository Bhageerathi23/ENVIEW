from flask import Flask

from app.controllers import event_controller, alert_controller
from app.repositories import event_repository, alert_repository, location_type_repository
from app.services import rule_engine

app = Flask(__name__)

if __name__ == '__main__':
    app.run()
