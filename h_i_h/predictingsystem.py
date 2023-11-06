import numpy as np
import pickle
 #loading the saved model
loaded_model = pickle.load(open('C:/Users\ac/Desktop/h_i_h/New folder/trained_model (1).sav', 'rb'))
input_data = (1,85,66,29,0,26.6,0.351,30)

# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

# standardize the input data


prediction = loaded_model.predict(std_data)
print(prediction)

if (prediction[0] == 0):
  print('The person is not diabetic')
else:
  print('The person is diabetic')