import numpy as np
import csv
#ndarray로 받아옴!
# CSV 파일을 읽어서 NumPy 배열로 가져옵니다.
arr1 = np.genfromtxt('mars_base_main_parts-001.csv', delimiter=',', dtype=None, encoding='utf-8',skip_header=1)
arr2 = np.genfromtxt('mars_base_main_parts-002.csv', delimiter=',', dtype=None, encoding='utf-8', skip_header=1)
arr3 = np.genfromtxt('mars_base_main_parts-003.csv', delimiter=',', dtype=None, encoding='utf-8', skip_header=1)

parts = np.concatenate((arr1, arr2, arr3),axis=0)
parts = np.sort(parts)

mean_strength_by_material = []
for i in range(len(parts)//3):
    value = parts[i][1]+parts[i+1][1]+parts[i+2][1]
    mean_strength_by_material.append((parts[i*3][0],value/3))

below_50 = [item for item in mean_strength_by_material if item[1] < 50]
below_50 = [['parts','strength']] + below_50

with open('parts_to_work_on.csv','w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(below_50)