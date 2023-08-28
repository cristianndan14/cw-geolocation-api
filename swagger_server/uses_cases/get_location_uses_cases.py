from swagger_server.models.base_request import BaseRequest
from swagger_server.models.response_get_location import ResponseGetLocation
from swagger_server.models.data_get_location import DataGetLocation
from swagger_server.services.get_location_service import GetLocationService
from swagger_server.utils.logs.logging import log as Logging
from flask import request


class GetLocationUseCase:

    def __init__(self, get_location_service: GetLocationService, log: Logging):
        self.log = log
        self.get_location_service = get_location_service
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '

    def get_location(self, body: BaseRequest, internal_transaction_id: str):
        try:
            location = self.get_location_service.get_location_service(internal_transaction_id, body.external_transaction_id)
            
            data = DataGetLocation(
                ip=request.environ.get("HTTP_X_FORWARDED_FOR", request.remote_addr),
                latitude=location['location']['lat'],
                longitude=location['location']['lng']
            )
            
            response = ResponseGetLocation(
                channel=None,
                external_transaction_id=body.external_transaction_id,
                internal_transaction_id=internal_transaction_id,
                code=0,
                message="Datos obtenidos exitosamente.",
                data=data
            )
            return response
        except Exception as ex:
            response = ResponseGetLocation(
                channel=None,
                external_transaction_id=body.external_transaction_id,
                internal_transaction_id=internal_transaction_id,
                code=1,
                message=str(ex),
                data=[]
            )
            return response, 400