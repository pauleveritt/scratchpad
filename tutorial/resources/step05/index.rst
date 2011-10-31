=================================
Step 05: Projector with Resources
=================================


Goals
=====


Objectives
==========


Steps
=====

#. ``$ cd ../../creatingux; mkdir step05; cd step05``

#. Copy the following into ``step05/application.py``:

   .. literalinclude:: application.py
      :linenos:

#. ``$ mkdir static``

#. Copy the following into ``step05/static/global_layout.css``:

   .. literalinclude:: static/global_layout.css
      :language: css
      :linenos:

#. Copy the following into ``step05/static/global_layout.js``:

   .. literalinclude:: static/global_layout.js
      :language: js
      :linenos:

#. Copy the following into ``step05/views.py``:

   .. literalinclude:: views.py
      :linenos:

#. Copy the following into ``step05/layouts.py``:

   .. literalinclude:: layouts.py
      :linenos:

#. Copy the following into ``step05/dummy_data.py``:

   .. literalinclude:: dummy_data.py
      :linenos:

#. Copy the following "global template" into
   ``step05/templates/global_layout.pt``:

   .. literalinclude:: templates/global_layout.pt
      :language: html
      :linenos:

#. Copy the following "macros template" into
   ``step05/templates/macros.pt``:

   .. literalinclude:: templates/macros.pt
      :language: html
      :linenos:

#. Copy the following into ``step05/templates/index.pt``:

   .. literalinclude:: templates/index.pt
      :language: html
      :linenos:

#. Copy the following into ``step05/templates/about.pt``:

   .. literalinclude:: templates/about.pt
      :language: html
      :linenos:

#. Copy the following into ``step05/templates/company.pt``:

   .. literalinclude:: templates/company.pt
      :language: html
      :linenos:

#. Copy the following into ``step05/templates/people.pt``:

   .. literalinclude:: templates/people.pt
      :language: html
      :linenos:

#. Copy the following into ``step05/test_views.py``:

   .. literalinclude:: test_views.py
      :linenos:

#. Copy the following into ``step05/test_layout.py``:

   .. literalinclude:: test_layout.py
      :linenos:

#. ``$ nosetests`` should report running 10 tests.

#. ``$ python application.py``

#. Open ``http://127.0.0.1:8080/`` in your browser.


Extra Credit
============

Analysis
========

- We are using self-posting forms

Discussion
==========

