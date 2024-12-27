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


