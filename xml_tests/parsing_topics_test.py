# import xml.etree.ElementTree as et
#
# tree = et.parse('test.xml')
#
# root = tree.getroot()
#
# for elem in root.iter():
#     print(elem.tag)


# import xmltodict,json
#
# with open('test.xml') as f:
#     doc = xmltodict.parse(f.read())
#
# print(doc['parameters'])


# import untangle
#
# docc = untangle.parse('test.xml')
#
# print(docc)



# file = open('test.xml').read()
#
# # for char in file:
# #     print(char)
#
# print(file[0] == '>')
#
# print(type(file))


# teststr = 'se katouraw'
# testlist = list(teststr)
# testlist.insert(4,' kaiegw ')
# print(str(testlist))
#
# newstr = ''.join(testlist)
# print(type(newstr))
#
# with open('newfile.xml','w') as filenew:
#     filenew.write(newstr)







xmlstr = open('test.xml').read()

print(xmlstr)

# xmllist = (list(xmlstr))

xmlsplited = xmlstr.split(' ')

print(xmlsplited)

# xmlsplited.insert(33, '</title>\n')
#
# print(xmlsplited)
#
# newstr = ' '.join(xmlsplited)
#
# print(newstr)
#
# with open('newfile.xml','w') as filenew:
#     filenew.write(newstr)

def make_end_tag(tag):
    endtag = [char for char in tag]
    endtag.insert(1, '/')
    endtag = ''.join(endtag)
    return endtag

result = []
temptag = ''
for index, elem in enumerate(xmlsplited):

    if '<title>' in elem:
        result.append(elem)
        temptag = make_end_tag(elem)
    elif '<desc>' in elem:
        result.append(temptag)
        result.append(elem)
        temptag = make_end_tag(elem)
    elif '</top>' in elem:
        result.append(temptag)
        result.append(elem)
    else:
        result.append(elem)


print(result)


newstr = ' '.join(result)

print(newstr)

with open('newfile.xml','w') as filenew:
    filenew.write(newstr)