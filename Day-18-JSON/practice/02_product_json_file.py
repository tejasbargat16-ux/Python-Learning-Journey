import json

product = {
    "name": "Keyboard",
    "price": 800,
    "quantity": 2
}

# Save product data
with open("product.json", "w", encoding="utf-8") as file:
    json.dump(product, file, indent=4)

print("Product saved successfully!")

# Read product data
with open("product.json", "r", encoding="utf-8") as file:
    saved_product = json.load(file)

print("\nProduct Details")
print("Name:", saved_product["name"])
print("Price: ₹", saved_product["price"])
print("Quantity:", saved_product["quantity"])
print("Total: ₹", saved_product["price"] * saved_product["quantity"])
