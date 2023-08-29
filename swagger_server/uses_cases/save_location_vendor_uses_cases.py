from swagger_server.models.request_save_location_vendor import RequestSaveLocationVendor
from swagger_server.models.response_save_location_vendor import ResponseSaveLocationVendor
from swagger_server.repository.save_location_vendor_repository import SaveLocationVendorRepository
from swagger_server.models.data_save_location_vendor import DataSaveLocationVendor
from swagger_server.utils.logs.logging import log as Logging


class SaveLocationVendorUseCase:

    def __init__(self, save_location_vendor_repository: SaveLocationVendorRepository, log: Logging):
        self.log = log
        self.save_location_vendor_repository = save_location_vendor_repository
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '

    def save_location_vendor(self, body: RequestSaveLocationVendor, internal_transaction_id: str):
        try:
            data_request = body.data
            
            location_log = self.save_location_vendor_repository.save_location(data_request, internal_transaction_id, body.external_transaction_id)
            
            response = ResponseSaveLocationVendor(
                code=0,
                message="Locacion del vendedor guardada exitosamente.",
                data=location_log.to_json(),
                internal_transaction_id=internal_transaction_id,
                external_transaction_id=body.external_transaction_id
            )
            return response
        except Exception as ex:
            response = ResponseSaveLocationVendor(
                code=1,
                message=str(ex),
                data=[],
                internal_transaction_id=internal_transaction_id,
                external_transaction_id=body.external_transaction_id
            )
            return response, 400