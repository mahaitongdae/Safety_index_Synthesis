from tensorflow.keras.layers import Dense
from tensorflow.keras import Model, Sequential
from tensorflow import Variable
import tensorflow as tf


class MLPNet(Model):
    def __init__(self, input_dim, num_hidden_layers, num_hidden_units, output_dim, **kwargs):
        super(MLPNet, self).__init__(**kwargs)
        self.first_ = Dense(num_hidden_units, input_shape=(None, input_dim), activation='elu')
        self.hidden = Sequential([Dense(num_hidden_units, activation='elu') for _ in range(num_hidden_layers-1)])
        self.outputs = Dense(output_dim, activation='elu')
        self.build(input_shape=(None, input_dim))

    def call(self, x, **kwargs):
        x = self.first_(x)
        x = self.hidden(x)
        x = self.outputs(x)
        return x

def test_attrib():
    import numpy as np

    a = Variable(0, name='d')

    p = MLPNet(2, 2, 128, 1, name='ttt')
    print(hasattr(p, 'get_weights'))
    print(hasattr(p, 'trainable_weights'))
    print(hasattr(a, 'get_weights'))
    print(hasattr(a, 'trainable_weights'))
    print(type(a))
    print(type(p))
    # print(a.name)
    # print(p.name)
    # p.build((None, 2))
    p.summary()
    # inp = np.random.random([10, 2])
    # out = p.forward(inp)
    # print(p.get_weights())
    # print(p.trainable_weights)


def test_clone():
    p = MLPNet(2, 2, 128, 1, name='ttt')
    print(p._is_graph_network)
    s = tf.keras.models.clone_model(p)
    print(s)

def test_out():
    import numpy as np
    Qs = tuple(MLPNet(8, 2, 128, 1, name='Q' + str(i)) for i in range(2))
    inp = np.random.random((128, 8))
    out = [Q(inp) for Q in Qs]
    print(out)


def test_memory():
    import time
    Q = MLPNet(8, 2, 128, 1)
    time.sleep(111111)

def test_memory2():
    import time
    model = tf.keras.Sequential([tf.keras.layers.Dense(10, input_shape=(30,), activation='relu'),
                                 tf.keras.layers.Dense(20, activation='relu'),
                                 tf.keras.layers.Dense(20, activation='relu'),
                                 tf.keras.layers.Dense(10, activation='relu')])
    time.sleep(10000)



if __name__ == '__main__':
    test_memory2()