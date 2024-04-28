from .utils import port_binding

def nginx_image_name(tag):
    return f'nginx:{tag}'

def port_to_bind(port):
    return port_binding(port, port)
