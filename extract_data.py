import requests
import pandas as pd

response = requests.get("https://jsonplaceholder.typicode.com/users")
data = requests.json()
df = pd.DataFrame(data)
df = df[["id", "name"]]
print(df)