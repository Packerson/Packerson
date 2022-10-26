from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def write_code():
    return f"""
    <form action="/" method="POST">
    Hello, write your postal code:
    <label>
        <input type="text" name="post_code"
    </label>
    <label>
        <button type="submit" > CHECK </button>
    </label>
    </form>
    """


@app.route('/', methods=['POST'])
def check_code():
    post_code = request.form["post_code"]
    try:
        first, second = post_code.split("-")
        if (first.isdigit() and second.isdigit() == True) and (len(first) == 2 and len(second) == 3):
            return f"""
                    Post code is correct"""
        else:
            return f""" Wrong post code. Please write it again""" + write_code()
    except ValueError:
        return f""" Hmm, something went wrong. Please write it again""" + write_code()


if __name__ == "__main__":
    app.run(debug=True, port=4000)
