import re
srcfile = open('source.txt', 'r')
resfile = open('result.txt', 'w')

text = srcfile.read()

srcfile.close()

list = re.findall(r'@\w+\.\w+', text)

for element in list:
    resfile.writelines(element + '\n')

resfile.close()