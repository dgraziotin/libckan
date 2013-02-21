__author__ = 'dgraziotin'

import serializable


class TrackingSummary(serializable.Serializable):
    """
    Tracking Summary  object contained in a Package tracking_summary attribute
    """
    def __init__(self):
        self.total = 0
        self.recent = 0
