"""
This Python package contains the definition of a CKAN Dataset / Package.
"""
__author__ = 'dgraziotin'

import serializable
import resource
import trackingsummary
import tag
import extra

class Package(serializable.Serializable):
    """
    A CKAN Package of Open Data.
    """
    def __init__(self, name=''):
        self.id = ''
        self.name = name
        self.title = ''
        self.type = None
        self.version = None
        self.state = ''
        self.revision_id = ''
        self.revision_timestamp = ''
        self.url = None
        self.ckan_url = ''
        self.download_url = ''
        self.notes_rendered = ''
        self.notes = ''
        self.tracking_summary = trackingsummary.TrackingSummary()

        self.license_id = 'notspecified'
        self.license = ''
        self.license_title = 'License Not Specified'
        self.licese_url = ''

        self.author = ''
        self.author_email = ''
        self.maintainer = ''
        self.maintainer_email = ''
        self.owner_org = None
        self.organization = None

        self.tags = []
        self.num_tags = 0
        self.groups = [] #TODO convert to objects
        self.isopen = True
        self.private = False
        self.metadata_created = ''
        self.metadata_modified = ''
        self.relationships = [] #TODO convert to objects

        self.resources = []
        self.num_resources = 0

        self.ratings_count = 0
        self.rating_average = 0.0

        self.extras = []

    def add_resource(self, resource_obj):
        """
        Add a Resource to the Package's array of resources

        :param resource_obj: The Resource to be associated to the Package
        :type name: :class:`libckan.model.resource.Resource`

        :raises: ValueError if resource_obj is not a Resource
        """
        if not isinstance(resource_obj, resource.Resource):
            raise ValueError('Please add only libckan.model.reource.Resource to a Package.')
        self.resources.append(resource_obj)

    def add_tag(self, tag_obj):
        """
        Add a Tag to the Package's array of tags

        :param tag_obj: The Resource to be associated to the Package
        :type name: :class:`libckan.model.tag.Tag`

        :raises: ValueError if tag_obj is not a Tag
        """
        if not isinstance(tag_obj, tag.Tag):
            raise ValueError('Please add only libckan.model.tag.Tag to a Package.')
        self.tags.append(tag_obj)
        self.num_tags = len(self.tags)

    def add_extra(self, extra_obj):
        """
        Add an Extra to the Package's array of extras

        :param extra_obj: The Resource to be associated to the Package
        :type name: :class:`libckan.model.extra.Extra`

        :raises: ValueError if extra_obj is not an Extra
        """
        if not isinstance(extra_obj, extra.Extra):
            raise ValueError('Please add only libckan.model.extra.Extra to a Package.')
        self.extras.append(extra_obj)

    @classmethod
    def from_dict(cls, package_dict):
        """
        Convert a CKAN JSON Package, already converted to a PYthon dict, to a CKAN Python Package.

        :param package_dict: The CKAN Package already converted to a Python dict.
        :type name: dict
        :returns: The resulting CKAN Python Package.
        :rtype: :class:`libckan.models.package.Package`

        :raises: ValueError if package_dict is not a dict
        """
        if not isinstance(package_dict, dict):
            raise ValueError('Please add only libckan.model.extra.Extra to a Package.')

        pkg = Package()
        for key in package_dict.keys():
            if pkg.__dict__.has_key(key):
                if key == 'resources':
                    for resource_dict in package_dict[key]:
                        pkg.add_resource(resource.Resource.from_dict(resource_dict))
                elif key == 'tracking_summary':
                    pkg.tracking_summary = trackingsummary.TrackingSummary.from_dict(package_dict[key])
                elif key == 'tags':
                    for tag_dict in package_dict[key]:
                        pkg.add_tag(tag.Tag.from_dict(tag_dict))
                elif key == 'extras':
                    for extra_dict in package_dict[key]:
                        pkg.add_tag(extra.Extra.from_dict(extra_dict))
                else:
                    pkg.__dict__[key] = package_dict[key]
        return pkg