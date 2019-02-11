import connexion
import six

from swagger_server.models.get_lat_lon import GetLatLon  # noqa: E501
from swagger_server import util
from google_request import get_coordinades


def get_latlon_get(body):  # noqa: E501
    """obtener tiempo estimado

     # noqa: E501

    :param body: hello
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = connexion.request.get_json()  # noqa: E501
        print(body)
        #print(body["Destino"])
        #inicio 
        direccionI = body["Inicio"]["address"]
        numeroI = str(body["Inicio"]["number"])
        comunaI = body["Inicio"]["comuna"]
        ciudadI = body["Inicio"]["ciudad"]
        paisI = body["Inicio"]["pais"]
        coordenadaI = get_coordinades(direccionI, numeroI, comunaI, ciudadI, paisI)
        #destino
        direccionD = body["Destino"]["address"]
        numeroD = str(body["Destino"]["number"])
        comunaD = body["Destino"]["comuna"]
        ciudadD = body["Destino"]["ciudad"]
        paisD= body["Destino"]["pais"]
        coordenadaD = get_coordinades(direccionD, numeroD, comunaD, ciudadD, paisD)

        data = {
            "latitud_final": coordenadaD['lat'],
            "latitud_inicial": coordenadaI['lat'],
            "longitud_final": coordenadaD['lng'],
            "longitud_inicial": coordenadaI['lng']
            }
        
    return data
