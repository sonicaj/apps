from .utils import port_binding

def pihole_image_name(tag):
    return f'pihole:{tag}'

def port_to_bind(port):
    return port_binding(port, port)
