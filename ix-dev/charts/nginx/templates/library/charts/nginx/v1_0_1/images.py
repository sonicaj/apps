from base_v1_0_0.containers import container_name
from .utils import port_binding


def nginx_image_name(tag):
    return f'nginx:{tag}:{container_name("testing")}'


def port_to_bind(port):
    return port_binding(port, port)
