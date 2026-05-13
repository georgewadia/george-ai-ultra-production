from app.agents.marketing_agent import marketing_agent

from app.services.facebook_poster import (
    post_to_facebook
)

post = marketing_agent(
    "ديكورات جبس بورد مودرن"
)

print("Generated Post:\n")

print(post)

print("\nPosting To Facebook...\n")

result = post_to_facebook(post)

print(result)