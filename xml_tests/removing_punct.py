import string


def remove_dublicates(x):
  return list(dict.fromkeys(x))


def remove_punctuation(str_in,punctuation_list):
    char_list_without_punct = [char for char in str_in if char not in punctuation_list]
    text_without_punct = ''.join(char_list_without_punct)
    return text_without_punct

punct_list = set(string.punctuation)
print(punct_list)

text_example = 'A relevant document must as a minimum identify the organization and the type of illegal activity (e.g., Columbian cartel exporting cocaine). Vague references to international drug trade without identification of the organization(s) involved would not be relevant.'

print(text_example)
print(remove_punctuation(text_example,punct_list))