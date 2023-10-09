import numpy as np
from sklearn import preprocessing



data_binarized = preprocessing.Binarizer(threshold=0.5).transform(input_data
)
print("\nBinarized data:\n", data_binarized)
