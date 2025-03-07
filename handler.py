import json
from recommendation import get_recommendations

def recommend(event, context):
    user_id = int(event["queryStringParameters"]["user_id"])
    recommendations = get_recommendations(user_id)
    return {
        "statusCode": 200,
        "body": json.dumps({"user_id": user_id, "recommendations": recommendations})
    }
}
