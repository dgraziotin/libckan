__author__ = 'dgraziotin'

import serializable


class TrackingSummary(serializable.Serializable):
    def __init__(self):
        self.total = 0
        self.recent = 0
