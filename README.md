# readme2confluence
---

Python module and script to create Confluence pages from Markdown file.
Main purpose and motivation is to take (Markdown) README files from git repos
and quickly create a Confluence page for it.

This can be used as part of a CI process to update Confluence documentation once README
is changed.

### Usage
```
Usage: readme2confluence [OPTIONS]

  Create a Confluence page from Markdown formatted README. You can either
  set --markdown-file with path to README file or pass the file content in
  through stdin. Options can also be set using environment variables by
  prefixing README2CONFLUENCE_ for example README2CONFLUENCE_USERNAME to set
  username.

Options:
  --url TEXT                      Confluence URL  [required]
  -u, --username TEXT             Confluence Username  [required]
  -p, --password TEXT             Confluence Password  [required]
  --space TEXT                    Confluence Space where pages are created
                                  [required]
  -t, --title TEXT                Page title  [required]
  -f, --markdown-file, --file TEXT
                                  Markdown README file
  --parent-title, --parent TEXT   Title of Parent page
  --help                          Show this message and exit.
```

#### Examples
Create a page in `DevOps` space called `foo` under `Papa` parent, using `/foo/README.md` file

```bash
readme2confluence --url https://xxxx.atlassian.net -u 'xxx.xxx@xxxx.xxx' -p $ATLASSIAN_API_TOKEN --space DevOps -t foo --parent "Papa" -f /foo/README.md
```

Same as above but use environment variables
```bash
README2CONFLUENCE_URL='https://xxxx.atlassian.net'
README2CONFLUENCE_USERNAME='xxx.xxx@xxxx.xxx'
README2CONFLUENCE_PASSWORD=$ATLASSIAN_API_TOKEN
README2CONFLUENCE_SPACE='DevOps'
README2CONFLUENCE_TITLE='foo'
README2CONFLUENCE_PARENT='Papa'
README2CONFLUENCE_MARKDOWN_FILE='/foo/README.md'

readme2confluence
```

Same as above, but use STDIN

```bash
README2CONFLUENCE_URL='https://xxxx.atlassian.net'
README2CONFLUENCE_USERNAME='xxx.xxx@xxxx.xxx'
README2CONFLUENCE_PASSWORD=$ATLASSIAN_API_TOKEN
README2CONFLUENCE_SPACE='DevOps'
README2CONFLUENCE_TITLE='foo'
README2CONFLUENCE_PARENT='Papa'

readme2confluence
Enter the Markdown README content below then press CTRL+D when your done
# Header 1
Some TEXT

bullets:

- foo
- bar
^D
```

Same as above but use pipe

```bash
README2CONFLUENCE_URL='https://xxxx.atlassian.net'
README2CONFLUENCE_USERNAME='xxx.xxx@xxxx.xxx'
README2CONFLUENCE_PASSWORD=$ATLASSIAN_API_TOKEN
README2CONFLUENCE_SPACE='DevOps'
README2CONFLUENCE_TITLE='foo'
README2CONFLUENCE_PARENT='Papa'
echo /tmp/README.md | readme2confluence
```

### Testing

At the moment there are no tests as the code is pretty simple and is more of a wrapper around
https://atlassian-python-api.readthedocs.io/en/latest/confluence.html.
Eventually we should look to add tests.
