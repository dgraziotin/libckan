__author__ = 'dgraziotin'


class Serializable(object):
    @staticmethod
    def from_dict(dict):
        raise NotImplementedError("Please do not directly instantiate a Serializable")

    @staticmethod
    def to_dict():
        raise NotImplementedError("Please do not directly instantiate a Serializable")


class Package(Serializable) :
    def __init__(self, name=''):
        #TODO check default values
        super(Package, self).__init__()
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

    def add_relationship(self, package):
        #TODO
        pass

    @staticmethod
    def from_dict(dict):
        pkg = Package()
        for key in dict.keys():
            if pkg.__dict__.has_key(key):
                if key == 'resources':
                    for resource_dict in dict[key]:
                        pkg.add_resource(Resource.from_dict(resource_dict))
                else:
                    pkg.__dict__[key] = dict[key]
        return pkg


class Resource(Serializable):
    def __init__(self):
        super(Resource, self).__init__()
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

    @staticmethod
    def from_dict(dict):
        resource = Resource()
        for key in dict.keys():
            if resource.__dict__.has_key(key):
                resource.__dict__[key] = dict[key]
        return resource