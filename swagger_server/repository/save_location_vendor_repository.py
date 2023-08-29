from swagger_server.repository.base_repository import BaseRepository
from swagger_server.models.db.geolocation_model import Geolocation


class SaveLocationVendorRepository(BaseRepository):

    def save_location(self, data: dict, internal_transaction_id: str, external_transaction_id: str):
        try:
            location_log = Geolocation(data.to_dict())
            location_log.save()
            return location_log
        except Exception as ex:
            error = self.error_message_format(ex)
            self.log.critical(self.msg_log,internal_transaction_id, external_transaction_id, "save_location", __name__, error)
            return {"message": error, "code": 1}