from flask import Flask, request

app = Flask(__name__)

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            return False

    return True

@app.route('/')
def home():
    num = request.args.get('number', default=0, type=int)

    if is_prime(num):
        result = f"{num} is a Prime Number"
    else:
        result = f"{num} is NOT a Prime Number"

    return result

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
