#!/usr/bin/env python3
"""
CLI script for readme2confluence
"""

import sys
import click

from . import Readme2Confluence

@click.command()
@click.version_option()
@click.option('--url', required=True, help='Confluence URL')
@click.option('--username', '-u', required=True, help='Confluence Username')
@click.option('--password', '-p', required=True, help='Confluence Password')
@click.option('--space', required=True, help="Confluence Space where pages are created")
@click.option('--title', '-t', required=True, help="Page title")
@click.option('--markdown-file', '--file', '-f', default=None, help="Markdown README file")
@click.option('--parent-title', '--parent', default=None, help="Title of Parent page")
# pylint: disable=too-many-arguments
def cli(url, username, password, space, markdown_file, title, parent_title):
    """
    Create a Confluence page from Markdown formatted README.
    You can either set --markdown-file with path to README file or
    pass the file content in through stdin.
    Options can also be set using environment variables by prefixing README2CONFLUENCE_
    for example README2CONFLUENCE_USERNAME to set username.
    """
    r2c = Readme2Confluence(url, username, password, space)
    if markdown_file is None:
        if sys.stdin.isatty():
            print("Enter the Markdown README content below then press CTRL+D when your done")
        md_content = sys.stdin.read()
        ret = r2c.send2confluence(title, parent_title=parent_title, md_text=md_content)
    else:
        ret = r2c.send2confluence(title, parent_title=parent_title, md_file=markdown_file)

    if "id" in ret.keys():
        print("{}{}".format(ret["_links"]["base"], ret["_links"]["webui"]))
    else:
        print("Failed : {}".format(ret))

if __name__ == '__main__':
    # pylint: disable=no-value-for-parameter,unexpected-keyword-arg
    cli(auto_envvar_prefix='README2CONFLUENCE')
