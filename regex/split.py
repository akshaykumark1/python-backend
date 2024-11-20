#regex split
import re
text = "hello world"
pattern = r"\s"
result = re.split(pattern, text)
print(result)