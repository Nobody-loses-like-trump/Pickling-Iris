import pickle
import requests

data = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data").text

list_of_lists = [[y for y in x.split(",")] for x in data.splitlines() if x != ""]

with open("Iris.pkl", "wb") as f:
    pickle.dump(list_of_lists, f)

with open("Iris.pkl", "rb") as f:
    print(pickle.load(f))
