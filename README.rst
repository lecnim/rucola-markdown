===============
rucola-markdown
===============

A Rucola plugin used to render markdown files.

Installation
------------

Install with a ``pip`` command:

::

    $ pip install rucola-markdown

Dependencies
~~~~~~~~~~~~

Plugin requires ``markdown`` package.

Usage
-----

Using a plugin without arguments - all *.md files will be rendered to *.html

.. code-block:: python

    from rucola_markdown import Markdown

    app = Rucola()
    app.use(
        Markdown()  # same as: Markdown('**/*.md')
    )

Plugin can render specified files:

.. code-block:: python

    app.use(
        Markdown('path/to/file.md')  # render given file
        Markdown('path/to/*.md')     # render all md files in directory
        Markdown('path/to/foo.txt')  # file extension is not a problem
    )

Support for markdown plugins is available:

.. code-block:: python

    app.use(
        Markdown('*.md', toc=True)               # render given file
        Markdown('*.md', toc={'baselevel': 3})   # render all md files in directory
    )


Options
~~~~~~~

pattern:
    Renders all files that matches a pattern. Default is '**/*.md'

**extensions:
    Dict with used extensions, a key is a extension name,
    a value is a dict with extensions options or True if no options.


License
-------

MIT