=========================================
Step 08: CSS and JS With Static Resources
=========================================

Web applications include many static resources in the UX: CSS and JS
files, images, etc. Web frameworks need to support productive
development by the UX team, but also the richness and complexity
required by the core developers and the deployment team.

It's a surprisingly hard problem, supporting all these needs while
keeping the simple case easy.

Pyramid accomplishes this using the view machinery and static resources.

Goals
=====

- Show Pyramid's support for static resources

Objectives
==========

- Add a static view to Pyramid's ``Configurator``

- Change the main template to includes the CSS and JS

- Change the templates to have a nicer layout

.. note::

   Our templates will include jQuery from the Google CDN.

Steps
=====

#. ``$ cd ../creatingux; mkdir step08; cd step08``

#. Copy the following into ``step08/application.py``:

   .. literalinclude:: application.py
      :linenos:

#. ``$ mkdir static``

#. Copy the following into ``step08/static/global_layout.css``:

   .. literalinclude:: static/global_layout.css
      :linenos:

#. Copy the following into ``step08/static/global_layout.js``:

   .. literalinclude:: static/global_layout.js
      :linenos:

#. Copy the following into ``step08/views.py``:

   .. literalinclude:: views.py
      :linenos:

#. Copy the following into ``step08/layouts.py``:

   .. literalinclude:: layouts.py
      :linenos:

#. Copy the following into ``step08/dummy_data.py``:

   .. literalinclude:: dummy_data.py
      :linenos:

#. Copy the following "global template" into
   ``step08/templates/global_layout.pt``:

   .. literalinclude:: templates/global_layout.pt
      :language: html
      :linenos:

#. Copy the following into ``step08/templates/index.pt``:

   .. literalinclude:: templates/index.pt
      :language: html
      :linenos:

#. Copy the following into ``step08/templates/about.pt``:

   .. literalinclude:: templates/about.pt
      :language: html
      :linenos:

#. Copy the following into ``step08/templates/company.pt``:

   .. literalinclude:: templates/company.pt
      :language: html
      :linenos:

#. Copy the following into ``step08/templates/people.pt``:

   .. literalinclude:: templates/people.pt
      :language: html
      :linenos:

#. Copy the following into ``step08/test_views.py``:

   .. literalinclude:: test_views.py
      :linenos:

#. Copy the following into ``step08/test_layout.py``:

   .. literalinclude:: test_layout.py
      :linenos:

#. ``$ nosetests`` should report running 8 tests.

#. ``$ python application.py``

#. Open ``http://127.0.0.1:8080/`` in your browser.

Analysis
========

Extra Credit
============

Analysis
========

Discussion
==========

