===========================
Sphinx Code Fence Extension
===========================

This is a single-module sphinx extension that monkey-patches docutils adding
the ability to parse code fences. For example, the following code block was
generated with a codefence (check the "page source"):

~~~py
def hello_codefence():
  print("I am in a codefence!")
~~~

----
Why?
----

It can be cumbersome when copy-pasting many chunks of code into and out of
reStructuredText documents due to the syntactic indentation required for
literal text or code directives. Code fences allow you to copy-paste snippets
into and out of your doc pages without having to fixup the indentation.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   examples
