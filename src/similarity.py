def calculate_similarity(product1, product2):
    score = 0

    if product1.category == product2.category:
        score += 3

    if product1.brand == product2.brand:
        score += 2

    price_difference = abs(product1.price - product2.price)

    if price_difference <= 500:
        score += 2
    elif price_difference <= 1000:
        score += 1

    return score


def find_similar_products(target_product_id, products, top_n=5):
    if target_product_id not in products:
        return []

    target_product = products[target_product_id]
    similar_products = []

    for product_id, product in products.items():
        if product_id == target_product_id:
            continue

        score = calculate_similarity(target_product, product)

        if score > 0:
            similar_products.append((product, score))

    similar_products.sort(key=lambda item: item[1], reverse=True)

    return similar_products[:top_n]