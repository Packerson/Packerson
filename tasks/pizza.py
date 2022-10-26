import datetime

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def pizza():
    return pizza_form()


def czas():
    czas_1 = datetime.datetime.now().strftime("%H:%M:%S %d-%m-%Y %A")
    print(czas_1)
    return f"Aktualny czas! {czas_1}"


def pizza_form():
    return czas() + """<br/>
    Podaj składniki pizzy:<br/>
    <form action="/pizza" method="POST">
        <label>Adres dostawy:
            <input type="text" name="address">
        </label><br/>
        <label for="pizza_name">Wybierz rodzaj pizzy:</label>
        <select name="pizza_name">
          <option value="margharitta">Margharitta</option>
          <option value="vege">Vege</option>
          <option value="pepperoni">Pepperoni</option>
          <option value="hawaii">Hawajska</option>
        </select>
        <br/>
        Składniki: <br/>
            <input type="checkbox" name="pizza_topping" value="cheese"> dodatkowy ser <br/>
            <input type="checkbox" name="pizza_topping" value="ham"> szynka <br/>
            <input type="checkbox" name="pizza_topping" value="spinach"> szpinak <br/>
            <input type="checkbox" name="pizza_topping" value="egg"> jajko <br/>
            <input type="checkbox" name="pizza_topping" value="salami"> salami <br/>
            <input type="checkbox" name="pizza_topping" value="garlic"> czosnek <br/>
            <input type="checkbox" name="pizza_topping" value="muschrums"> pieczarki <br/>
            <input type="checkbox" name="pizza_topping" value="broklins"> brokuły <br/>
        <label>
            <button type="submit"> Zamów </button>
        </label>
    </form>
    """


@app.route("/pizza", methods=["POST"])
def add_toppings():
    tops = request.form.getlist("pizza_topping")
    address = request.form['address']
    pizza_name = request.form['pizza_name']
    return f"""
    Pizza: {pizza_name} <br/>
    składniki: {tops} <br/>
    adres: {address} <br/>
    <img src="https://th.bing.com/th/id/OIP.j4-Cqo5FqnlhfIr8v3Fn8QHaJ4?pid=ImgDet&rs=1" style="width:400px;height:400px;"> <br/>
    """ + pizza_form(), czas()


if __name__ == "__main__":
    app.run(debug=True, port=4000)
