import numpy as np 
from code import run

def test_experiment_run_decision_tree():
    data_path = 'data/candy-data.csv'
    learner_type = 'decision_tree'
    confusion_matrix, accuracy, precision, recall, f1_measure = (
        run(data_path, learner_type, .9)
    )
    assert (accuracy > .8)
    

def test_experiment_run_prior_probability():
    data_path = 'data/candy-data.csv'
    learner_type = 'prior_probability'
    confusion_matrix, accuracy, precision, recall, f1_measure = (
        run(data_path, learner_type, .9)
    )
    assert (accuracy > .2)

def test_experiment_run_and_compare():
    data_path = 'data/candy-data.csv'
    learner_types = ['prior_probability', 'decision_tree']
    accuracies = {}
    for learner_type in learner_types:
        accuracies[learner_type] = run(data_path, learner_type, .9)[1]

    assert (accuracies['decision_tree'] > accuracies['prior_probability'])