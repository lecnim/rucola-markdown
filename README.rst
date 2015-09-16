===============
rucola-markdown
===============

.. image:: https://travis-ci.org/lecnim/rucola-markdown.svg?branch=master
    :target: https://travis-ci.org/lecnim/rucola-markdown

A Rucola plugin used to render markdown files.

Installation
------------

You can install using ``pip``: ::

    $ pip install rucola-markdown

Dependencies
~~~~~~~~~~~~

The plugin requires a `markdown <https://pypi.python.org/pypi/Markdown/>`_
package. If you use ``pip``, it will automatically install it for you.

Usage
-----

You can use the plugin without arguments, it will render all markdown ``md``
files into ``html``.

.. code-block:: python

    from rucola_markdown import Markdown

    app = Rucola()
    app.use(
        Markdown()  # same as: Markdown('**/*.md')
    )

You can render chosen files:

.. code-block:: python

    app.use(
        Markdown('path/to/file.md'),  # render given file
        Markdown('path/to/*.md'),     # render all md files in directory
        Markdown('path/to/foo.txt')   # file extension is not a problem
    )

Support for the markdown extensions is available:

.. code-block:: python

    app.use(
        Markdown('*.md', toc=True),             # render using table of contents
        Markdown('*.md', toc={'baselevel': 3})  # set extension options
    )


Options
~~~~~~~

pattern:
    Renders all files that matches a pattern. Default is ``**/*.md``.

**extensions:
    A dict with used extensions, a key is a extension name,
    a value is a dict with extensions options or True if no options.


License
-------

MIT