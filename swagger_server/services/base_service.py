import googlemaps
from swagger_server.config.access import access


class BaseService:

    def __init__(self):
        self.service_key = access()["KEY_API_GOOGLE_MAPS"]
        self.service_client = googlemaps.Client(key=self.service_key)
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '

    def error_message_format(self, ex):
        return "Error durante la consulta: {}".format(ex)