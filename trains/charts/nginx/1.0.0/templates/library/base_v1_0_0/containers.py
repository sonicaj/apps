import random
import string


def container_name(name):
    return f'{name}_{"".join(random.choice(string.ascii_lowercase) for i in range(10))}'
