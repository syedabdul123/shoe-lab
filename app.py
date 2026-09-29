from flask import Flask, render_template

app = Flask(__name__)

PRODUCTS = [
    {
        "id": 1,
        "name": "Velocity Runner",
        "category": "Running",
        "price": 128,
        "color": "Volt / White",
        "image": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=900&q=85",
        "label": "BESTSELLER",
        "tone": "coral",
    },
    {
        "id": 2,
        "name": "Court Classic",
        "category": "Casual",
        "price": 94,
        "color": "Cloud / Gum",
        "image": "https://images.unsplash.com/photo-1600185365483-26d7a4cc7519?auto=format&fit=crop&w=900&q=85",
        "label": "NEW",
        "tone": "mint",
    },
    {
        "id": 3,
        "name": "Trail Form 02",
        "category": "Outdoor",
        "price": 156,
        "color": "Stone / Moss",
        "image": "https://images.unsplash.com/photo-1551488831-00ddcb6c6bd3?auto=format&fit=crop&w=900&q=85",
        "label": "",
        "tone": "sand",
    },
    {
        "id": 4,
        "name": "Everyday Canvas",
        "category": "Casual",
        "price": 76,
        "color": "Ink / Natural",
        "image": "https://images.unsplash.com/photo-1525966222134-fcfa99b8ae77?auto=format&fit=crop&w=900&q=85",
        "label": "JUST IN",
        "tone": "blue",
    },
    {
        "id": 5,
        "name": "Pace Pro Knit",
        "category": "Running",
        "price": 142,
        "color": "Ice / Cobalt",
        "image": "https://images.unsplash.com/photo-1552346154-21d32810aba3?auto=format&fit=crop&w=900&q=85",
        "label": "",
        "tone": "lilac",
    },
    {
        "id": 6,
        "name": "Weekend High",
        "category": "Casual",
        "price": 112,
        "color": "Chalk / Cherry",
        "image": "https://images.unsplash.com/photo-1495555961986-6d4c1ecb7be3?auto=format&fit=crop&w=900&q=85",
        "label": "LOW STOCK",
        "tone": "yellow",
    },
]


@app.get("/")
def home():
    return render_template("index.html", products=PRODUCTS)


if __name__ == "__main__":
    app.run(debug=True)