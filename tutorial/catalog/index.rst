====================
Using repoze.catalog
====================

Install
-------

You have to install repoze.catalog into the venv.

application.py
--------------

Nothing needed here

resources.py
------------

Note the imports of catalog and index from repoze.catalog.

We create a catalog and two text indexes for title and content attributes.

We add the catalog *inside* the site folder. We also add a document map, which
helps us map actual content to catalog ids.

views.py
--------

On the add_folder and add_content views, we now index the document and add it
to the document map. We use the content ittem's path on the site to make the
map. 

To obtain a nice docid for the catalog, we use document_map.new_docid().

The path is obtained using the pyramid.traversal.resource_path() call.

After that we can index with catalog.index_doc().

The search view makes a query for all content with the search term either in
the title or the content of all catalogued items.

The [results] dance afterwards is to get the actual objects from the doc_id via
the document map.

Note the use of render_to_response to use the search template and not the one
configured for this view.
