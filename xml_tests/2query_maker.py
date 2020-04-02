import xml.etree.ElementTree as et
import string

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


def remove_punctuation(str_in, punctuation_list):
    char_list_without_punct = [char for char in str_in if char not in punctuation_list]
    text_without_punct = ''.join(char_list_without_punct)
    return text_without_punct


# creating the xml format
root = et.Element('parameters')
et.SubElement(root, 'index').text = '/home/gbabatz/workspace/Information_retrieval/project1/IR-2019-2020-Project-1/indices/index1'
et.SubElement(root, 'rule').text = 'method:dirichlet,mu:1000'
et.SubElement(root, 'count').text = '1000'
et.SubElement(root, 'trecFormat').text = 'true'

# loop from here
# parse the topics

topics_tree = et.parse('../topics_all_reformated_readable.xml')
topics_root = topics_tree.getroot()

modes = ['titles', 'titles_desc', 'titles_desc_narr']
print("0: Titles only 1: Titles and Descriptions 2: Titles, Descriptions and Narratives ")
mode_option = 10  # random number
while mode_option < 0 or mode_option > 2:
    mode_option = int(input("Enter value: 0,1 or 2 "))

number = 301
punct_list = set(string.punctuation)
for title, desc, narr in zip(topics_root.iter('title'), topics_root.iter('desc'), topics_root.iter('narr')):

    query = et.SubElement(root, 'query')
    et.SubElement(query, 'type').text = 'indri'
    et.SubElement(query, 'number').text = str(number)
    number += 1

    # got to take the 'Description: ' off the text
    # we know that the word takes a standard size on the beginning of the string
    desc.text = desc.text[14:]
    # same for Narrative:
    narr.text = narr.text[12:]

    if mode_option == 0:
        query_txt = remove_punctuation(title.text,punct_list)
        et.SubElement(query, 'text').text = query_txt
    elif mode_option == 1:
        query_txt = remove_punctuation(title.text + desc.text, punct_list)
        et.SubElement(query, 'text').text = query_txt
    elif mode_option == 2:
        query_txt = remove_punctuation(title.text + desc.text + narr.text, punct_list)
        et.SubElement(query, 'text').text = query_txt

# yes it processes all even though some data may not need to be processed
# for example when I need only titles however the application is low cost
# and it looks cleaner like this

indent(root)
# creating the tree in order to save it
tree = et.ElementTree(root)

file_title = '../basic_queries_' + modes[mode_option] + '.xml'
# tree.write('../queries_titles_desc_narr_tree.xml')
tree.write(file_title)
