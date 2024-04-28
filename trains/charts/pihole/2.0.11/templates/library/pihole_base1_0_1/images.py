from .utils import ports_bindings

def pihole_image_name(tag):
    return f'pihole:{tag}'

def port_to_bind(port):
    return ports_bindings(port, port)
