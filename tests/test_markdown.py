import os
import unittest
from rucola import Rucola
from rucola_markdown import Markdown


class Test(unittest.TestCase):

    def setUp(self):

        self.maxDiff = None
        self.app = Rucola(os.path.dirname(__file__))

    def test_no_arguments(self):

        self.app.use(Markdown())
        self.assertEqual('<h1>hello</h1>\n<p>foo</p>', self.app.get('basic.html').content)

    def test_pattern(self):

        self.app.use(Markdown('b*.md'))
        self.assertEqual('<h1>hello</h1>\n<p>foo</p>', self.app.get('basic.html').content)

    def test_abbr(self):

        self.app.use(
            Markdown(abbr=True)
        )
        self.assertEqual(
            '<p>The <abbr title="Hyper Text Markup Language">HTML</abbr> specification.</p>',
            self.app.get('abbr.html').content)

    def test_wikilinks(self):

        self.app.use(
            Markdown(wikilinks={'base_url': '/home/'})
        )
        self.assertEqual(
            '<p><a class="wikilink" href="/home/test/">test</a></p>',
            self.app.get('wikilinks.html').content)
