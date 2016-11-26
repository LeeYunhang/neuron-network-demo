from network1 import Network
import mnist_loader

(train_data, validation_data, test_data) = mnist_loader.load_data_wrapper()
net = Network([784, 10, 10])
net.SGD(list(train_data), epochs=100, mini_batch_size=10, eta=0.1, test_data=list(test_data))