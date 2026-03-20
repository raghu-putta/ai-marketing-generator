from fastapi import FastAPI

app = FastAPI()

def article_for(word: str) -> str:
    return "an" if word[:1].lower() in "aeiou" else "a"

@app.get("/")
def home():
    return {"message": "AI Marketing Generator Running"}

@app.post("/generate")
def generate_content(product: str, audience: str, tone: str):
    article = article_for(tone)

    return {
        "content": f"""
1. Facebook Ad:
Boost your routine with {product}! Designed for {audience}, this solution helps you stay ahead with {article} {tone.lower()} experience. Start today and see the difference.

2. Email:
Subject: Transform Your Results with {product}

Hi there,

If you're part of {audience}, {product} is built for you. With {article} {tone.lower()} approach, it helps simplify your goals and improve results faster.

Get started today and take the next step.

Best,
Marketing Team

3. Blog Intro:
In today’s fast-moving digital world, tools like {product} are helping {audience} achieve better results more efficiently. In this article, we explore how {article} {tone.lower()} solution can improve engagement, productivity, and overall performance.
"""
    }