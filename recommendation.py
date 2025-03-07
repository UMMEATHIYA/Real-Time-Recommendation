from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split
import pandas as pd

data_dict = {"user_id": [1, 2, 3, 4, 5], "item_id": [101, 102, 103, 104, 105], "rating": [5, 4, 3, 5, 4]}
df = pd.DataFrame(data_dict)

reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(df[["user_id", "item_id", "rating"]], reader)
trainset, testset = train_test_split(data, test_size=0.2)

model = SVD()
model.fit(trainset)

def get_recommendations(user_id, num_recommendations=5):
    items = df["item_id"].unique()
    predictions = [(item, model.predict(user_id, item).est) for item in items]
    predictions.sort(key=lambda x: x[1], reverse=True)
    return [item for item, _ in predictions[:num_recommendations]]

# Example usage
print(get_recommendations(1))
