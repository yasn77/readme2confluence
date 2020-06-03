"""
readme2confluence
-----------------

Create a Confluence page from a Markdown README file

"""
import os
import sys
from markdown2 import Markdown
from atlassian import Confluence
from pkg_resources import get_distribution

__version__ = get_distribution('readme2confluence').version

def get_md_text(md_file):
    """
    Take a file and return the text of that file
    """
    sys.stderr.write("Getting Markdown text from {}/{}".format(os.getcwd(), md_file))
    assert os.path.isfile(md_file)
    with open(md_file, 'r') as this_file:
        text = this_file.read()
    return text

def md2html(markdown):
    """
    Take Markdown text and convert it to HTML
    """
    markdowner = Markdown(safe_mode=False, extras={"fenced-code-blocks": {"full": False},
                                                   "smarty-pants": None,
                                                   "tables": None,
                                                   "task_list": None})
    return markdowner.convert(markdown)

class Readme2Confluence:
    """
    Main class that will create the Confluence page from Markdown
    """
    def __init__(self, url, username, password, space):
        self.confluence = Confluence(url, username=username, password=password)
        spaces = self.confluence.get_all_spaces(start=0, limit=500)
        if any(s for s in spaces if s["name"] == space):
            self.space = space
        else:
            raise ValueError("{} is not valid Confluence Space".format(space))

    def get_page_id(self, title):
        """
        Retrieve the ID of a page using it's title
        This is basically a small wrapper around confluence.get_page_id().
        The main reason for the wrapper is to better handle pages that aren't found
        by raising an exception
        """
        page_id = self.confluence.get_page_id(self.space, title)
        if page_id is None:
            raise ValueError("{} is not a valid page title in {}".format(title, self.space))
        return page_id

    def get_page_html(self, title):
        """
        Retrieve a confluence page and return it as a
        HTML (string)
        """
        page_id = self.get_page_id(title)
        return self.confluence.get_page_by_id(page_id)


    def send2confluence(self, title, parent_title=None, md_file=None, md_text=""):
        """
        Method that creates the confluence page.
        Page will either be created or updated depending on what is
        required.
        """
        if md_file is None:
            body = md2html(md_text)
        else:
            body = md2html(get_md_text(md_file))

        parent_id = None if parent_title is None else self.get_page_id(parent_title)
        page_id = self.confluence.get_page_id(self.space, title)

        if page_id is None:
            ret = self.confluence.create_page(self.space,
                                              title,
                                              body,
                                              parent_id=parent_id,
                                              type='page',
                                              representation='storage')
        else:
            ret = self.confluence.update_page(page_id,
                                              title,
                                              body,
                                              parent_id=parent_id,
                                              type='page',
                                              representation='storage')
        return ret
