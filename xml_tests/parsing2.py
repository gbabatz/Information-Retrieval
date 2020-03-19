xmlstr = open('topics.xml').read()

xmlsplited = xmlstr.split(' ')

# making sure that every tag is seperated from the other
xmlsplited2 = []
for subxml in xmlsplited:

    temp = subxml.split('\n')

    for element in temp:

        xmlsplited2.append(element)

print(xmlsplited2)

def make_end_tag(tag):
    endtag = [char for char in tag]
    endtag.insert(1, '/')
    endtag = ''.join(endtag)
    return endtag

result = []
temptag = ''
for index, elem in enumerate(xmlsplited2):

    # adding root
    if index == 0 :
        result.append('<topics>')
    elif index == (len(xmlsplited2)-1):
        result.append('</topics>')

    #escape char
    if '&' in elem:
        elem = elem.replace('&', '&amp;')

    if '<num>' in elem:
        result.append(elem)
        temptag = make_end_tag(elem)
    elif '<title>' in elem:
        result.append(temptag)
        result.append(elem)
        temptag = make_end_tag(elem)
    elif '<desc>' in elem:
        result.append(temptag)
        result.append(elem)
        temptag = make_end_tag(elem)
    elif '<narr>' in elem:
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

#print(newstr)

with open('topics_reformated.xml','w') as filenew:
    filenew.write(newstr)


# making it readable
def indent(elem, level=0):
    i = "\n" + level * "  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level + 1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


import xml.etree.ElementTree as et

tree = et.parse('topics_reformated.xml')
root = tree.getroot()

indent(root)
newtree = et.ElementTree(root)
newtree.write('topics_reformated_readable.xml')