# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 11:59:04 2021

@author: Ham
FaceBook Interview

2 datasets from 2 CSV files of dinosaurs
file1:
    name,leg_length,diet

file2:
    name,stride_length,kind

Calculate the speed of each dinosaur as:
    speed = (stride_length - leg_length - 1) * sqrt(leg_length * g)
Sort the speeds from fastest to slowest, then print only dinosaur names.
In each CSV file, a name can occur several times, so keep only the last one.
A name in a CSV file might not exist in the other CSV file, and vice versa.

"""
import math
import pandas as pd
from typing import List, Tuple

import io

CSV1_SIO = io.StringIO("""
NAME,STRIDE_LENGTH,DIET
Din1,2.1,food
Din4,5.4,grass
Din3,3.6,car
Din6,4.8,bird
Din4,2.4,grasas
""".strip())

CSV2_SIO = io.StringIO("""
NAME,LEG_LENGTH,KIND
Din3,1.1,bipedal
Din4,1.2,bipedal
Din7,100.2,bipedal
Din3,2.0,bipedal
Din1,0.0,quadpedal
""".strip())


def parse_from_file(filename: str) -> dict:
    dct = dict()
    fh = open(filename) if type(filename) is str else filename
    for line in fh:
        l = line.strip().split(',')
        if l[0] != 'NAME':
            dct[l[0]] = l[1:]
    #print(dct)
    return dct

def calculate_speed(df_leg: pd.core.frame.DataFrame,
                    df_stride: pd.core.frame.DataFrame) -> List[Tuple[str, float]]:
    retval = list()
    g = 9.8
    for name in df_leg.index:
        if name in df_stride.index:
            leg_length = df_leg.LEG_LENGTH[name]
            speed = (df_stride.STRIDE_LENGTH[name] - leg_length - 1) * math.sqrt(leg_length * g)
            retval.append((name, speed))
    #print(retval)
    return retval

def select_and_calculate_speed(dict_stride: dict, dict_leg: dict, kind: str) -> list:
    retval = list()
    g = 9.8
    for name,leg in dict_leg.items():
        #print(name, leg)
        if leg[-1] != kind:
            continue
        if name in dict_stride:
            leg_length = float(leg[0])
            speed = (float(dict_stride[name][0]) - leg_length - 1) * math.sqrt(leg_length * g)
            retval.append((name, speed))
    #print(retval)
    return retval

def sort_and_print(lst: List[Tuple[str, float]]) -> None:
    lst.sort(key = lambda t: t[1], reverse=True)
    #print(lst)
    for name,speed in lst:
        print(name, speed)

if __name__ == '__main__':
    #dict_leg = parse_from_file(CSV2_SIO)
    #dict_stride = parse_from_file(CSV1_SIO)

    # Read in a CSV, indexed by the 'NAME' column, and if dup, keep the last one
    df_leg    = pd.read_csv(CSV2_SIO, index_col='NAME')
    df_leg    = df_leg[~df_leg.index.duplicated(keep='last')]
    df_stride = pd.read_csv(CSV1_SIO, index_col='NAME')
    df_stride = df_stride[~df_stride.index.duplicated(keep='last')]
    #print(df_leg)
    #print(df_stride)

    #lst = select_and_calculate_speed(dict_stride, dict_leg, 'bipedal')
    lst = calculate_speed(df_leg[df_leg.KIND == 'bipedal'], df_stride)

    sort_and_print(lst)
