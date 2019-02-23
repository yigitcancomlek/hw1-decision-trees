import numpy as np
from sklearn.datasets import make_classification
import random, string
import csv

def write_random_csv_file(n_features, n_samples):
    features, targets = make_classification(
        n_samples=n_samples, 
        n_features=n_features, 
        n_classes=2
    )
    attribute_names = [
        random_string(10) for i in range(n_features)
    ]
    
    with open('tests/test.csv', 'w', newline='') as csvfile:
        writer = csv.writer(
            csvfile, 
            delimiter=',', 
            quotechar='|', 
            quoting=csv.QUOTE_MINIMAL
        )
        writer.writerow(attribute_names + ['class'])
        for i in range(features.shape[0]):
            row = features[i].tolist() + [targets[i].tolist()]
            writer.writerow(row)

    return features, targets, attribute_names

def random_string(N):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))

def test_load_data():
    from code import load_data

    n_features = np.random.randint(5, 20)
    n_samples = np.random.randint(50, 150)
    features, targets, attribute_names = write_random_csv_file(n_features, n_samples)

    _features, _targets, _attribute_names = load_data('tests/test.csv')
    assert type(_features) == np.ndarray and type(_targets) == np.ndarray
    assert len(attribute_names) == len(_attribute_names)
    assert features == _features and targets == _targets

def test_train_test_split():
    from code import train_test_split

    n_features = np.random.randint(5, 20)
    n_samples = np.random.randint(50, 150)
    features, targets, attribute_names = write_random_csv_file(n_features, n_samples)
    fraction = np.random.rand()

    output = train_test_split(features, targets, fraction)
    expected_train_size = int(n_samples * fraction)
    expected_test_size = int(n_samples * (1 - fraction))

    for o in output:
        assert o.shape[0] == expected_train_size or o.shape[0] == expected_test_size