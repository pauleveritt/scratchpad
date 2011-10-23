======================
Hello World in Pyramid
======================

What's the simplest way to get started? A single-file module. No
packages, imports, ``setup.py``, or other machinery.

Goals
=====

- Get Pyramid pixels on the screen as easily as possible

- Use that as a well-understood base for adding each unit of complexity

Background
==========

Microframeworks are all the rage these days. They provide low-overhead
on execution. But also, they have a low mental overhead: they do so
little, the only things you have to worry about are *your things*.

Pyramid is special because it can act as a single-file module
microframework. You have a single Python file that can be executed
directly by Python. But Pyramid also scales to the larges of
applications.

Steps
=====

#. ``mkdir creatingux; cd creatingux``

#. ``mkdir step01; cd step01``

#. Copy the following into ``step01/application.py``:



- A "view" as a function

- It returns a string

Running
=======

- Add env27/bin to your path

- cd to step01

- python application.py

- Open in browser