from app.agents.sales_agent import sales_agent
from app.agents.design_agent import design_agent
from app.agents.pricing_agent import pricing_agent
from app.agents.marketing_agent import marketing_agent

def route_message(message: str):
    responses = []

    if "سعر" in message or "تكلفة" in message:
        responses.append(pricing_agent(message))

    if "تصميم" in message or "ديكور" in message:
        responses.append(design_agent(message))

    if "إعلان" in message or "تسويق" in message:
        responses.append(marketing_agent(message))

    responses.append(sales_agent(message))

    return "\n".join(responses)