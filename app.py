from flask import Flask
import random

app = Flask(__name__)


jokes = [
    "Why did the angry function exceed the callstack size? It got into an Argument with itself",
    "Whats the object-oriented way to become wealthy? Inheritance"
]

@app.get("/")
def tell_a_joke():
    joke = random.choice(jokes)
    return f"<p>{joke}</p>"
