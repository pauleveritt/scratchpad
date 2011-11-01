======================
Hello World for Logins
======================

Adding security to your application mixes in lots of ideas at once. In
this step we introduce just one: authorization.

Goals
=====

- Show how you protect a resource

Objectives
==========

- Introduce concept of an ACL

Steps
=====

#. ``$ cd ../../security; mkdir step01; cd step01``

#. (Unchanged) Copy the following into ``step01/application.py``:

   .. literalinclude:: application.py
      :linenos:

#. Copy the following into ``step01/views.py``:

   .. literalinclude:: views.py
      :linenos:

#. Copy the following into ``step01/resources.py``:

   .. literalinclude:: resources.py
      :linenos:

#. Copy the following into ``step01/templates/default_view.pt``:

   .. literalinclude:: templates/default_view.pt
      :language: html
      :linenos:

#. Copy the following into ``step01/tests.py``:

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