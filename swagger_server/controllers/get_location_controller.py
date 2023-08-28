import connexion

from swagger_server.models.base_request import BaseRequest  # noqa: E501

from flask.views import MethodView

from timeit import default_timer

from swagger_server.uses_cases.get_location_uses_cases import GetLocationUseCase
from swagger_server.services.get_location_service import GetLocationService
from swagger_server.utils.transactions.transaction import generate_internal_transaction_id
from swagger_server.utils.logs.logging import log as logging
from swagger_server.resources.db import db


class GetLocationView(MethodView):

    def __init__(self):
        log = logging()
        self.log = log
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '
        self.msg_log_time = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: Fin de la transacción, procesada en : %r milisegundos'
        get_geolocation_service = GetLocationService()
        self.get_geolocation_use_case = GetLocationUseCase(get_geolocation_service, log)

    def get_geolocation(self):  # noqa: E501
        """Obtener localizacion

        Obtener localizacion # noqa: E501

        :param body: 
        :type body: dict | bytes

        :rtype: ResponseGetLocation
        """
        response = ""
        internal_transaction_id = str(generate_internal_transaction_id())
        function_name = "get_geolocation"
        package_name = __name__
        log = logging()
        start_time = default_timer()

        if connexion.request.is_json:
            body = BaseRequest.from_dict(connexion.request.get_json())  # noqa: E501
            message = f"start request: {function_name}"
            log.info(
                self.msg_log,
                internal_transaction_id, body.external_transaction_id, function_name, package_name, message)

        response = self.get_geolocation_use_case.get_location(body, internal_transaction_id)

        end_time = default_timer()
        log.info("ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: Fin de la transacción, procesada en : %r milisegundos", internal_transaction_id, body.external_transaction_id, f"{function_name}", __name__, round((end_time-start_time)*1000))
        return response
