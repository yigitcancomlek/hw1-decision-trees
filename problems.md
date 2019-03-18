# Coding (5 points)
Your task is to implement two machine learning algorithms:

1. Decision tree (in `code/decision_tree.py`)
2. Prior probability (in `code/prior_probability.py`)

You will also write code that reads in data into numpy arrays and code that manipulates
data for training and testing in `code/data.py`.

You will implement evaluation measures in `code/metrics.py`:

1. Confusion matrix (`code/metrics.py -> confusion_matrix`)
2. Precision and recall (`code/metrics.py -> precision_and_recall`)
3. F1-Measure (`code/metrics.py -> f1_measure`)

The entire workflow will be encapsulated in `code/experiment.py -> run`. The run function 
will allow you to run each approach on different datasets easily. You will have to 
implement this `run` function.

Your goal is to pass the test suite (contained in `tests/`). Once the tests are passed, you 
may move on to the next part - reporting your results.

Your grade for this section is defined by the autograder. If it says you got an 80/100,
you get 4 points here. Suggested order for passing test_cases:

1. test_load_data
2. test_train_test_split
3. test_confusion_matrix
4. test_accuracy
5. test_precision_and_recall
6. test_f1_measure
7. test_experiment_run_prior_probability
8. test_experiment_run_decision_tree
9. test_experiment_run_and_compare

# Free-response questions (5 points)

1. To handle attributes that are real-valued (e.g. height, weight, age) with the ID3 algorithm, one must pick a split point for each attribute (e.g. height > 3). How would you pick a split point? Explain why you think that would be a good idea. Is there an example data distribution for which your approach would not work well?

2. There is a difference between what a decision tree can represent and what functions exist in the world that might need to be represented. What if you you want to use a decision tree built with ID3 to represent the concept weight > age. In other words, you want to return "true" if someone's weight is greater than their age and "false" otherwise.  Can you do it? If so, specify the decision tree. If not, say why not.

3. Let <img src="/tex/6c4adbc36120d62b98deef2a20d5d303.svg?invert_in_darkmode&sanitize=true" align=middle width=8.55786029999999pt height=14.15524440000002pt/> a voter in the set of voters <img src="/tex/a9a3a4a202d80326bda413b5562d5cd1.svg?invert_in_darkmode&sanitize=true" align=middle width=13.242037049999992pt height=22.465723500000017pt/>. Let each <img src="/tex/6c4adbc36120d62b98deef2a20d5d303.svg?invert_in_darkmode&sanitize=true" align=middle width=8.55786029999999pt height=14.15524440000002pt/> have a value drawn from <img src="/tex/e3d7babdf84d997af0eefde61fc68c05.svg?invert_in_darkmode&sanitize=true" align=middle width=23.744301899999993pt height=21.18721440000001pt/>. The majority-rule algorithm is defined as the rounded sum of all voters. If over half of the voters say 0, it returns 0, if over half return 1, it returns 1. Assume an odd number of voters. Can you represent this function in a decision tree? If so, how? if not, why not?

4. How well did your decision tree learn the majority-rule function? How well did it learn XOR.  How well did it learn on the Ivy League problem? What about these data sets made the ID3 learning algorithm suitable or unsuitable for learning the function for each data set?

5. In general, what kinds of functions does ID3 work well for and what kinds of functions does it work poorly for. 


