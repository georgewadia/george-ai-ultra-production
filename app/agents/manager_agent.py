from app.agents.sales_agent import sales_agent
from app.agents.design_agent import design_agent
from app.agents.pricing_agent import pricing_agent
from app.agents.marketing_agent import marketing_agent


def route_message(user_id: str, message: str):

    responses = []

    # Agent التسعير
    if "سعر" in message or "تكلفة" in message:

        responses.append(
            pricing_agent(message)
        )

    # Agent التصميم
    if "تصميم" in message or "ديكور" in message:

        responses.append(
            design_agent(message)
        )

    # Agent التسويق
    if "إعلان" in message or "تسويق" in message:

        responses.append(
            marketing_agent(message)
        )

    # Agent المبيعات الرئيسي + Memory
    responses.append(
        sales_agent(user_id, message)
    )

    return "\n".join(responses)