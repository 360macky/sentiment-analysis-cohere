#!/usr/local/bin/python3


import cohere
from cohere.responses.classify import Example
from decouple import config

co = cohere.Client(config('COHERE_API_KEY'))


examples = [
    Example("The order came 5 days early", "positive"),
    Example("The item exceeded my expectations", "positive"),
    Example("I ordered more for my friends", "positive"),
    Example("I would buy this again", "positive"),
    Example("I would recommend this to others", "positive"),
    Example("The package was damaged", "negative"),
    Example("The order is 5 days late", "negative"),
    Example("The order was incorrect", "negative"),
    Example("I want to return my item", "negative"),
    Example("The item\'s material feels low quality", "negative"),
    Example("The product was okay", "neutral"),
    Example("I received five items in total", "neutral"),
    Example("I bought it from the website", "neutral"),
    Example("I used the product this morning", "neutral"),
    Example("The product arrived yesterday", "neutral"),
]

inputs = [
    "My product was delivered on time and it's perfect",
]

response = co.classify(
    model='large',
    inputs=inputs,
    examples=examples,
)

print(response)
