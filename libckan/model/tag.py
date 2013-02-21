__author__ = 'dgraziotin'

import serializable


class Tag(serializable.Serializable):
    def __init__(self):
        self.vocabulary_id = None
        self.display_name = ''
        self.revision_timestamp = ''
        self.state = ''
        self.id = ''

