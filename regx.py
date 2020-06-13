import re
import os

stri = "The code only can tell you how it does but cannot tell you why it does so. However, your comment can do that. You use comments to explain the formulas, complex algorithms and sophisticated business logic.Python comment begins with a hash or pound sign and continues to the end of the line. It is important to note that Python interpreter ignores comments when it interpret the code.Python provides three kinds of comments including block comment, inline comment and documentation string."



pattern = "[py]"
string= input("enter anything: ")
result = re.match(pattern,string)
if result:
    print("matched")
else:
    print("unmatched")

"""
pattern = re.compile("Python")
matcher = pattern.finditer(stri)
count = 0
for i in matcher:
    count += 1
    print("python is available in",i.start())
print("the no of occurance",count)
"""

 



