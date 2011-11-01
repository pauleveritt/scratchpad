=======================
Hello World with Deform
=======================

Many times you want forms generated for you. If you can live within the
constraints, you gain a lot: slick widgets, automatic layout,
validation, add and edit handling, and even Ajax submission.

Deform is a part of a set of Pylons libraries that break this
functionality into its logically-separate parts:

- Peppercorn for marshalling form data from requests

- Colander for expressing constraints and fields as schemas

- Deform for generating HTML form markup from a Colander schema,
  with built-in widgets and support for custom widgets

In this step we do the smallest possible step with Deform and Colander.

Steps
=====

- easy_install deform