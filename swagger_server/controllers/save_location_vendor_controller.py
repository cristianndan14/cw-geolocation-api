import connexion

from flask.views import MethodView

from timeit import default_timer

from swagger_server.repository.save_location_vendor_repository import SaveLocationVendorRepository
from swagger_server.uses_cases.save_location_vendor_uses_cases import SaveLocationVendorUseCase
from swagger_server.models.request_save_location_vendor import RequestSaveLocationVendor  # noqa: E501
from swagger_server.utils.transactions.transaction import generate_internal_transaction_id
from swagger_server.utils.logs.logging import log as logging
from swagger_server.resources.db import db


class SaveLocationVendorView(MethodView):

    def __init__(self):
        log = logging()
        mysql = db
        self.log = log
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '
        self.msg_log_time = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: Fin de la transacción, procesada en : %r milisegundos'
        save_location_vendor_repository = SaveLocationVendorRepository(mysql, log)
        self.save_location_vendor_use_case = SaveLocationVendorUseCase(save_location_vendor_repository, log)

    def save_location_vendor(self):  # noqa: E501
        """Guardar localizacion de un vendedor

        Guardar localizacion de un vendedor # noqa: E501

        :param body: 
        :type body: dict | bytes

        :rtype: ResponseSaveLocationVendor
        """
        response = ""
        internal_transaction_id = str(generate_internal_transaction_id())
        function_name = "save_location_vendor"
        package_name = __name__
        log = logging()
        start_time = default_timer()

        if connexion.request.is_json:
            body = RequestSaveLocationVendor.from_dict(connexion.request.get_json())  # noqa: E501
            message = f"start request: {function_name}"
            log.info(
                self.msg_log,
                internal_transaction_id, body.external_transaction_id, function_name, package_name, message)
            
        response = self.save_location_vendor_use_case.save_location_vendor(body, internal_transaction_id)

        end_time = default_timer()
        log.info("ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: Fin de la transacción, procesada en : %r milisegundos", internal_transaction_id, body.external_transaction_id, f"{function_name}", __name__, round((end_time-start_time)*1000))
        return response

