import uuid
import random
import time


class Base(object):

    def __init__(self):
        # unique identifier
        self.id = '-'.join([str(time.time()), str(uuid.uuid4()), str(random.choice(range(1000)))])

    def __getattr__(self, name):
        return None

    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        self.__dict__[key] = value
