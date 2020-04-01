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

index_location = ' '
abs_path = ' '
relative_bath = [' ',' ',' ','']


corpus = et.SubElement(root, 'corpus')

for path in relative_bath:
    et.SubElement(corpus, 'path').text = abs_path + path
    et.SubElement(corpus, 'class').text = 'trectext'


et.SubElement(root, 'index').text = index_location

et.SubElement(root, 'memory').text = '2024M'
et.SubElement(root, 'storeDocs').text = 'true'
stemmer = et.SubElement(root, 'stemmer')
et.SubElement(stemmer, 'name').text = 'Krovetz'

indent(root)
tree = et.ElementTree(root)
tree.write('../parameter_file.parameter')

