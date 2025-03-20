from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Dictionary of Bihar facts
bihar_facts = {
    "nalanda university": "Nalanda University, established in the 5th century, was one of the world's first residential universities.",
    "bihar capital": "The capital of Bihar is Patna, one of the oldest continuously inhabited cities in the world.",
    "famous food": "Bihar is famous for Litti Chokha, Thekua, and Khaja.",
    "chhath puja": "Chhath Puja is a major festival in Bihar, dedicated to the Sun God.",
    "maurya empire": "The Maurya Empire, founded by Chandragupta Maurya, had its roots in Bihar."
}

def get_response(query):
    """Function to get response based on query"""
    response = "Sorry, I don't have information on that."
    for key in bihar_facts:
        if key in query.lower():
            response = bihar_facts[key]
            break
    return response

@app.route("/voice-assistant", methods=["POST"])
def voice_assistant():
    """API endpoint to receive user queries and return responses"""
    data = request.get_json()
    
    if not data or "query" not in data:
        return jsonify({"reply": "Invalid request"}), 400  # Handle missing query
    
    user_query = data["query"].lower()
    response = get_response(user_query)
    
    print(f"User Query: {user_query} | Response: {response}")  # Debugging log
    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)
