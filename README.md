# Benchmark Data for Accurate and Efficient Comparison of Machine Learning Models for Materials Discovery

## Data
This repository contains datasets gathered from a variety of papers related to machine learning models used for materials discovery. The 'raw_data' directory contains the pre-split datasets, while the 'split_data' directory contains the split datasets. All datasets are in .csv format. An explanation of the specific method used for splitting each dataset is described below.

Datasets with more than 100 values were split into train, test, and validation sets, either using 10-fold or 5-fold cross-valdiation with the use of the scikit-learn [KFold cross-validation method](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html). The number of folds (10 vs 5) was determined by what each specific paper had done in their own respective studies. Datasets with less than 100 values were split into train and test sets using the scikit-learn [LeaveOneOut cross-validaiton method](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeaveOneOut.html).

Each dataset can be downloaded and read in by using Pandas. An example is shown below.
```
import pandas as pd
data = pd.read_csv("Bala_classification_dataset/val/val0.csv")
```
The code that was used to split the datasets via the K-Fold and the Leave-One-Out cross-validation methods is located in the [code](code/lit_data_k_splits.py) directory. To run this code, the 'raw_data' directory will need to be downloaded, and the path given at the beginning of the code will need to be changed respectively:
```
def read_in_data():
   # the following path needs to be changed
    path = 'Literature_Data/Lit_cleaned_data/'
```

## Works Cited
Here lists the papers whose data were used to complete this repository. The corresponding datasets are listed below their respective paper. Additionally, a general overview of each paper can be seen in the Lit_Data_Overview_ver_final.xlsx file, which includes information such as the materials system, material property tested, machine learning model used, and performance metrics.

* Balachandran, Prasanna V., et al. "Experimental search for high-temperature ferroelectric perovskites guided by two-step machine learning." Nature communications 9.1 (2018): 1-9. https://doi.org/10.1038/s41467-018-03821-9
   - Bala_classification_dataset
   - Bala_regression_dataset
* Carrete, Jesús, et al. "Finding unprecedentedly low-thermal-conductivity half-Heusler semiconductors via high-throughput materials modeling." Physical Review X 4.1 (2014): 011019. https://journals.aps.org/prx/abstract/10.1103/PhysRevX.4.011019 
   - Carrete_therm_conduct_train_clean
* Lee, Joohwi, et al. "Prediction model of band gap for inorganic compounds by combination of density functional theory calculations and machine learning techniques." Physical Review B 93.11 (2016): 115104. https://doi.org/10.1103/PhysRevB.93.115104 
   - Lee_band_gaps
* Li, Wei, Ryan Jacobs, and Dane Morgan. "Predicting the thermodynamic stability of perovskite oxides using machine learning models." Computational Materials Science 150 (2018): 454-463. https://doi.org/10.1016/j.commatsci.2018.04.033 
   - Li_DFT_and_features_clean
   - Li_DFT_dataset_clean
* Liu, Yue, et al. "The onset temperature (Tg) of AsxSe1-x glasses transition prediction: A comparison of topological and regression analysis methods." Computational Materials Science 140 (2017): 315-321. https://doi.org/10.1016/j.commatsci.2017.09.008 
   - Liu_Tg_AsSe_glass
 
