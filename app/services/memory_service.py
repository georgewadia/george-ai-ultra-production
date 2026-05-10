memory_store = {}

def save_memory(user_id, text):
    if user_id not in memory_store:
        memory_store[user_id] = []

    memory_store[user_id].append(text)

def get_memory(user_id):
    return memory_store.get(user_id, [])