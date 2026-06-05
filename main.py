from src.data_loader import load_products, load_users, load_interactions, load_ratings
from src.similarity import find_similar_products
from src.recommender import recommend_products, recommend_by_category
from src.report_generator import save_recommendation_report

def show_all_products(products):
    print("\nAll Products:\n")

    for product in products.values():
        print(product)


def show_all_users(users):
    print("\nAll Users:\n")

    for user in users.values():
        print(user)


def show_recommendations(products, interactions, ratings):
    user_id = input("Enter user ID: ")
    top_n = int(input("Enter number of recommendations: "))

    recommendations = recommend_products(user_id, products, interactions, ratings, top_n)

    if not recommendations:
        print("\nNo recommendations found.")
        save_recommendation_report(user_id, recommendations, "outputs/recommendations.txt")
        print("Report saved to outputs/recommendations.txt")
        return

    print(f"\nRecommended products for {user_id}:\n")

    for index, item in enumerate(recommendations, start=1):
        product, score = item
        print(f"{index}. {product.name} | {product.category} | {product.brand} | Rs.{product.price} | Score: {score}")

    save_recommendation_report(user_id, recommendations, "outputs/recommendations.txt")
    print("\nReport saved to outputs/recommendations.txt")

def show_similar_products(products):
    product_id = input("Enter product ID: ")
    top_n = int(input("Enter number of similar products: "))

    similar_products = find_similar_products(product_id, products, top_n)

    if not similar_products:
        print("\nNo similar products found.")
        return

    print(f"\nSimilar products for {product_id}:\n")

    for index, item in enumerate(similar_products, start=1):
        product, score = item
        print(f"{index}. {product.name} | {product.category} | {product.brand} | Rs.{product.price} | Score: {score}")


def show_category_recommendations(products):
    category = input("Enter category: ")
    top_n = int(input("Enter number of products: "))

    category_products = recommend_by_category(category, products, top_n)

    if not category_products:
        print("\nNo products found in this category.")
        return

    print(f"\nTop products in {category} category:\n")

    for index, product in enumerate(category_products, start=1):
        print(f"{index}. {product.name} | {product.brand} | Rs.{product.price}")


def main():
    products = load_products("data/products.csv")
    users = load_users("data/users.csv")
    interactions = load_interactions("data/interactions.csv")
    ratings = load_ratings("data/ratings.csv")

    while True:
        print("\n======================================")
        print(" E-Commerce Product Recommendation Engine")
        print("======================================")
        print("1. Show all products")
        print("2. Show all users")
        print("3. Recommend products for user")
        print("4. Show similar products")
        print("5. Show category-wise products")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_all_products(products)
        elif choice == "2":
            show_all_users(users)
        elif choice == "3":
            show_recommendations(products, interactions, ratings)
        elif choice == "4":
            show_similar_products(products)
        elif choice == "5":
            show_category_recommendations(products)
        elif choice == "6":
            print("\nThank you for using the recommendation engine.")
            break
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()