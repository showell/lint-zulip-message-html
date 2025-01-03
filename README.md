This code allows you to validate that an HTML message
conforms to the type of HTML that a Zulip markdown
processor creates.  It's still a bit of work in progress,
but it's been tested on 500k real-world messages as well
as 183 test fixture messages.

******

This project is on hold for a while, but it has useful
to crib off if you want to learn how to walk an lxml tree.

It also now correctly shows the current subset of Zulip
messages in `rules.py`.

******

Key files:

- `test.py` - run this to see it action
- `html_validator/validator.py` - this is the main entry point
- `zulip_message_rules/rules.py` - sets up the actual rules for Zulip in `CONFIG`

The code is all Python, and the only dependency is
the `lxml` library.

There are a couple sort-of-overlapping use cases for this code:

- prevent rogue parsers from creating bad HTML
- allow WYSIWIG clients to send HTML to Zulip
- phase out the use of Zulip markdown in the long run
- learn about Zulip from reading `rules.py`
- facilitate ports of the Zulip markdown processor (e.g. to Djot) by quickly identifying broken HTML

The code mostly uses an accept-list type of approach,
as opposed to trying to exclude evil things:

- tags must be found in rules.py
- attributes must be found in rules.py (per tag)
- classes must be found in rules.py or validated by custom rules

Security TODOS:
- prevent tags like script, applet, etc. (DONE)
- avoid attributes like onclick, onload, etc. (DONE)
- scrutinize style attributes (MOSTLY DONE)
- scrutinize href and src attributes (TODO)
- scrutinize data-foo attributes (TODO)
- make sure the HTML is well-balanced and tidy (TODO)

One of the tricky things about Zulip is that it supports
pygment and katex syntax, so that makes the universe of
acceptable HTML a bit bigger. The ugliest aspect is that
`<span>` tags have a zillion valid HTML classes from pygment/katex,
as well as a different class for each possible emoji.
We use the `CUSTOM_TAG_HANLDERS` mechanism to handle some of
the trickier details of validating those classes.

Other than that, the Zulip HTML is fairly consistent
and clean in terms of structure.

The code is pretty fast. On my box I can validate almost
a million messages per minute.

TECH DETAILS: The validator code uses the popular `lxml`
library for the actual parsing of the HTML.  Then,
my custom Python code uses appropriate data structures like
dictionaries, sets, or tiny lists to ensure speed.
Each call to `validate_html` makes an AST and then walks
it recursively.

The validator throws exceptions when it finds any errors,
which avoids ugly debugging code if you're deep into the
AST.

As far as code quality, there is lots of room for improvement.
I try to keep it formatted with out-of-the-box `ruff`, so the
code is tidy. I also use `flake8` out-of-the-box.

I use `mypy --strict` for static type safety.

This code is tested on python 3.12, but I don't use any
super exotic Python features. It should be relatively simple
to port to JS and other languages, as it's all data manipulation.

