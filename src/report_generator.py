def save_recommendation_report(user_id, recommendations, file_path):
    with open(file_path, mode="w") as file:
        file.write("E-Commerce Product Recommendation Report\n")
        file.write("=======================================\n\n")
        file.write(f"User ID: {user_id}\n\n")

        if not recommendations:
            file.write("No recommendations found.\n")
            return

        file.write("Recommended Products:\n\n")

        for index, item in enumerate(recommendations, start=1):
            product, score = item
            file.write(
                f"{index}. {product.name} | "
                f"Category: {product.category} | "
                f"Brand: {product.brand} | "
                f"Price: Rs.{product.price} | "
                f"Score: {score}\n"
            )

        file.write("\nDSA Concepts Used:\n")
        file.write("- Dictionary / HashMap\n")
        file.write("- List\n")
        file.write("- Set\n")
        file.write("- Sorting\n")
        file.write("- Heap / Priority Queue\n")
        file.write("- Similarity Scoring\n")