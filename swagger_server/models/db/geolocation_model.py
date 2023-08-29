from swagger_server.resources.db import db


class Geolocation(db.Model):
    __tablename__ = "geolocation_logs"
    id_geolocation_log = db.Column(db.Integer, primary_key=True)
    code_email = db.Column(db.String(100), db.ForeignKey("users.code_email"))
    id_prospect = db.Column(db.Integer, db.ForeignKey("prospect.id"))
    ip = db.Column(db.String(30))
    latitude = db.Column(db.Float)  # Campo para guardar la latitud
    longitude = db.Column(db.Float)  # Campo para guardar la longitud
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def __init__(self, payload):
        self.id_prospect = payload.get("id_prospect")
        self.code_email = payload.get("code_email")
        self.ip = payload.get("ip")
        self.latitude = payload.get("latitude")
        self.longitude = payload.get("longitude")

    def to_json(self):
        return {
            "id_geolocation_log": self.id_geolocation_log,
            "code_email": self.code_email,
            "id_prospect": self.id_prospect,
            "ip": self.ip,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "created_at": self.created_at,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()
