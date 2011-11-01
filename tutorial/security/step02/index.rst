======================================
Step 02: Basic Hierarchy for Traversal
======================================


Goals
=====


Objectives
==========


Steps
=====

#. ``$ cd ../../security; mkdir step02; cd step02``

#. (Unchanged) Copy the following into ``step02/application.py``:

   .. literalinclude:: application.py
      :linenos:

#. Copy the following into ``step02/views.py``:

   .. literalinclude:: views.py
      :linenos:

#. Copy the following into ``step02/resources.py``:

   .. literalinclude:: resources.py
      :linenos:

#. Copy the following into ``step02/templates/default_view.pt``:

   .. literalinclude:: templates/default_view.pt
      :language: html
      :linenos:

#. Copy the following into ``step02/tests.py``:

   .. literalinclude:: tests.py
      :linenos:

#. ``$ nosetests`` should report running 2 tests.

#. ``$ python application.py``

#. Open ``http://127.0.0.1:8080/`` in your browser.

Extra Credit
============


Analysis
========


Discussion
==========

