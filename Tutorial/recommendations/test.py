from recommendations_pb2 import BookCategory, RecommendationRequest

request = RecommendationRequest(user_id=1, category=BookCategory.SCIENCE_FICTION)
print(request.max_results)
