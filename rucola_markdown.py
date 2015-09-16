import os
import markdown

# Extra:
from markdown.extensions.extra import ExtraExtension
from markdown.extensions.abbr import AbbrExtension
from markdown.extensions.attr_list import AttrListExtension
from markdown.extensions.def_list import DefListExtension
from markdown.extensions.fenced_code import FencedCodeExtension
from markdown.extensions.footnotes import FootnoteExtension
from markdown.extensions.tables import TableExtension
from markdown.extensions.smart_strong import SmartEmphasisExtension
# Other extensions:
from markdown.extensions.admonition import AdmonitionExtension
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.meta import MetaExtension
from markdown.extensions.nl2br import Nl2BrExtension
from markdown.extensions.sane_lists import SaneListExtension
from markdown.extensions.smarty import SmartyExtension
from markdown.extensions.toc import TocExtension
from markdown.extensions.wikilinks import WikiLinkExtension


EXTS = {
    'extra': ExtraExtension,
    'abbr': AbbrExtension,
    'attr_list': AttrListExtension,
    'def_list': DefListExtension,
    'fenced_code': FencedCodeExtension,
    'footnotes': FootnoteExtension,
    'tables': TableExtension,
    'smart_strong': SmartEmphasisExtension,
    'admonition': AdmonitionExtension,
    'codehilite': CodeHiliteExtension,
    'meta': MetaExtension,
    'nl2br': Nl2BrExtension,
    'sane_lists': SaneListExtension,
    'smarty': SmartyExtension,
    'toc': TocExtension,
    'wikilinks': WikiLinkExtension
}


def _get_extensions(extensions):
    """Returns a list of markdown extensions instances, ready to be passed to
    the markdown.markdown() ``extensions`` parameter.
    """

    e = []

    for key in extensions:
        if key in EXTS:

            value = extensions[key]
            if isinstance(value, dict):
                e.append(EXTS[key](**value))
            elif value:
                e.append(EXTS[key]())
            else:
                pass
        else:
            raise KeyError('Markdown: extension not found: ' + key)
    return e


def render_markdown(source, **extensions):

    # TODO: add output_format option

    e = _get_extensions(extensions)
    if not isinstance(source, str):
        source = source['content']
    return markdown.markdown(source, output_format='html5', extensions=e)


class Markdown:

    # TODO: .md or .markdown

    def __init__(self, pattern='**/*.md', **extensions):
        self.pattern = pattern
        self.exts = extensions

    def __call__(self, app):

        e = _get_extensions(self.exts)

        for f in app.find(self.pattern):
            f.content = markdown.markdown(
                f.content,
                output_format='html5',
                extensions=e)
            f.path = os.path.splitext(f.path)[0] + '.html'
