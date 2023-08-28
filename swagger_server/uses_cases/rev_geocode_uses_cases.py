from swagger_server.models.request_rev_geo_code import RequestRevGeoCode
from swagger_server.models.response_rev_geo_code import ResponseRevGeoCode
from swagger_server.services.rev_geocode_service import RevGeocodeService
from swagger_server.utils.logs.logging import log as Logging


class RevGeocodeUseCase:

    def __init__(self, rev_geocode_service: RevGeocodeService, log: Logging):
        self.log = log
        self.rev_geocode_service = rev_geocode_service
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '

    def get_rev_geocode(self, body: RequestRevGeoCode, internal_transaction_id: str):
        try:
            data_request = body.data.to_dict()
            data = self.rev_geocode_service.get_rev_geocoding(
                data_request['latitude'],
                data_request['longitude'],
                internal_transaction_id=internal_transaction_id,
                external_transaction_id=body.external_transaction_id
            )
            response = ResponseRevGeoCode(
                channel=None,
                external_transaction_id=body.external_transaction_id,
                internal_transaction_id=internal_transaction_id,
                code=0,
                message="Datos obtenidos exitosamente.",
                data=data
            )
            return response
        except Exception as ex:
            response = ResponseRevGeoCode(
                channel=None,
                external_transaction_id=body.external_transaction_id,
                internal_transaction_id=internal_transaction_id,
                code=1,
                message=str(ex),
                data=[]
            )
            return response, 400