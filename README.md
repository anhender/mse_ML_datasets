# Benchmark Data for Accurate and Efficient Comparison of Machine Learning Models for Materials Discovery

## Data
This repository contains datasets gathered from a variety of papers related to machine learning models used for materials discovery. The datasets are located under the directory labeled 'data' and are all in .csv format. Each dataset has been split into train, test, and validation sets OR simply train, test sets with the use of the scikit-learn [KFold cross-validation method](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html), depending on the number of folds. An explanation of the specific method used for each dataset is described below.

Datasets with more than 100 values were split into train, test, and validation sets, either using 10-fold or 5-fold cross-valdiation. The number of folds (10 vs 5) was determined by what each specific paper had done in their own respective studies. Datasets with less than 100 values were split into train and test sets using the scikit-learn [LeaveOneOut cross-validaiton method](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeaveOneOut.html).

Each dataset can be downloaded and read in by using Pandas. An example is shown below.
```
import pandas as pd
data = pd.read_csv("Bala_classification_dataset/val/val0.csv")
```
