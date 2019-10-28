===========================
Sphinx Code Fence Extension
===========================

.. image:: https://readthedocs.org/projects/sphinx-codefence/badge/?version=latest
    :target: https://sphinx-codefence.readthedocs.io

This is a single-module sphinx extension that monkey-patches docutils adding
the ability to parse code fences. For example, the following code fence is
rendered as a block of python code:

.. code::

    ~~~py
    def hello_codefence():
      print("I am in a codefence!")
    ~~~

For more information, see the documentation_

.. _documentation: https://sphinx-codefence.readthedocs.io
