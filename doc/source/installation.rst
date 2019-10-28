============
Installation
============

-------------
Local Install
-------------

The extension is a single file (`sphinx_codefence.py`) so the easiest thing to
do is grab it and put it somewhere that sphinx can find it. For example, we
can follow the recommendations of the sphinx documentation `hello world`_
extension. If your sphinx document tree looks like this:

.. _`hello world`: https://www.sphinx-doc.org/en/master/development/tutorials/helloworld.html

.. code::

  ├── build
  ├── Makefile
  └── source
      ├── conf.py
      ├── index.rst
      ├── _static
      └── _templates

Then add a directory `_ext` to `source/` and put `sphinx_codefence.py` in
it:

.. code::

  ├── build
  ├── Makefile
  └── source
      ├── conf.py
      ├── _ext
      │   └── sphinx_codefence.py
      ├── index.rst
      ├── _static
      └── _templates

Now update your `conf.py` with:

```
import os
import sys

# Add the local extension directory to the python path
sys.path.insert(0, os.path.abspath('./_ext'))

# include the condefence parser monkeypatch
extensions = [
  "sphinx_codefence"
]
```

----
PyPi
----

The extension is available via PYPI_. You can install it using `pip`:

.. _PYPI: https://pypi.org/project/sphinx-codefence

.. code::

   pip install sphinx-extension

And then update your `conf.py` adding "sphinx_codefence" to your list of
extensions, such as:

.. code::

   extensions = [
     "sphinx_codefence"
   ]
