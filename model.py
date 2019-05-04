from sklearn.naive_bayes import GaussianNB as GNB
from sklearn.svm import SVC
from preprocessor import preprocess

def testm(model, chunks, test):
    set = [[], []]
    for chunk in chunks:
        set[0] += chunk[0]
        set[1] += chunk[1]
    model.fit(set[0], set[1])
    data = model.predict(test[0])
    num = 0
    for i in range(len(data)):
        if data[i] == test[1][i]:
            num += 1
    print(type(model))
    print(num / len(data))
    return model

def learn():
    prep = preprocess()
    chunks = prep[0]
    test = prep[1]
    nbmodel = GNB()
    svmodel = SVC(gamma = 'auto', kernel = 'linear')
    nbnum = 0
    svnum = 0

    for j in range(len(chunks)):
        chunks.insert(0, chunks.pop(-1))
        dev = chunks[0]
        train = [[], []]
        for t in chunks[1:]:
            train[0] += t[0]
            train[1] += t[1]

        nbmodel.fit(train[0], train[1])
        data = nbmodel.predict(dev[0])
        for i in range(len(data)):
            if data[i] == dev[1][i]:
                nbnum += 1
        print('Finished GNB loop {}'.format(j + 1))
        print(nbnum / len(data) / (j + 1))
        print()

        svmodel.fit(train[0], train[1])
        data = svmodel.predict(dev[0])
        for i in range(len(data)):
            if data[i] == dev[1][i]:
                svnum += 1
        print('Finished SVM loop {}'.format(j + 1))
        print(svnum / len(data) / (j + 1))
        print()

    if svnum >= nbnum:
        return testm(svmodel, chunks, test)
    else:
        return testm(nbmodel, chunks, test)

learn()