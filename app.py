from flask import Flask, render_template_string, redirect
import os

app = Flask(__name__)

# Кнопки и маршруты
ROUTES = {
    "r1": ("Дом → Работа", "https://yandex.ru/maps/36/stavropol/?ll=41.968120%2C45.041440&mode=routes&rtext=45.041731%2C41.962148~45.042827%2C41.964385&rtt=auto&ruri=ymapsbm1%3A%2F%2Fgeo%3Fdata%3DCgg1NzU0MDUwNhJR0KDQvtGB0YHQuNGPLCDQodGC0LDQstGA0L7Qv9C-0LvRjCwg0YPQu9C40YbQsCDQnNC40YXQsNC40LvQsCDQnNC-0YDQvtC30L7QstCwLCA1IgoNPdknQhW7KjRC~ymapsbm1%3A%2F%2Fgeo%3Fdata%3DCgg1NzU0MDQ5MBJE0KDQvtGB0YHQuNGPLCDQodGC0LDQstGA0L7Qv9C-0LvRjCwg0L_Qu9C-0YnQsNC00Ywg0JvQtdC90LjQvdCwLCAz0JAiCg2H2ydCFdsrNEI%2C&z=16.93"),
    "r2": ("Работа → Магазин", "https://maps.google.com/?saddr=Работа&daddr=Магазин"),
    "r3": ("Дом → Спортзал", "https://maps.google.com/?saddr=Дом&daddr=Спортзал")
}

@app.route('/')
def index():
    html = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Маршруты</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 20px;
                background-color: #f4f4f9;
            }
            h2 {
                margin-bottom: 20px;
            }
            .btn {
                display: block;
                width: 100%;
                max-width: 300px;
                margin: 10px auto;
                padding: 15px;
                font-size: 18px;
                font-weight: bold;
                background-color: #007BFF;
                color: white;
                border: none;
                border-radius: 8px;
                cursor: pointer;
                transition: background 0.3s;
            }
            .btn:hover {
                background-color: #0056b3;
            }
        </style>
    </head>
    <body>
        <h2>Выберите маршрут:</h2>
        {% for key, (name, url) in routes.items() %}
            <form action="/go/{{ key }}" method="get">
                <button class="btn" type="submit">{{ name }}</button>
            </form>
        {% endfor %}
    </body>
    </html>
    """
    return render_template_string(html, routes=ROUTES)

@app.route('/go/<route_key>')
def go(route_key):
    route = ROUTES.get(route_key)
    if route:
        return redirect(route[1])
    return "Маршрут не найден", 404


if name == "__main__":
    # Render задаёт PORT через переменные окружения
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)