# Benchmark Data for Accurate and Efficient Comparison of Machine Learning Models for Materials Discovery

## Data
This repository contains datasets gathered from a variety of papers related to machine learning models used for materials discovery. The 'raw_data' directory contains the pre-split datasets, while the 'split_data' directory contains the split datasets. All datasets are in .csv format. An explanation of the specific method used for splitting each dataset is described below.

Datasets with more than 100 values were split into train, test, and validation sets, either using 10-fold or 5-fold cross-valdiation with the use of the scikit-learn [K-Fold cross-validation method](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html). The number of folds (10 vs 5) was determined primarily by following what each respective study did. Datasets with less than 100 values were split into train and test sets using the scikit-learn [Leave-One-Out cross-validation method](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeaveOneOut.html).

Each dataset can be downloaded and read in by using Pandas. An example is shown below.
```
import pandas as pd
data = pd.read_csv("Bala_classification_dataset/val/val0.csv")
```
The code that was used to split the datasets via the K-Fold and the Leave-One-Out cross-validation methods is located in the [code](code/lit_data_k_splits.py) directory. To run this code, the 'raw_data' directory will need to be downloaded, and the path given at the beginning of the code will need to be changed.
```
def read_in_data():
   # the following path needs to be changed
    path = '/Users/anhender/Documents/UROP/Literature_Data/Lit_cleaned_data/'
```

## Works Cited
Below are the papers whose data were used to populate this repository. The corresponding datasets are listed below their respective paper. Additionally, a general overview of the papers can be seen in the Lit_Data_Overview_ver_final.xlsx file, which includes information such as the materials system, material property tested, machine learning model used, and performance metrics.

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
* Mannodi-Kanakkithodi, Arun, et al. "Machine learning strategy for accelerated design of polymer dielectrics." Scientific reports 6 (2016): 20952. https://doi.org/10.1038/srep20952  
   - Mannodi_polymer_dielec
* Pilania, Ghanshyam, et al. "Accelerating materials property predictions using machine learning." Scientific reports 3.1 (2013): 1-6. https://doi.org/10.1038/srep02810
   - Pilania_Polymers_data
   - Pilania_Polymers_data_Spring_Const_clean
   - Pilania_Polymers_data_total_Dielec_Const_clean
* Pilania, Ghanshyam, et al. "Machine learning bandgaps of double perovskites." Scientific reports 6 (2016): 19375. https://doi.org/10.1038/srep19375 
   - Pilania_double_perovskites_clean
* Pilania, Ghanshyam, and X-Y. Liu. "Machine learning properties of binary wurtzite superlattices." Journal of materials science 53.9 (2018): 6652-6664. https://doi.org/10.1007/s10853-018-1987-z 
   - Pilania_superlattices
   - Pilania_superlattices_Formation_E_clean
   - Pilania_superlattices_GGA_Band_Gap_clean
   - Pilania_superlattices_HSE_Band_Gap_clean
   - Pilania_superlattices_elastic_consts
* Rajan, Arunkumar Chitteth, et al. "Machine-learning-assisted accurate band gap predictions of functionalized MXene." Chemistry of Materials 30.12 (2018): 4031-4038. https://doi-org.ezproxy.lib.utah.edu/10.1021/acs.chemmater.8b00686 
   - Rajan_MXene_data
* Seko, Atsuto, et al. "Machine learning with systematic density-functional theory calculations: Application to melting temperatures of single-and binary-component solids." Physical Review B 89.5 (2014): 054303. https://doi.org/10.1103/PhysRevB.89.054303
   - Seko_melt_temps
* Wei, Han, et al. "Predicting the effective thermal conductivities of composite materials and porous media by machine learning methods." International Journal of Heat and Mass Transfer 127 (2018): 908-916. https://doi.org/10.1016/j.ijheatmasstransfer.2018.08.082 
   - Wei_composite_materials
   - Wei_porous_media
* Wu, K., et al. "Prediction of polymer properties using infinite chain descriptors (ICD) and machine learning: Toward optimized dielectric polymeric materials." Journal of Polymer Science Part B: Polymer Physics 54.20 (2016): 2082-2091. https://doi-org.ezproxy.lib.utah.edu/10.1002/polb.24117 
   - Wu_DFT_Eg_dielec_consts
   - Wu_Exp_Tg
   - Wu_Exp_dielec_const
   - Wu_loss_tang_100Hz
   - Wu_loss_tang_1kHz
* Xue, Dezhen, et al. "Accelerated search for materials with targeted properties by adaptive design." Nature communications 7.1 (2016): 1-9. https://doi.org/10.1038/ncomms11241 
   - Xue_thermal_hysteresis
* Zeng, Shuming, et al. "Machine learning-aided design of materials with target elastic properties." The Journal of Physical Chemistry C 123.8 (2019): 5042-5047. https://doi-org.ezproxy.lib.utah.edu/10.1021/acs.jpcc.9b01045 
   - Zeng_elastic_prop
* Zhuo, Ya, Aria Mansouri Tehrani, and Jakoah Brgoch. "Predicting the band gaps of inorganic solids by machine learning." The journal of physical chemistry letters 9.7 (2018): 1668-1673. https://pubs.acs.org/doi/abs/10.1021/acs.jpclett.8b00124
   - Zhuo_classification_data
   - Zhuo_regression_data

## Acknowledgments
This work was supported by the University of Utah's [Undergraduate Reserach Opportunities Program (UROP)](https://our.utah.edu/urop/) for the Fall 2020 Semester.
