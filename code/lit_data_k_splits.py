# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 19:51:16 2020

@author: anhen
"""
from sklearn.model_selection import KFold, train_test_split, LeaveOneOut
import pandas as pd
import os


def read_in_data():
    path = 'Literature_Data/Lit_cleaned_data/'
    data_files = os.listdir(path)
    folders = []
    csv_files = []
    csv_df_dict = {}
    csv_df_list = []
    for file in data_files:
        # separating files that are .csv files and those that are folders
        if '.csv' in file:
            csv_files.append(file)
            data = pd.read_csv(f'{path}{file}')
            csv_df_list.append(data)
        else:
            folders.append(file)
    # reading in the .csv files' data + putting into dictionary
    for df in range(len(csv_files)):
        csv_df_dict[csv_files[df]] = csv_df_list[df]
    # going into the folders list and reading in the data
    df_dict = {}
    df_list = []
    all_file_names = []
    for folder in folders:
        file_path = f'{path}{folder}'
        files = os.listdir(file_path)
        # 31 files in total
        # print(f'{file_path}\n{os.listdir(file_path)}\n')
        for file in files:
            if folder in file:
                file_name = f'{file}'
            else:
                file_name = f'{folder}/{file}'
            all_file_names.append(file_name)
            data = pd.read_csv(f'{file_path}/{file}')
            # print(f'{folder}:{file}\n{data}')
            df_list.append(data)
        for df in range(len(all_file_names)):
            df_dict[all_file_names[df]] = df_list[df]
    # combining the csv_df_dict and df_dict into one dict
    full_dict = {**csv_df_dict, **df_dict}
    return(full_dict)


papers_dict = read_in_data()


def k_cv_5_fold():
    papers_dict = read_in_data()
    # papers needing 5-fold
    five_fold = ['Pilania_double_perovskites_clean.csv',
                 'Pilania_Polymers_data/Atomization Eng. (eV).csv',
                 'Pilania_Polymers_data/Bandgap (eV).csv',
                 'Pilania_Polymers_data/c [lattice param] (angstrom).csv',
                 'Pilania_Polymers_data/elec. Dielec. Const.csv',
                 'Pilania_Polymers_data/Electron Affinity (eV).csv',
                 'Pilania_Polymers_data/Formation Eng. (eV).csv',
                 'Pilania_Polymers_data_Spring_Const_clean.csv',
                 'Pilania_Polymers_data_total_Dielec_Const_clean.csv',
                 'Pilania_superlattices/Interfacial Energy (eV-angstrom^2).csv',
                 'Pilania_superlattices/Lattice Parameter (angstrom).csv',
                 'Pilania_superlattices_Formation_E_clean.csv',
                 'Pilania_superlattices_GGA_Band_Gap_clean.csv',
                 'Pilania_superlattices_HSE_Band_Gap_clean.csv',
                 'Pilania_superlattices_elastic_consts/c11 (GPa).csv',
                 'Pilania_superlattices_elastic_consts/c12 (GPa).csv',
                 'Pilania_superlattices_elastic_consts/c13 (GPa).csv',
                 'Pilania_superlattices_elastic_consts/c33 (GPa).csv',
                 'Pilania_superlattices_elastic_consts/c44 (GPa).csv',
                 'Wei_composite_materials.csv', 'Wei_porous_media.csv',
                 'Zeng_elastic_prop/G_Reuss.csv',
                 'Zeng_elastic_prop/G_Voigt.csv',
                 'Zeng_elastic_prop/G_VRH.csv', 'Zeng_elastic_prop/K_Ress.csv',
                 'Zeng_elastic_prop/K_voigt.csv',
                 'Zeng_elastic_prop/K_VRH.csv']
    for key in five_fold:
        df = papers_dict[key]
        kf = KFold(n_splits=5, shuffle=True, random_state=42)
        # print(key, '\n', papers_dict[key])
        training, testing, validation = [], [], []
        # create train, test, val splits
        for train_index, test_index in kf.split(df):
            df_train = df.iloc[train_index]
            val_ind, test_ind = train_test_split(test_index, train_size=0.5,
                                                 random_state=42)
            df_val = df.iloc[val_ind]
            df_test = df.iloc[test_ind]
            training.append(df_train)
            validation.append(df_val), testing.append(df_test)
        # create a directory for the df AND for train, test, val files
        folder_path = f'Lit_data_splits/5_fold/{key[:-4]}'
        csv_split_fol = ['train', 'test', 'val']
        os.makedirs(folder_path, exist_ok=True)
        for string in csv_split_fol:
            os.makedirs(f'{folder_path}/{string}', exist_ok=True)
        # save the train, test, val files to respective directories
        n_split = 5
        for i in range(n_split):
            training[i].to_csv(f'{folder_path}/train/train{i}.csv',
                               index=False, header=True)
            testing[i].to_csv(f'{folder_path}/test/test{i}.csv',
                              index=False, header=True)
            validation[i].to_csv(f'{folder_path}/val/val{i}.csv',
                                 index=False, header=True)


k_cv_5_fold()


def k_cv_10_fold():
    papers_dict = read_in_data()
# papers needing 10-fold
    ten_fold = ['Bala_classification_dataset.csv',
                'Bala_regression_dataset.csv', 'Lee_band_gaps.csv',
                'Li_DFT_and_features_clean.csv', 'Li_DFT_dataset_clean.csv',
                'Mannodi_polymer_dielec/Electronic Dielectric Constant.csv',
                'Mannodi_polymer_dielec/HSE Band Gap (eV).csv',
                'Mannodi_polymer_dielec/Ionic Dielectric Constant.csv',
                'Mannodi_polymer_dielec/Total Dielectric Constant.csv',
                'Seko_melt_temps.csv', 'Wu_DFT_Eg_dielec_consts/epsilon_e.csv',
                'Wu_DFT_Eg_dielec_consts/epsilon_i.csv',
                'Wu_DFT_Eg_dielec_consts/GAP.csv', 'Wu_Exp_Tg.csv',
                'Zhuo_classification_data.csv', 'Zhuo_regression_data.csv']
    for key in ten_fold:
        df = papers_dict[key]
        kf = KFold(n_splits=10, shuffle=True, random_state=42)
        # print(key, '\n', papers_dict[key])
        training, testing, validation = [], [], []
        # create train, test, val splits
        for train_index, test_index in kf.split(df):
            df_train = df.iloc[train_index]
            val_ind, test_ind = train_test_split(test_index, train_size=0.5,
                                                 random_state=42)
            df_val = df.iloc[val_ind]
            df_test = df.iloc[test_ind]
            training.append(df_train)
            validation.append(df_val), testing.append(df_test)
        # create a directory for the df AND for train, test, val files
        folder_path = f'Lit_data_splits/10_fold/{key[:-4]}'
        csv_split_fol = ['train', 'test', 'val']
        os.makedirs(folder_path, exist_ok=True)
        for string in csv_split_fol:
            os.makedirs(f'{folder_path}/{string}', exist_ok=True)
        # save the train, test, val files to respective directories
        n_split = 10
        for i in range(n_split):
            training[i].to_csv(f'{folder_path}/train/train{i}.csv',
                               index=False, header=True)
            testing[i].to_csv(f'{folder_path}/test/test{i}.csv',
                              index=False, header=True)
            validation[i].to_csv(f'{folder_path}/val/val{i}.csv',
                                 index=False, header=True)


k_cv_10_fold()


def leave_one_k_fold():
    papers_dict = read_in_data()
    leave_one = ['Carrete_therm_conduct_train_clean.csv',
                 'Liu_Tg_AsSe_glass.csv', 'Rajan_MXene_data.csv',
                 'Wu_Exp_dielec_const.csv', 'Wu_loss_tang_100Hz.csv',
                 'Wu_loss_tang_1kHz.csv', 'Xue_thermal_hysteresis.csv']
    for key in leave_one:
        df = papers_dict[key]
        print(len(df))
        loo = LeaveOneOut()
        # print(key, '\n', papers_dict[key])
        training, testing = [], []
        # create train, test splits
        for train_index, test_index in loo.split(df):
            df_train = df.iloc[train_index]
            df_test = df.iloc[test_index]
            # print(f'TRAIN:{df_train}\n\nTEST:{df_test}\n')
            training.append(df_train), testing.append(df_test)
        # create a directory for the df AND for train, test files
        folder_path = f'Lit_data_splits/leave_one/{key[:-4]}'
        csv_split_fol = ['train', 'test']
        os.makedirs(folder_path, exist_ok=True)
        for string in csv_split_fol:
            os.makedirs(f'{folder_path}/{string}', exist_ok=True)
        # save the train, test files to respective directories
        for i in range(len(df)):
            training[i].to_csv(f'{folder_path}/train/train{i}.csv',
                               index=False, header=True)
            testing[i].to_csv(f'{folder_path}/test/test{i}.csv',
                              index=False, header=True)


leave_one_k_fold()
