import React, { useState } from "react";

function App() {
    const [userId, setUserId] = useState("");
    const [recommendations, setRecommendations] = useState([]);

    const fetchRecommendations = async () => {
        const response = await fetch(`https://your-api-endpoint/recommend?user_id=${userId}`);
        const data = await response.json();
        setRecommendations(data.recommendations);
    };

    return (
        <div>
            <h1>Recommendation Engine</h1>
            <input
                type="number"
                value={userId}
                onChange={(e) => setUserId(e.target.value)}
                placeholder="Enter User ID"
            />
            <button onClick={fetchRecommendations}>Get Recommendations</button>
            <ul>
                {recommendations.map((item) => (
                    <li key={item}>Item {item}</li>
                ))}
            </ul>
        </div>
    );
}

export default App;
