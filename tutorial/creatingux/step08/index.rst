=============================
Step 08: AJAX With JSON Views
=============================

Modern web development means AJAX. Through its renderer support,
Pyramid makes return JSON data from a view very easy and coherent with
the rest of the Pyramid architecture.

In this step we add a box to ach screen which fetches, format,
and re-fetches site news updates.

Goals
=====

- Show Pyramid's support for AJAX

Background
==========

- Learn about the ``json`` renderer

- Add a test for the JSON response

- Include into the main template

Steps
=====

#. ``$ cd ../creatingux; mkdir step08; cd step08``

#. (Unchanged) Copy the following into ``step08/application.py``:

   .. literalinclude:: application.py
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

