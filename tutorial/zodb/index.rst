==========================
Storing conent on the ZODB
==========================

We install *pyramid_zodb* to handle database connections to ZODB. This pulls
the ZODB3 package as well.

To enable pyramid_zodb:

- We activate the package configuration using config.include.
- We define a zodbconn.uri setting with the path to the Data.fs file.
- We put that setting in a dict and pass it to the Configurator.

In the root factory, instead of using our old root object, we now get a
connection to the ZODB and create the object using that.

Our resources need a couple of small changes. Folders now inherit from
persistent.PersistentMapping and document from persistent.Persistent. Note
that Folder now needs to call super() on the __init__ method, or the
mapping will not initialize properly.

On the bootstrap, note the use of transaction.commit() to commit the
change. We could also have installed pyramid_tm and use config.include to
add automatic transaction handling.

The use of transaction is the only key change in the views as well.
