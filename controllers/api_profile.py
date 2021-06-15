from app import app
from models.profile import Profile
from flask import jsonify, request

PREFIX = "/profile"

@app.route(PREFIX, methods=['POST'])
def create_profile():
    data = request.form.to_dict()

    if 'title' not in data:
        return "Title is required", 400
    title = data["title"]

    if 'twitter' not in data:
        return "Twitter is required", 400
    twitter = data["twitter"]

    profile = Profile(
        title,
        twitter = twitter,
        user_info = data["user_info"] if 'user_info' in data else "",
        image = data["image"] if 'image' in data else "",
        description = data["description"] if 'description' in data else "",
    )

    data = profile.create()

    return jsonify(data)

@app.route(PREFIX, methods=['PUT'])
def update_profile():
    data = request.form.to_dict()

    if 'twitter' not in data:
        return "Twitter is required", 400
    twitter = data["twitter"]

    profile = Profile(
        title = data["title"] if 'title' in data else "",
        twitter = twitter,
        user_info = data["user_info"] if 'user_info' in data else "",
        image = data["image"] if 'image' in data else "",
        description = data["description"] if 'description' in data else "",
    )

    data = profile.update()

    return jsonify(data)

@app.route(PREFIX + '_last', methods=['GET'])
def get_last_profile():
    #username = request.args.get('limit')
    profiles = Profile.get_last()

    return jsonify(profiles)

@app.route(PREFIX + '/<twitter>', methods=['GET'])
def get_profile(twitter):

    profile = Profile.get(twitter)

    return jsonify(profile)

@app.route(PREFIX + '/<twitter>', methods=['DELETE'])
def delete_profile(twitter):

    result = Profile.delete(twitter)

    return jsonify(result)
