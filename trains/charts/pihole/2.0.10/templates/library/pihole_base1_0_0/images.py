from .utils import port_binding

def db_image_name(tag):
    return f'mongo:{tag}'

def express_image_name(tag):
    return f'mongo-express:{tag}'

def port_to_bind(port):
    return port_binding(port, port)