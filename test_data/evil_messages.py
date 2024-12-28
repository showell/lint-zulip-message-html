EVIL_MESSAGES = [
    "<p><script></p>",
    "<p src='fred'>src is a bad attr</p>",
    "<a class='fred'></a>",
    "<a fred=1>fred is bad attr</a>",
    "<path><div></div></path>",  # path should be leaf
    "<div>text spam</div",
    "<span class='fred'></span>",
    "<span class='emoji emoji-whatever fred'></span>",
]
