EVIL_MESSAGES = [
    "<p><script></p>",
    "<p src='bogus'>src is a bad attr</p>",
    "<a class='bogus'></a>",
    "<a bogus=1>bogus is bad attr</a>",
    "<path><div></div></path>",  # path should be leaf
    "<div>text spam</div",
    "<span class='bogus'></span>",
    "<span class='emoji emoji-whatever bogus'></span>",
    "<span style='bogus'></span>",
]
