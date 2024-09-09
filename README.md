# priceformatter
format prices


### exemplo de uso no Flask:

```python
from flask import Flask, render_template
from your_module import CurrencyFormatter

app = Flask(__name__)

@app.route('/')
def index():
    # Example products
    produtos = [
        {"nome": "Produto A", "preco": 1500.50, "quantidade": 10},
        {"nome": "Produto B", "preco": 300.25, "quantidade": 5},
        {"nome": "Produto C", "preco": 1200.75, "quantidade": 3}
    ]
    
    # Instantiate the formatter for Real
    real_formatter = CurrencyFormatter('Real')
    
    return render_template('index.html', produtos=produtos, real_formatter=real_formatter)

```

### agora no html:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product List</title>
</head>
<body>
    <h1>Product List</h1>
    <table border="1">
        <thead>
            <tr>
                <th>Product Name</th>
                <th>Price</th>
                <th>Quantity</th>
            </tr>
        </thead>
        <tbody>
            {% for produto in produtos %}
                <tr>
                    <td>{{ produto.nome }}</td>
                    <td>{{ real_formatter.format_currency(produto.preco) }}</td>
                    <td>{{ produto.quantidade }}</td>
                </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>




```
