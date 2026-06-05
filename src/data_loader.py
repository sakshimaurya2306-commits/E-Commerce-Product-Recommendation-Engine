import csv
from src.models import Product, User


def load_products(file_path):
    products = {}

    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            product = Product(
                row["product_id"],
                row["name"],
                row["category"],
                row["brand"],
                row["price"]
            )

            products[row["product_id"]] = product

    return products


def load_users(file_path):
    users = {}

    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            user = User(row["user_id"], row["name"])
            users[row["user_id"]] = user

    return users


def load_interactions(file_path):
    interactions = {}

    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            user_id = row["user_id"]
            product_id = row["product_id"]
            event = row["event"]

            if user_id not in interactions:
                interactions[user_id] = []

            interactions[user_id].append({
                "product_id": product_id,
                "event": event
            })

    return interactions


def load_ratings(file_path):
    ratings = {}

    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            user_id = row["user_id"]
            product_id = row["product_id"]
            rating = float(row["rating"])

            ratings[(user_id, product_id)] = rating

    return ratings