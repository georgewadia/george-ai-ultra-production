crm_store = []

def create_lead(name, phone):
    crm_store.append({
        "name": name,
        "phone": phone
    })

def list_leads():
    return crm_store