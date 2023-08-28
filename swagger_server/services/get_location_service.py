from swagger_server.services.base_service import BaseService


class GetLocationService(BaseService):

    def get_location_service(self, internal_transaction_id, external_transaction_id):
        try:
            response = self.service_client.geolocate()
            #data = response.get("location")
            return response
        except Exception as ex:
            error = self.error_message_format(ex)
            self.log.critical(self.msg_log, internal_transaction_id, external_transaction_id, "get_location", __name__, error)
            return None