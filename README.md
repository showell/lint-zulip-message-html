This code allows you to validate that an HTML message
conforms to the type of HTML that a Zulip markdown
processor creates.  It's still a bit of work in progress,
but it's been tested on 250k real-world messages as well
as 183 test fixture messages.

Key files:

- `test.py` - run this to see it action
- `validator.py` - this is the main entry point
- `rules.py` - sets up the actual rules for Zulip

There are a couple sort-of-overlapping use cases for this:

- prevent rogue parsers from creating bad HTML
- allow WYSIWIG clients to send HTML to Zulip
- learn about Zulip from reading `rules.py`

The code mostly uses an accept-list type of approach,
as opposed to trying to exclude evil things:

- tags must be found in rules.py
- attributes must be found in rules.py (per tag)
- classes must be found in rules.py (except for "span")

Security TODOS:
- prevent tags like script, applet, etc. (DONE)
- avoid attributes like onclick, onload, etc. (DONE)
- scrutinize href and src attributes (TODO)
- scrutinize style attributes (TODO)
- scrutinize data-foo attributes (TODO)

One of the tricky things about Zulip is that it supports
pygment and katex syntax, so that makes the universe of
acceptable HTML a bit bigger. The ugliest aspect is that
"span" has a zillion valid attributes from pygment/katex,
as well as emojis.

Other than that, the Zulip markdown is fairly consistent
and clean.

