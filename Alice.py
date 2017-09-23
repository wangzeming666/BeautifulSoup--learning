html_doc="""
<html>
	<head>
		<title> The three pig's story.</title>
	</head>
	<body>
		<p class="title"><b> The three pig's story</b></p>

		<p class="title"> Once upon a time there were three little pigs; and their names were

		<a href="http://example.com/elsie" class="sister" id="link1">Elisie</a>

		<a href="http://example.com/elsie" class="sister" id="link2">Lacie</a>

		<a href="http://example.com/elsie" class="sister" id="link3">Tillie</a>;
		and they lived at the bottom if a well.</p>

	</body>
</html>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, "lxml")
print(soup.prettify())
