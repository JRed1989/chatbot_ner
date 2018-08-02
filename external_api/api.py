import json

from django.http import HttpResponse
from datastore.datastore import DataStore


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
        print('result', result)
        status = True

    except TypeError:
        return HttpResponse(status=500)
    return HttpResponse(json.dumps({'status': status}), content_type='application/json')
