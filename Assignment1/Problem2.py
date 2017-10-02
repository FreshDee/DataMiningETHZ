import re
import sys
import collections


def mapCount(id, lines):
    emit_array = []
    for line in lines:
        line = line.replace("\n", " ")
        line = line.replace("\t", " ")
        line = re.sub(r'[^\w\s]', '', line)
        line = re.sub(r'[0-9]+', '', line)
        words = re.split(r'\W+', line)
        for word in words:
            if (word not in (" ", "\n")):
                emit_array.append([word.lower(), 1])
    return emit_array


def reduceCount(list_word_count_pairs):
    sums = {}
    final = {}
    letter = {}
    A = 0
    B = 100000
    for word in list_word_count_pairs:
        count = int(word[1])
        try:
            sums[word[0]] = sums[word[0]] + count
        except:
            sums[word[0]] = count
    sorted_sums = collections.OrderedDict(sorted(sums.items()))
    for word in sorted_sums.keys():
        count_word = sorted_sums[word]
        if (A <= count_word <= B):
            key = str(word)
            if (key != ""):
                try:
                    letter[key[0]] = letter[key[0]] + 1
                except:
                    letter[key[0]] = 1
                if(letter[key[0]]<=30):
        #    try:
        #        letter[word[0]]=letter[word[0]]+1
        #    except:
        #        letter[word[0]]=1
        #if (letter[word[0]]<=30):
                    final[word] = count_word
    return final


input_text = sys.stdin
word_count_pairs=reduceCount(mapCount(1, input_text))
for word in word_count_pairs.keys():
    print('%s\t%s'% ( word, word_count_pairs[word] ))
