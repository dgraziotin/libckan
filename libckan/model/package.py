__author__ = 'dgraziotin'

import serializable
import resource


class Package(serializable.Serializable):

    def __init__(self, name=''):
        #TODO check default values
        self.id = ''
        self.name = name
        self.title = ''
        self.type = None
        self.version = ''
        self.state = ''
        self.revision_id = ''
        self.url = ''
        self.ckan_url = ''
        self.download_url = ''
        self.notes_rendered = ''
        self.notes = ''
        self.tracking_summary = None

        self.license_id = ''
        self.license = ''
        self.license_title = ''
        self.licese_url = ''

        self.author = ''
        self.author_email = ''
        self.maintainer = ''
        self.maintainer_email = ''

        self.tags = []
        self.groups = []
        self.isopen = True
        self.metadata_created = ''
        self.metadata_modified = ''
        self.relationships = []

        self.resources = []

        self.ratings_count = 0
        self.rating_average = 0.0

        self.extras = None

    def add_resource(self, resource):
        self.resources.append(resource)

    #def add_relationship(self, package):
    #    #TODO
    #    pass

    @staticmethod
    def from_dict(dict):
        pkg = Package()
        for key in dict.keys():
            if pkg.__dict__.has_key(key):
                if key == 'resources':
                    for resource_dict in dict[key]:
                        pkg.add_resource(resource.Resource.from_dict(resource_dict))
                else:
                    pkg.__dict__[key] = dict[key]
        return pkg