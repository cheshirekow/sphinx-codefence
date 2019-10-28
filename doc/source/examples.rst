========
Examples
========

The content of a codefence is parsed the same
as the content of a ``.. code::`` directive.

For example, the following:

.. code::

   ```
   Hello world!
   ```

Is rendered as:

```
Hello world!
```

Code fences support languages. The language keyword is passed as the optional
argument to the ``.. code::`` directive. For example:


.. code::

   ```cpp
   int main(int argc, char** argv){
     exit(0);
   }
   ```

Is rendered as:

```cpp
int main(int argc, char** argv){
  exit(0);
}
```

Code fences can also be nested within indented structures, such as:

.. code::

   .. tip::

      This code-fence is nested within an admonition.

      ```py
      def hello_world():
        print("hello world")
      ```

which is rendered as:

.. tip::

   This code-fence is nested within an admonition.

   ```py
   def hello_world():
     print("hello world")
   ```

However the whole point of using a code-fence is to avoid the indentation
so I'm not sure why you'd want to do that.

There are two styles of codefence. You can either use triple-tick or
triple-tilde. The examples thus-far have been triple-tick. Triple-tilda
looks like this:

.. code::

   ~~~py
   def hello_codefence():
     print("I am in a codefence!")
   ~~~

Which renders as:

~~~py
def hello_codefence():
  print("I am in a codefence!")
~~~
