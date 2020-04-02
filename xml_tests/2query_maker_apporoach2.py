import xml.etree.ElementTree as et

index_path = '/home/gbabatz/workspace/Information_retrieval/project1/IR-2019-2020-Project-1/indices/index1'
basic_structure = '<parameters>\n' \
                  '<index>' + index_path + '</index>\n' \
                  '<rule>method:dirichlet,mu:1000</rule>\n' \
                  '<count>1000</count>\n<trecFormat>true</trecFormat>\n'

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
queries = basic_structure
for title, desc, narr in zip(topics_root.iter('title'), topics_root.iter('desc'), topics_root.iter('narr')):

    # got to take the 'Description: ' off the text
    # we know that the word takes a standard size on the beginning of the string
    desc.text = desc.text[14:]
    # same for Narrative:
    narr.text = narr.text[12:]

    if mode_option == 0:
        text = title.text
    elif mode_option == 1:
        text = title.text + desc.text
    elif mode_option == 2:
        text = title.text + desc.text + narr.text

    query_structure = '  <query> <type>indri</type><number>' + str(number) + '</number><text> ' + text + ' </text></query>\n'
    number += 1
    queries = queries + query_structure

queries = queries + '</parameters>'

# yes it processes all even though some data may not need to be processed
# for example when I need only titles however the application is low cost
# and it looks cleaner like this

file_title = '../basic_queries_' + modes[mode_option] + '_approach2.xml'
with open(file_title, 'w') as f:
    f.write(queries)