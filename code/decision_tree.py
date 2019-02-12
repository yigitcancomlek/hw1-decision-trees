import numpy as np

class DecisionTree():
    def __init__(self):
        """
        This class implements a binary decision tree learner for examples with
        categorical attributes. Use the ID3 algorithm for implementing the Decision
        Tree: https://en.wikipedia.org/wiki/ID3_algorithm

        

        

        """
        raise NotImplementedError()

    def fit(self, data):

        raise NotImplementedError()

    def predict(self, data):

        raise NotImplementedError()

def information_gain(features, attribute_index, targets):
    """
    Information gain is how a decision tree makes decisions on how to create 
    split points in the tree. Information gain is measured in terms of entropy.
    The goal of a decision tree is to decrease entropy at each split point as much as 
    possible. This function should work perfectly or your decision tree will not work
    properly.

    Information gain is a central concept in many machine learning algorithms. In
    decision trees, it captures how effective splitting the tree on a specific attribute
    will be for the goal of classifying the training data correctly. Consider 
    data points S and an attribute A. S is split into two data points given binary A:

        S(A == 0) and S(A == 1)

    Together, the two subsets make up S. If A was an attribute perfectly correlated with
    the class of each data point in S, then all points in a given subset will have the 
    same class. Clearly, in this case, we want something that captures that A is a good
    attribute to use in the decision tree. This something is information gain. Formally:

        IG(S,A) = H(S) - H(S|A)

    where H is information entropy. Recall that entropy captures how orderly or chaotic
    a system is. A system that is very chaotic will evenly distribute probabilities to 
    all outcomes (e.g. 50% chance of class 0, 50% chance of class 1). Machine learning
    algorithms work to decrease entropy, as that is the only way to make predictions 
    that are accurate on testing data. Formally, H is defined as:

        H(S) = sum_{c in (classes in S)} -p(c) * log_2 p(c)

    To elaborate: for each class in S, you compute its prior probability p(c):

        (# of elements of class c in S) / (total # of elements in S) 

    Then you compute the term for this class: 

        -p(c) * log_2 p(c)

    Then compute the sum across all classes. The final number is the entropy. To gain 
    more intution about entropy, consider the following - what does H(S) = 0 tell you 
    about S? 

    Information gain is an extension of entropy. The equation for information gain 
    involves comparing the entropy of the set and the entropy of the set when conditioned
    on selecting for a single attribute (e.g. S(A == 0)). 

    For more details: https://en.wikipedia.org/wiki/ID3_algorithm#The_ID3_metrics

    Args:
        features (np.array): numpy array containing features for each example.
        attribute_index (int): which column of features to take when computing the 
            information gain
        targets (np.array): numpy array containing labels corresponding to each example.

    Output:
        information_gain (float): information gain if the features were split on the 
            attribute_index.
    """

    raise NotImplementedError()