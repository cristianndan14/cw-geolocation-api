from swagger_server.resources.db import db


class Prospect(db.Model):
    __tablename__ = 'prospect'
    id = db.Column(db.Integer, primary_key=True)
    action = db.Column(db.String(100))
    address = db.Column(db.String(100))
    city = db.Column(db.String(100))
    contact_channel = db.Column(db.String(100))
    dni = db.Column(db.String(100))
    email = db.Column(db.String(100))
    event = db.Column(db.String(100))
    interested_level = db.Column(db.Integer)
    lastname = db.Column(db.String(100))
    name = db.Column(db.String(100))
    not_contact_days = db.Column(db.Integer)
    phone = db.Column(db.String(100))
    plan = db.Column(db.String(100))
    prev_provider = db.Column(db.String(100))
    zone = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now())

    def __init__(self, payload):
        self.action = payload.get("action")
        self.address = payload.get("address")
        self.city = payload.get("city")
        self.contact_channel = payload.get("contact_channel")
        self.dni = payload.get("dni")
        self.email = payload.get("email")
        self.event = payload.get("event")
        self.interested_level = payload.get("interested_level")
        self.lastname = payload.get("lastname")
        self.name = payload.get("name")
        self.not_contact_days = 30
        self.phone = payload.get("phone")
        self.plan = payload.get("plan")
        self.prev_provider = payload.get("prev_provider")
        self.zone = payload.get("zone")

    def to_json(self):
        """
        It takes the object and returns a dictionary representation of it
        :return: A dictionary with the keys and values of the user object.
        """
        return {
            "id": self.id,
            "action": self.action,
            "address": self.address,
            "city": self.city,
            "contact_channel": self.contact_channel,
            "dni": self.dni,
            "email": self.email,
            "event": self.event,
            "interested_level": self.interested_level,
            "lastname": self.lastname,
            "name": self.name,
            "not_contact_days": self.not_contact_days,
            "phone": self.phone,
            "plan": self.plan,
            "prev_provider": self.prev_provider,
            "zone": self.zone,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    def save(self):
        """
        The save function is a method that is called on an instance of the User class.
        It adds the instance to the database and commits the changes
        """
        db.session.add(self)
        db.session.commit()

    def destroy(self):
        db.session.delete(self)
        db.session.commit()
