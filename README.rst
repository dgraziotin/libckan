libckan
=======

libckan is a Python library for OKFN CKAN APIv3. It will support the Action API `CKAN API`_, of CKAN v2.0.0.

It might eventually support the DataStore API `DATASTORE API`_, and the FileStore API `FILESTORE API`_, by re-using ckanclient codebase
and become the de-facto CKAN standard client library. However, the plans actually are to make it a ckanclient `CKANCLIENT`_ companion.

It is libckan aim to reach 90%+ test coverage before pushing the source-code to the public.

.. _CKAN API: https://ckan.readthedocs.org/en/255-update-api-docs/api.html
.. _DATASTORE API: https://ckan.readthedocs.org/en/255-update-api-docs/datastore-api.html
.. _FILESTORE API: https://ckan.readthedocs.org/en/255-update-api-docs/filestore-api.html
.. _CKANCLIENT: https://github.com/okfn/ckanclient

Documentation
-------------
Work in progress.
You will use libckan like this:

    import libckan.logic.action.get
    packages = libckan.logic.action.get.package_search(q='test')


License
------------
BSD 3-Clause License (Revised). See COPYING.rst for the license.

Status
------------
Very, very early development. Stay tuned.

