from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/rank", methods=["POST"])  # Allow POST requests for this endpoint
def analyze_sentiment():
    post_data = request.json

    platform = post_data.get("session")  # Checking the social media platform

    #deciding on the post to add based on the platform
    if platform.get("platform") == "reddit":
        NEW_POSTS = [
            {
                "id": "n4uq94",
                "url": "https://www.reddit.com/r/Mindfulness/comments/n4uq94/why_are_you_scrolling_are_you_aware_of_your/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button",
            }
        ]
    if platform.get("platform") == "facebook":
        NEW_POSTS = [
            {
                "id": "pfbid02de23RA7aC2oNZsDQ1SjT1f2H6St4gi3fTQy37FS173CjGkpzXcShpBR1CKywcBnql",
                "url": "https://www.facebook.com/NAMI/posts/pfbid02de23RA7aC2oNZsDQ1SjT1f2H6St4gi3fTQy37FS173CjGkpzXcShpBR1CKywcBnql",
            }
        ]
    if platform.get("platform") == "twitter":
        NEW_POSTS = [
            {
                "id": "1250894742285684737",
                "url": "https://twitter.com/NCHPAD/status/1250894742285684737",
            }
        ]
    #word counter
    wc = 0
    #post counter
    pc = 0
    ranked_ids = []
    #adding reminder posts
    for item in post_data.get("items"):
        id = item.get("id")
        type = item.get("type")
        ranked_ids.append(id)
        if "text" in item:
            try:
                words = item["text"].split()
                wc += len(words)
            except AttributeError:
                pass
        if "title" in item:
            try:
                words = item["title"].split()
                wc += len(words)
            except AttributeError:
                pass
        if "comment" in item:
            try:
                words = item["comment"].split()
                wc += len(words)
            except AttributeError:
                pass
        if type == "tweet" or type == "post":
            pc += 1
            if wc >= 180 and pc >=2:
                ranked_ids.append(NEW_POSTS)
                wc=0
                pc=0

    result = {
        "ranked_ids": ranked_ids,
        "new_items": NEW_POSTS,
    }

    return jsonify(result)

@app.route('/')
def hello_world():
    return 'Hello, World!'
