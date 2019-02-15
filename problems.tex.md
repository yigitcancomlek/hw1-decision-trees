# Coding 
Your task is to implement two machine learning algorithms:

1. Decision tree (in code/decision_tree.py)
2. Prior probability (in code/prior_probability.py)

You will also write code that reads in data into numpy arrays and code that manipulates
data for training and testing in code/data.py.

You will implement evaluation measures in code/metrics.py:

1. Confusion matrix (code/metrics.py -> confusion_matrix)
2. Precision and recall (code/metrics.py -> precision and recall)
3. F1-Measure (code/metrics.py -> f1_measure)

Your goal is to pass the test suite (contained in tests/). Once the test is passed, you 
may move on to the next part - reporting your results.

# Report 
Your task is to run the machine learning algorithms you have implemented on various
datasets and synthesize the results into a coherent report. Someone reading your 
report should be able to:

1. Understand the datasets you used - their structure, size, etc.
2. Understand the approaches you used - how they work, how they are trained, etc.
3. Understand the experiment you set up. What approaches were run on which datasets? What
   was the training data? What was the testing data? Did you use n-fold cross 
   validation?
4. Know how your approaches performed on the datasets. You may report confusion 
   matrices, f1-measure, precision and recall. You can also include graphs that you 
   think are interesting. 
5. Gain insight from your discussion of the results from the experiment. If am 
   approach failed for a specific dataset, discuss why it failed. For example, was it
   because of a bug in the implementation? Or something inherent to the approach that
   makes it impossible for this task? If an approach succeeded on a dataset, discuss why 
   it succeeded.

Your write-up should be clear and concise. Writing good reports are an important part 
of machine learning. When writing machine learning papers, you'll have to do something
like this. When making models in industry, you will have to communicate to your
manager that your new model actually works before it gets deployed. This is done 
through a clear, rigorous experimental report that is easily understood by others.
Here is a suggested outline:

1. Describe datasets used.
2. Describe the approaches used.
3. Explain your experiment clearly.
4. Report your results.
5. Discuss your results.
