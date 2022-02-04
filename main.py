import pickle
import requests

r = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
data = r.text

list_of_lists = [[y for y in x.split(",")] for x in data.split("\n")]

with open("Iris.pkl", "wb") as f:
    pickle.dump(list_of_lists, f)

with open("Iris.pkl", "rb") as f:
    print(pickle.load(f))
