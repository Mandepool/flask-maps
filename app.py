from flask import Flask, render_template_string, redirect
import os

app = Flask(__name__)

# Кнопки и маршруты
ROUTES = {
    "r1": ("Дом → Работа", "https://maps.google.com/?saddr=Дом&daddr=Работа"),
    "r2": ("Работа → Магазин", "https://maps.google.com/?saddr=Работа&daddr=Магазин"),
    "r3": ("Дом → Спортзал", "https://maps.google.com/?saddr=Дом&daddr=Спортзал")
}

@app.route('/')
def index():
    html = """
    <h2>Выберите маршрут:</h2>
    {% for key, (name, url) in routes.items() %}
        <form action="/go/{{ key }}" method="get">
            <button type="submit">{{ name }}</button>
        </form>
    {% endfor %}
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