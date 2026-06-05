import heapq
from src.similarity import calculate_similarity


EVENT_WEIGHTS = {
    "view": 1,
    "cart": 3,
    "purchase": 5
}


def get_user_seen_products(user_id, interactions):
    seen_products = set()

    for interaction in interactions.get(user_id, []):
        seen_products.add(interaction["product_id"])

    return seen_products


def recommend_products(user_id, products, interactions, ratings, top_n=5):
    if user_id not in interactions:
        return []

    user_history = interactions[user_id]
    seen_products = get_user_seen_products(user_id, interactions)

    recommendation_scores = {}

    for interaction in user_history:
        history_product_id = interaction["product_id"]
        event = interaction["event"]

        if history_product_id not in products:
            continue

        history_product = products[history_product_id]
        event_weight = EVENT_WEIGHTS.get(event, 1)

        for candidate_id, candidate_product in products.items():
            if candidate_id in seen_products:
                continue

            similarity_score = calculate_similarity(history_product, candidate_product)

            if similarity_score == 0:
                continue

            final_score = similarity_score * event_weight

            rating_key = (user_id, history_product_id)
            if rating_key in ratings:
                final_score += ratings[rating_key]

            if candidate_id not in recommendation_scores:
                recommendation_scores[candidate_id] = 0

            recommendation_scores[candidate_id] += final_score

    top_items = []

    for product_id, score in recommendation_scores.items():
        heapq.heappush(top_items, (-score, product_id))

    recommendations = []

    while top_items and len(recommendations) < top_n:
        negative_score, product_id = heapq.heappop(top_items)
        recommendations.append((products[product_id], -negative_score))

    return recommendations


def recommend_by_category(category, products, top_n=5):
    category_products = []

    for product in products.values():
        if product.category.lower() == category.lower():
            category_products.append(product)

    category_products.sort(key=lambda product: product.price)

    return category_products[:top_n]