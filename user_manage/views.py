# Create your views here.
from MyWebApp.json_utils import result_handler


def hello(request):
    return result_handler('Hello Word!')
