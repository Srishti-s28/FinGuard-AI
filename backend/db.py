logs = []

def save_log(query, response):
    logs.append({"query": query, "response": response})

def get_logs():
    return logs