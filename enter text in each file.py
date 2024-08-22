filenames = ['doc.txt', 'report.txt', 'presentation.txt']
contents = ['Hello']
for filename in filenames:
    file = open(filename, 'w')
    file.write("Hello")
    file.close()
names=['members.txt','report.txt']
for name in names:
    file = open(name, 'r')
    content = file.read()
    print(content)

with open('doc.txt','r') as file:
    print(file.read)


