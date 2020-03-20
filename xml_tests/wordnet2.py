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


def del_dubl(x):
  return list(dict.fromkeys(x))


root = et.Element('paremeters')

et.SubElement(root, 'index').text = '/home/gbabatz/workspace/Information_retrieval/project1/IR-2019-2020-Project-1/indices/index1'

et.SubElement(root, 'rule').text = 'method:dirichlet,mu:1000'

et.SubElement(root, 'count').text = '1000'

et.SubElement(root, 'trecFormat').text = 'true'

# loop from here
# parse the topics

# import nltk
# nltk.download()
from nltk.corpus import wordnet


topics_tree = et.parse('topics_reformated_readable.xml')
topics_root = topics_tree.getroot()

number = 301

for title in topics_root.iter('title'):

    query = et.SubElement(root, 'query')
    et.SubElement(query, 'type').text = 'indri'

    et.SubElement(query, 'number').text = str(number)
    number += 1

    title_words = title.text.split(' ')
    title_words = del_dubl(title_words)

    original_words = []
    for word in title_words:

        syns = wordnet.synsets(word)
        if syns:
            for word in syns:
                # plain_word = word.lemmas()[0].name()
                for plain_word in word.lemmas():
                    if plain_word.name() not in original_words:
                        original_words.append(plain_word.name())
        else:
            original_words.append(word)


    title_enhanced = ' '.join(original_words)

    # # got to take the 'Description: ' off the text
    # # we know that the word takes a standard size on the beggining of the string
    # desc.text = desc.text[14:]
    # # same for Narrative:
    # narr.text = narr.text[12:]

    # et.SubElement(query, 'text').text = title.text + desc.text + narr.text
    et.SubElement(query, 'text').text = title_enhanced


indent(root)
tree = et.ElementTree(root)
tree.write('titles_tree_enhanced.xml')
