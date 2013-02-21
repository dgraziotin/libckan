__author__ = 'dgraziotin'

import serializable

class Resource(serializable.Serializable):
    """
    Python CKAN Resource representation
    """
    def __init__(self):
        self.resource_group_id = ''
        self.cache_last_updated = None
        self.package_id = ''
        self.webstore_last_updated = None
        self.id = ''
        self.size = 0
        self.last_modified = None
        self.hash = ''
        self.description = ''
        self.format = ''
        self.tracking_summary = None
        self.mimetype_inner = ''
        self.mimetype = ''
        self.cache_url = ''
        self.name = ''
        self.created = None
        self.url = ''
        self.webstore_url = ''
        self.position = 0
        self.resource_type = ''

