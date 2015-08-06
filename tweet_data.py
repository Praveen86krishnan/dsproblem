__author__ = 'Z087875'

import re
from nltk.corpus import stopwords
from nltk import PorterStemmer
#import enchant
#d = enchant.Dict("en_US")

f = open('dic.txt' , 'r')
dict = []
for word in f:
    dict.append(str(word).strip())
f.close()
# Cleaning
## remove all URL/Hyperlinks - using regex
## remove all @ only keeping ClintEastwood, BradleyCooper and ChrisKyle

htags = []
twt = []
allwords = []
stop = stopwords.words('english') + ['#americansniper', 'rt' , 'retweet']
f = open('as.txt' , 'r' )
for line in f:
    line = re.sub(r"http\S+", "", line.lower()).decode("utf8", "replace").encode('ascii', 'ignore').replace('.',' ').replace(',',' ').strip().replace('american sniper', '') #removing hyper links
    words  = [word for word in line.split() if word not in stop] #remove stop words
    final_words = []
    # dcnt = 0
    # for word in words:
    #     word = ''.join(e for e in word if e.isalnum())
    #     if len(word) > 0:
    #         if not d.check(word) :
    #             dcnt = dcnt + 1

    #if dcnt > len(words) - 3: #remove if min 3 words are
    for word in words:  #removing all the other '@'
        if word.find('@') != -1:
            for everyat in filter(None, word.split('@')):
                if everyat not in ['clinteastwood', 'clint' 'bradleycooper','bradley',  'chriskyle', 'chris']:
                    word = word.replace('@' + everyat, '')
        if word.count('#') == 1:
            htags.append(PorterStemmer().stem_word(str(word.replace('#', '')).strip()))
        elif word.count('#') > 1:
            for eachtag in filter(None, word.split('#')):
                htags.append(PorterStemmer().stem_word(str(eachtag.replace('#', '')).strip()))
        else:
            pass
        final_words.append(word)

    if len(final_words) > 2:  #removing all sentences with less than 2 words
        twt.append(' '.join(final_words))

f.close()

htags = filter(None, list(set(htags)))
twt = filter(None, list(set(twt)))

fo = open('as_op.txt' , 'w')

for line in twt:
    fo.write(line+'\n')
fo.close()

# Task one - break the twitter hashtags into proper words
taskone= []
for word in htags:
    if word not in dict:
        for i in range(len(dict)/100):
            tmpdict = '|'.join([word for word in dict[(i-1)*100:(i*100)] if len(word) > 1])
            listofwrd = re.findall(tmpdict,word)
            if len(listofwrd) > 0:
                taskone.append([word] + listofwrd)
            else:
                taskone.append([word] + [''])
    else:
        taskone.append([word, ''])


fo = open('taskone_op.txt' , 'w')

for line in taskone:
    fo.write(line+'\n')
fo.close()