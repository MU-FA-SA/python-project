import requests
import pickle
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/"
res = requests.get(url)
with open ("RE.txt","wb") as f:
    res = f.write(res.content)
print(res)


