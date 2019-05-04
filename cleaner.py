from nltk.stem import SnowballStemmer
# from nltk import word_tokenize as tokenize

def clean(file, p = False):
    stem = SnowballStemmer('english').stem
    file = open(file, 'r')
    data = file.read().lower().split('\n')
    file.close()

    data = [d.split('\t') for d in data]
    hitlist = []
    for d in data:
        # if a line is all in brackets, remove it
        if d[1][0] == '(' and d[1][-1] == ')':
            hitlist.append(d)
        if d[1][0] == '[' and d[1][-1] == ']':
            hitlist.append(d)
        if '(' in d[1]:
            d[1] = d[1][:d[1].find('(')] + d[1][d[1].rfind(')'):]
        # the background voice thing lyrics
        if ' (' in d[1]:
            d[1] = d[1][:d[1].index(' (')]
        # lines that end in a colon are indicating who sings the verse
        if d[1][-1] == ':':
            hitlist.append(d)

        # remove punctuation
        d[1] = d[1].replace('-', ' ')
        for s in ',\'.!?;"()':
            d[1] = d[1].replace(s, '')

        d[1] = d[1].strip()

        d[1] = ' '.join([stem(i) for i in d[1].split()])

        # 1 for taytay, 2 for the beatly boys
        if d[0] == 'taylor_swift':
            d[0] = -1
        else:
            d[0] = 1

    for hit in hitlist:
        try: data.remove(hit)
        except ValueError: break

    if p: print('\n'.join([d.__repr__() for d in data]))
    return data