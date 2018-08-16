import re
with open("html.html",'rU') as strf:
    str = strf.read()
res = r'(?<=<h4>).*?(?=</h4>)'

li = re.findall(res,str)

with open("new.txt","w") as wstr:
    for s in li:
        wstr.write(s)
        wstr.write("\r\n")
        print(s,'\r\n')
