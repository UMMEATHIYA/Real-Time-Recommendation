from flask import Flask, request, jsonify
from recommendation import get_recommendations

app = Flask(__name__)

@app.route("/recommend", methods=["GET"])
def recommend():
    user_id = int(request.args.get("user_id"))
    recommendations = get_recommendations(user_id)
    return jsonify({"user_id": user_id, "recommendations": recommendations})

if __name__ == "__main__":
    app.run(debug=True)
