import streamlit as st

from src.data_loader import load_products, load_users, load_interactions, load_ratings
from src.recommender import recommend_products, recommend_by_category
from src.similarity import find_similar_products
from src.report_generator import save_recommendation_report


st.set_page_config(
    page_title="E-Commerce Recommendation Engine",
    page_icon="🛒",
    layout="wide"
)


products = load_products("data/products.csv")
users = load_users("data/users.csv")
interactions = load_interactions("data/interactions.csv")
ratings = load_ratings("data/ratings.csv")


st.title("E-Commerce Product Recommendation Engine")
st.write("A DSA-based recommendation system using HashMap, Sorting, Heap, and Similarity Scoring.")


product_rows = []
for product in products.values():
    product_rows.append({
        "Product ID": product.product_id,
        "Name": product.name,
        "Category": product.category,
        "Brand": product.brand,
        "Price": product.price
    })


st.subheader("Product Dataset")
st.dataframe(product_rows, use_container_width=True)


st.subheader("Personalized Recommendations")

user_options = list(users.keys())
selected_user = st.selectbox("Select User", user_options)
top_n = st.slider("Number of recommendations", 1, 10, 5)

if st.button("Generate Recommendations"):
    recommendations = recommend_products(selected_user, products, interactions, ratings, top_n)

    if not recommendations:
        st.warning("No recommendations found for this user.")
    else:
        recommendation_rows = []

        for product, score in recommendations:
            recommendation_rows.append({
                "Product ID": product.product_id,
                "Name": product.name,
                "Category": product.category,
                "Brand": product.brand,
                "Price": product.price,
                "Score": score
            })

        st.success(f"Top {top_n} recommendations for {selected_user}")
        st.dataframe(recommendation_rows, use_container_width=True)

        save_recommendation_report(
            selected_user,
            recommendations,
            "outputs/recommendations.txt"
        )

        st.info("Recommendation report saved to outputs/recommendations.txt")


st.subheader("Find Similar Products")

product_options = list(products.keys())
selected_product = st.selectbox("Select Product", product_options)
similar_top_n = st.slider("Number of similar products", 1, 10, 5)

if st.button("Find Similar Products"):
    similar_products = find_similar_products(selected_product, products, similar_top_n)

    if not similar_products:
        st.warning("No similar products found.")
    else:
        similar_rows = []

        for product, score in similar_products:
            similar_rows.append({
                "Product ID": product.product_id,
                "Name": product.name,
                "Category": product.category,
                "Brand": product.brand,
                "Price": product.price,
                "Similarity Score": score
            })

        st.success(f"Similar products for {selected_product}")
        st.dataframe(similar_rows, use_container_width=True)


st.subheader("Category-Wise Recommendations")

categories = sorted(list(set(product.category for product in products.values())))
selected_category = st.selectbox("Select Category", categories)
category_top_n = st.slider("Number of category products", 1, 10, 5)

if st.button("Show Category Products"):
    category_products = recommend_by_category(selected_category, products, category_top_n)

    if not category_products:
        st.warning("No products found in this category.")
    else:
        category_rows = []

        for product in category_products:
            category_rows.append({
                "Product ID": product.product_id,
                "Name": product.name,
                "Category": product.category,
                "Brand": product.brand,
                "Price": product.price
            })

        st.success(f"Top products in {selected_category}")
        st.dataframe(category_rows, use_container_width=True)


st.subheader("DSA Concepts Used")

st.write("""
- HashMap / Dictionary for fast product and user lookup
- List for storing products and interactions
- Set for filtering already seen products
- Sorting for ranking category products
- Heap / Priority Queue for top-N recommendation selection
- Similarity scoring for product matching
""")