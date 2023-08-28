import connexion

from flask.views import MethodView

from timeit import default_timer

from swagger_server.models.request_rev_geo_code import RequestRevGeoCode  # noqa: E501
from swagger_server.uses_cases.rev_geocode_uses_cases import RevGeocodeUseCase
from swagger_server.services.rev_geocode_service import RevGeocodeService
from swagger_server.utils.transactions.transaction import generate_internal_transaction_id
from swagger_server.utils.logs.logging import log as logging



class RevGeocodeView(MethodView):

    def __init__(self):
        log = logging()
        self.log = log
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '
        self.msg_log_time = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: Fin de la transacción, procesada en : %r milisegundos'
        rev_geocode_service = RevGeocodeService()
        self.rev_geocode_use_case = RevGeocodeUseCase(rev_geocode_service, log)

    def rev_geocode(self):  # noqa: E501
        """Obtiene la ubicación inversa

        Obtiene la ubicación inversa (reverse geocoding) basada en las coordenadas proporcionadas. # noqa: E501

        :param body: 
        :type body: dict | bytes

        :rtype: ResponseRevGeoCode
        """
        response = ""
        internal_transaction_id = str(generate_internal_transaction_id())
        function_name = "rev_geocode"
        package_name = __name__
        log = logging()
        start_time = default_timer()

        if connexion.request.is_json:
            body = RequestRevGeoCode.from_dict(connexion.request.get_json())  # noqa: E501
            message = f"start request: {function_name}"
            log.info(
                self.msg_log,
                internal_transaction_id, body.external_transaction_id, function_name, package_name, message)

        response = self.rev_geocode_use_case.get_rev_geocode(body, internal_transaction_id)

        end_time = default_timer()
        log.info("ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: Fin de la transacción, procesada en : %r milisegundos", internal_transaction_id, body.external_transaction_id, f"{function_name}", __name__, round((end_time-start_time)*1000))
        return response
