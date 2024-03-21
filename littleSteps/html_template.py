template = """<html>
<head>
    <title>%(title)s</title>
</head>
<body>
%(text)s
</body>
</html>"""
data = {"title": "Мой сайт",
        "text": "Контент"}
print(template % data)
