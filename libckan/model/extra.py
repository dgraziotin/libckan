__author__ = 'dgraziotin'

import serializable


class Extra(serializable.Serializable):
    def __init__(self):
        self.id = ''
        self.value = ''
        self.key = ''
        self.package_id = ''
        self.revision_id = ''
        self.revision_timestamp = ''
