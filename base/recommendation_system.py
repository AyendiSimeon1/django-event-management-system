# recommendation_system.py

from surprise import Dataset, Reader
from surprise import SVD
from surprise.model_selection import train_test_split
from surprise import accuracy
import pandas as pd

class EventRecommender:
    def __init__(self, user_event_data):
        reader = Reader(rating_scale=(0, 1))
        data = Dataset.load_from_df(user_event_data, reader)
        trainset, testset = train_test_split(data, test_size=0.2)

        # Use the SVD algorithm for collaborative filtering
        self.model = SVD()
        self.model.fit(trainset)

        # Evaluate the model
        predictions = self.model.test(testset)
        accuracy.rmse(predictions)

    def recommend_events(self, user_id, num_recommendations=5):
        all_event_ids = self.model.trainset._raw2inner_id_items.keys()
        user_event_ratings = [(event_id, self.model.predict(user_id, event_id).est) for event_id in all_event_ids]
        user_event_ratings.sort(key=lambda x: x[1], reverse=True)
        recommended_events = user_event_ratings[:num_recommendations]

        return recommended_events

# Example usage:
# Assume user_event_data is a DataFrame with columns: 'user_id', 'event_id', 'rating' (1 for attended, 0 for not attended).

# user_event_data = pd.DataFrame({
#     'user_id': [1, 1, 2, 2, 3, 3],
#     'event_id': [1, 2, 2, 3, 3, 4],
#     'rating': [1, 1, 1, 1, 1, 1]
# })

# recommender = EventRecommender(user_event_data)
# recommended_events = recommender.recommend_events(user_id=1, num_recommendations=2)
# print("Recommended Events:", recommended_events)
