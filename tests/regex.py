import re
text = open('tests/tmp.txt', 'r').read()

x = re.findall("\$\w+", text)
print(x)