import json

def load_data(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []

def save_data(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def create_new_entry(first_name, last_name, telephone, city, state, filename):
    data = load_data(filename)
    new_entry = {
        "first_name": first_name,
        "last_name": last_name,
        "telephone": telephone,
        "city": city,
        "state": state
    }
    data.append(new_entry)
    save_data(filename, data)


create_new_entry("John", "Doe", "111-222-3333", "Seattle", "WA", "phonebook.json")
create_new_entry("Jane", "Smith", "444-555-6666", "San Francisco", "CA", "phonebook.json")


updated_data = load_data("phonebook.json")
print(json.dumps(updated_data))

def search_by_first_name(query, filename):
    data = load_data(filename)
    results = [entry for entry in data if entry['first_name'].lower() == query.lower()]
    return results

def search_by_last_name(query, filename):
    data = load_data(filename)
    results = [entry for entry in data if entry['last_name'].lower() == query.lower()]
    return results

def search_by_full_name(query, filename):
    data = load_data(filename)
    results = [entry for entry in data if f"{entry['first_name']} {entry['last_name']}".lower() == query.lower()]
    return results

def search_by_telephone(query, filename):
    data = load_data(filename)
    results = [entry for entry in data if entry['telephone'] == query]
    return results

def search_by_city_or_state(query, filename):
    data = load_data(filename)
    results = [entry for entry in data if entry['city'].lower() == query.lower() or entry['state'].lower() == query.lower()]
    return results

def delete_record_by_telephone(query, filename):
    data = load_data(filename)
    data = [entry for entry in data if entry['telephone'] != query]
    save_data(filename, data)