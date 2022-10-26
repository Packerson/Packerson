from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def start():
    return f"""
    <form action="/" method="POST">
    <h1>Write a number!</h1>
    Hello, write your number: 
    <label>
        <input type="text" name="number">
    </label>
    <label>
            <button type="submit"> Send </button>
    </label>
    </form>
    """


@app.route('/', methods=['POST'])
def calculating():
    try:
        number = int(request.form["number"])
        a = 2 ** number
        b = number ** number
        c = 1
        for i in range(number + 1):
            c = i + c
        c = c-1
        return f"""
            <table border=10>
               <tr>
                  <td>2*n</td><td>{a}</td>
               </tr>
               <tr>
                  <td>n**n</td> <td>{b}</td> 
               </tr>
               <tr>
                  <td>n!</td> <td>{c}</td> 
               </tr>
            </table>
               """
    except ValueError:
        print("You need to type natural number!")
        return f"""
                  <br><br> You need to type a natural number </br></br>
                """


if __name__ == "__main__":
    app.run(debug=True, port=4000)
