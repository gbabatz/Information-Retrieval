import xml.etree.ElementTree as et


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


root = et.Element('paremeters')

et.SubElement(root, 'index').text = '/home/gbabatz/workspace/Information_retrieval/project1/IR-2019-2020-Project-1/indices/index1'

et.SubElement(root, 'rule').text = 'method:dirichlet,mu:1000'

et.SubElement(root, 'count').text = '1000'

et.SubElement(root, 'trecFormat').text = 'true'

# loop from here
# parse the topics

topics_tree = et.parse('../topics_all_reformated_readable.xml')
topics_root = topics_tree.getroot()

number = 301

for title, desc, narr in zip(topics_root.iter('title'), topics_root.iter('desc'), topics_root.iter('narr')):

    query = et.SubElement(root, 'query')
    et.SubElement(query, 'type').text = 'indri'

    et.SubElement(query, 'number').text = str(number)
    number += 1

    # got to take the 'Description: ' off the text
    # we know that the word takes a standard size on the beggining of the string
    desc.text = desc.text[14:]
    # same for Narrative:
    narr.text = narr.text[12:]

    et.SubElement(query, 'text').text = title.text + desc.text + narr.text


indent(root)
tree = et.ElementTree(root)
tree.write('../queries_titles_desc_narr_tree.xml')
