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


def normalize(string):
    string = string.lower()
    if '_' in string:
        string = string.replace('_', '-')
    return string

root = et.Element('paremeters')

et.SubElement(root, 'index').text = '/home/gbabatz/workspace/Information_retrieval/project1/IR-2019-2020-Project-1/indices/index1'

et.SubElement(root, 'rule').text = 'method:dirichlet,mu:1000'

et.SubElement(root, 'count').text = '1000'

et.SubElement(root, 'trecFormat').text = 'true'

# loop from here
# parse the topics

import nltk
nltk.download()
from nltk.corpus import wordnet

# for ease it would be best to parse the text from the text tag of each of the
# previously made query documents, for the instanse of title+desc , title+desc+narr
# just change the file parsed
topics_tree = et.parse('../topics_all_reformated_readable.xml')
topics_root = topics_tree.getroot()

number = 301
# change the 'title' of the topics doc to 'text' tag of the query doc
for title in topics_root.iter('title'):

    query = et.SubElement(root, 'query')
    et.SubElement(query, 'type').text = 'indri'

    et.SubElement(query, 'number').text = str(number)
    number += 1

    title_words = title.text.split(' ')
    title_words = del_dubl(title_words)

    # now we have each term of the title
    original_words = []
    for word in title_words:

        # we find the synonims for each word in title
        syns = wordnet.synsets(word)

        for syn in syns:
            # syn contains an synset object

            # plan A
            # plain_word = syn.lemmas()[0].name()
            # if plain_word not in original_words:
            #     original_words.append(plain_word)

            # plan B

            # we explore the lemmas of each synonim
            for lemma in syn.lemmas():
                # I need to check if lemma word and basic word have close meanings
                lemma_name = lemma.name()

                score = syn.wup_similarity(wordnet.synsets(lemma_name)[0])

                lemma_name = normalize(lemma_name)

                if lemma_name not in original_words and score is not None and score > 0.8:
                    original_words.append(lemma_name)

        # in case the original word does not contained in the synonims
        word = normalize(word)
        if word not in original_words:
            original_words.append(word)

    original_words = del_dubl(original_words)
    title_enhanced = ' '.join(original_words)

    et.SubElement(query, 'text').text = title_enhanced


indent(root)
tree = et.ElementTree(root)
tree.write('../queries_titles_enhanced.xml')

