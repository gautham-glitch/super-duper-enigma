import pandas as pd
from sklearn.preprocessing import StandardScaler

# Representing the data as a list of dictionaries
data = [
    {"Gender": "F", "Roll No": 1,  "Books Read per Month": 3},
    {"Gender": "F", "Roll No": 2,  "Books Read per Month": 2},
    {"Gender": "F", "Roll No": 3,  "Books Read per Month": 2},
    {"Gender": "M", "Roll No": 4,  "Books Read per Month": 2},
    {"Gender": "M", "Roll No": 5,  "Books Read per Month": 5},
    {"Gender": "F", "Roll No": 6,  "Books Read per Month": 3},
    {"Gender": "F", "Roll No": 7,  "Books Read per Month": 5},
    {"Gender": "F", "Roll No": 8,  "Books Read per Month": 15},
    {"Gender": "M", "Roll No": 9,  "Books Read per Month": 5},
    {"Gender": "F", "Roll No": 10, "Books Read per Month": 1},
    {"Gender": "M", "Roll No": 11, "Books Read per Month": 2},
    {"Gender": "M", "Roll No": 12, "Books Read per Month": 7},
    {"Gender": "M", "Roll No": 13, "Books Read per Month": 10},
    {"Gender": "F", "Roll No": 14, "Books Read per Month": 4},
    {"Gender": "M", "Roll No": 15, "Books Read per Month": 5},
    {"Gender": "F", "Roll No": 16, "Books Read per Month": 1},
    {"Gender": "F", "Roll No": 17, "Books Read per Month": 1},
    {"Gender": "M", "Roll No": 18, "Books Read per Month": 2},
    {"Gender": "M", "Roll No": 19, "Books Read per Month": 5},
    {"Gender": "M", "Roll No": 20, "Books Read per Month": 15},
    {"Gender": "F", "Roll No": 21, "Books Read per Month": 1},
    {"Gender": "M", "Roll No": 22, "Books Read per Month": 15},
    {"Gender": "M", "Roll No": 23, "Books Read per Month": 13},
    {"Gender": "F", "Roll No": 24, "Books Read per Month": 5},
    {"Gender": "F", "Roll No": 25, "Books Read per Month": 4},
    {"Gender": "M", "Roll No": 26, "Books Read per Month": 5},
    {"Gender": "F", "Roll No": 27, "Books Read per Month": 0},
    {"Gender": "M", "Roll No": 28, "Books Read per Month": 2},
    {"Gender": "F", "Roll No": 29, "Books Read per Month": 2},
    {"Gender": "F", "Roll No": 30, "Books Read per Month": 4},
    {"Gender": "M", "Roll No": 31, "Books Read per Month": 50},
    {"Gender": "M", "Roll No": 32, "Books Read per Month": 3},
]

# Creating a DataFrame
df = pd.DataFrame(data)
df["Gender"] = df["Gender"].map({"F": 0, "M": 1})

# Display the DataFrame

#top_readers = df.nlargest(32, 'Books Read per Month')
#print(top_readers)
#print("\n")
print( df["Books Read per Month"].corr(df["Gender"]))

