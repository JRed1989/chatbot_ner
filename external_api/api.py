import json

from django.http import HttpResponse
from datastore.datastore import DataStore
from external_api.external_api_utilities import structure_es_result


def get_entity_word_variants(request):
    """This functionality initializes text detection functionality to detect textual entities.

    Attributes:
        request: url parameters

    """
    status = False
    try:
        dictionary_name = request.GET.get('dictionary_name')
        datastore_obj = DataStore()
        result = datastore_obj.get_entity_dictionary(entity_name=dictionary_name)
        result = structure_es_result(result)
        status = True

    except TypeError:
        return HttpResponse(status=500)
    return HttpResponse(json.dumps({'status': status, 'result': result}), content_type='application/json')
