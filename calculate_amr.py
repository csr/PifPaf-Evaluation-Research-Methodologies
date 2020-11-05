import numpy as np
import pandas as pd

pif_night_data = './results.csv'
data = pd.read_csv(pif_night_data)
pifpaf = data['PifPaf Prediction']
ground_truth = data['Total bbox']
total_MR = 0
for i in range(len(pifpaf)):
    #If pifpaf detects more we should discard the value
    #MR of image x 
    if(ground_truth[i] != 0 and pifpaf[i]<=ground_truth[i]):
        MR = max(0,ground_truth[i]-pifpaf[i])/ground_truth[i]
        #print('MR of image id '+str(data['ImageID'][i])+' is '+str(MR))
        total_MR +=MR

#Average Miss rate 
aMR = total_MR/len(pifpaf)
print("Average miss rate = "+str(aMR))