import pickle
import gzip
with gzip.open('../data/mnist.pkl.gz', 'rb') as f:
    train, validation, test = pickle.load(f, encoding="latin1")
    test_inputs = test[0]
    test_outputs = test[1]
    test_data = zip(test_inputs, test_outputs)
    len(test_data)
    
    # for x, y in test_data:
        # print(y)
    # print(train)

    