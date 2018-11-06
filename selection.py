import pandas as pd
from sklearn import preprocessing


cog = pd.read_csv('cognitive_test.csv',sep=',')

CN = cog[cog['y'] == 0]         # select only records whose y value equals to 0
AD = cog[cog['y'] == 1]         # select only records whose y value equals to 1

CN = CN[['ADNI_MEM','ADNI_EF']] # pickup columns whose name is "ADNI_MEM" and "ADNI_EF"
AD = AD[['ADNI_MEM','ADNI_EF']]




