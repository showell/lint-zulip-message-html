This code allows you to validate that an HTML message
conforms to the type of HTML that a Zulip markdown
processor creates.  It's still a bit of work in progress,
but it's been tested on 250k real-world messages as well
as 183 test fixture messages.

Key files:

- `test.py` - run this to see it action
- `validator.py` - this is the main entry point
- `rules.py` - sets up the actual rules for Zulip

The code is all Python, and the only dependency is
the `lxml` library.

There are a couple sort-of-overlapping use cases for this code:

- prevent rogue parsers from creating bad HTML
- allow WYSIWIG clients to send HTML to Zulip
- phase out the use of Zulip markdown in the long run
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

Other than that, the Zulip HTML is fairly consistent
and clean in terms of structure.

The code is pretty fast. On my box I can validate over
a half million messages per minute.  It uses lxml for
the actual parsing, and then the custom Python that I
wrote tries to use appropriate data structures like
dictionaries, sets, or tiny lists.  The validator just
walks the AST recursively.

The validator throws exceptions when it finds any errors,
which avoids ugly debugging code if you're deep into the
AST.

As far as code quality, there is lots of room for improvement.
I try to keep it formatted with out-of-the-box `ruff`, so the
code is tidy. I also use `flake8` out-of-the-box.

I am not yet using `mypy`.

This code is tested on python 3.12, but I don't use any
super exotic Python features. It should be relatively simple
to port to JS and other languages, as it's all data manipulation.

