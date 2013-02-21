libckan
=======
libckan is a Python library for OKFN CKAN APIv3. It will support the Action API `CKAN API`_, of CKAN v2.0.0.

It might eventually support the DataStore API `DATASTORE API`_, and the FileStore API `FILESTORE API`_, by re-using ckanclient codebase
and become the de-facto CKAN standard client library. However, the plans actually are to make it a ckanclient `CKANCLIENT`_ companion.

It is libckan aim to reach 90%+ line coverage before releasing a version to the public.

.. _CKAN API: https://ckan.readthedocs.org/en/255-update-api-docs/api.html
.. _DATASTORE API: https://ckan.readthedocs.org/en/255-update-api-docs/datastore-api.html
.. _FILESTORE API: https://ckan.readthedocs.org/en/255-update-api-docs/filestore-api.html
.. _CKANCLIENT: https://github.com/okfn/ckanclient


CKAN Api key
-------------
Please manually insert your CKAN Api key for master.ckan.org in the file libckan/model/client.py
::
    API_KEY = 'insertithere'

This will obviously change in the future.


Tests
-----
libckan uses nosetests. Run then in the root of the project.

Documentation
-------------
Work in progress.
Checkout the latest documentation build on `Read The Docs`_
You will use libckan like this:::

    import libckan.logic.action.get
    packages = libckan.logic.action.get.package_search(q='test')

Checkout the tests folder to learn something more.
Otherwise, please look at the source for the moment.

.. _Read The Docs: https://libckan.readthedocs.org/en/latest/


Values
------
The following is the set of Values being followed while developing libckan.
They are listed in preferred order and priority.

1. Use `Semantic Versioning`_
2. Adhere to CKAN API syntax and semantics as most as possible.
3. Document the Public API and the Models
4. No commit/merge in master unless a 90%+ test coverage is ensured for the file. Rare exceptions may exist (e.g., HTTP errors non reproducible)
5. Adhere to `PEP8`_ before a version is released

.. _Semantic Versioning: https://semver.org
.. _PEP8: http://www.python.org/dev/peps/pep-0008


License
------------
BSD 3-Clause License (Revised). See COPYING.rst for the license.


Status
------------
Very, very early development. Stay tuned.

