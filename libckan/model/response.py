__author__ = 'dgraziotin'

import serializable


class Response(serializable.Serializable):

    def __init__(self):
        self.help = None
        self.result = None
        self.success = None
