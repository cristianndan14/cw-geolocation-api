from swagger_server.services.base_service import BaseService


class RevGeocodeService(BaseService):
    
    def get_rev_geocoding(self, lat: float, lng: float, internal_transaction_id, external_transaction_id):
        try:
            response = self.service_client.reverse_geocode((lat, lng))
            return response
        except Exception as ex:
            error = self.error_message_format(ex)
            self.log.critical(self.msg_log, internal_transaction_id, external_transaction_id, "get_rev_geocoding", __name__, error)
            return None