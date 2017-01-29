from . import v1

@v1.route('/', methods=['GET'])
def index():
    ''' Renders the API index page.
    :return:
    '''
    return "Welcome to the API version 1."

@v1.route('/hello', methods=['GET'])
def hello():
    ''' Renders the API index page.
    :return:
    '''
    return "Hello World !!!"
