import pickle
import numpy as np

model = pickle.load(open("health_model.pkl","rb"))

sample = np.array([[45,27,130,180]])

prediction = model.predict(sample)

print(prediction)
