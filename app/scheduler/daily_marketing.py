from apscheduler.schedulers.blocking import (
    BlockingScheduler
)

from app.agents.marketing_agent import (
    marketing_agent
)

from app.services.facebook_poster import (
    post_to_facebook
)


scheduler = BlockingScheduler()


def daily_post():

    print("Generating AI Post...")

    post = marketing_agent(
        "منشور تسويقي احترافي عن الجبس بورد"
    )

    print(post)

    print("Posting To Facebook...")

    result = post_to_facebook(post)

    print(result)


scheduler.add_job(
    daily_post,
    "interval",
    hours=24
)

print("AI Marketing Scheduler Started...")


daily_post()

scheduler.start()