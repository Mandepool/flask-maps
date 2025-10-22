
from flask import Flask, render_template_string, redirect

app = Flask(__name__)

# Маршруты: название -> (ссылка, описание)
ROUTES = {
    "Маршрут №1": ("#", "От общежития №1 (ул. Михаила Морозова 5) до СКФУ корпус №6 (пл. Ленина 3а)"),
    "Маршрут №2": ("#", "От общежития №1 (ул. Михаила Морозова 5) до Театра драмы им. Лермонтова (пл. Ленина 1а)"),
    "Маршрут №3 (с препятствиями)": ("#", "От общежития №1 (ул. Михаила Морозова 5) до Кампус-центра СКФУ (ул. Пушкина 1а)"),
    "Маршрут №3 (без препятствий)": ("#", "От общежития №1 (ул. Михаила Морозова 5) до Кампус-центра СКФУ (ул. Пушкина 1а)"),
    "Маршрут №4": ("#", "От общежития №1 (ул. Михаила Морозова 5) до Андреевского собора (ул. Дзержинского 157)"),
    "Маршрут №5": ("#", "От общежития №1 (ул. Михаила Морозова 5) до торговых точек (Пятёрочка, МКС) на ул. Михаила Морозова 14"),
    "Маршрут №6": ("#", "От кампус-центра СКФУ (ул. Пушкина 1а) до торговых точек (Пятёрочка, Магнит) на ул. Дзержинского 134"),
    "Маршрут №7": ("#", "От кампус-центра СКФУ до музея-заповедника (ул. Дзержинского 135). Автобусы: 32, 32а, 48; троллейбус: 2"),
    "Маршрут №8": ("#", "От кампус-центра СКФУ до Александровской площади. Автобусы: 32, 32а, 48; троллейбус: 2"),
    "Маршрут №9": ("#", "От кампус-центра СКФУ до площади Ленина. Автобусы: 32, 32а, 48; троллейбус: 2"),
    "Маршрут №10": ("#", "От кампус-центра СКФУ до стадиона «Динамо» (пр. Октябрьской Революции 33)"),
    "Маршрут №11": ("#", "От кампус-центра СКФУ до Парка Культуры и Отдыха Центральный (пр. Октябрьской Революции 22)"),
    "Маршрут №12": ("#", "От кампус-центра СКФУ до СКФУ корпус №8 (ул. Ленина 133б). Автобус №48"),
    "Маршрут №13": ("#", "От кампус-центра СКФУ до ТЦ «Европейский» (пр. Карла Маркса 53). Автобусы: 32, 32а; троллейбус: 2"),
    "Маршрут №14": ("#", "От кампус-центра СКФУ до филармонии (пр. Карла Маркса 61). Автобусы: 32, 32а; троллейбус: 2"),
    "Маршрут №15": ("#", "От общежития №9 (пр. Кулакова 2, корп. 6) до Кампуса-север СКФУ (пр. Кулакова 2)"),
    "Маршрут №16": ("#", "От общежития №9 (пр. Кулакова 2, корп. 6) до торговых точек (Пятёрочка, аптека) на ул. Ленина 480/1"),
    "Маршрут №17": ("#", "От общежития №9 (пр. Кулакова 2, корп. 6) до остановки «СтавНИИГиМ» (ул. Западный Обход)"),
    "Маршрут №18": ("#", "От общежития №9 (пр. Кулакова 2, корп. 6) до кинотеатра «Салют Юг» (ул. 50 лет ВЛКСМ 1). Автобус №9"),
    "Маршрут №19": ("#", "От общежития №9 (пр. Кулакова 2, корп. 6) до Парка Победы (ул. Шпаковская 111к5). Автобус №9"),
    "Маршрут №20": ("#", "От Кампуса-север СКФУ (пр. Кулакова 2) до храма Сергия Радонежского (пр. Кулакова 2а/1)")
}

@app.route('/')
def index():
    html = """
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Маршруты СКФУ</title>
        <style>
            body {
                background-color: #f9f9f9;
                color: #000;
                font-family: Arial, sans-serif;
                font-size: 20px;
                line-height: 1.6;
                padding: 40px;
                transition: all 0.3s ease;
            }
            h1 {
                font-size: 36px;
                text-align: center;
                margin-bottom: 30px;
            }
            .route {
                margin: 25px 0;
                padding: 25px;
                background-color: #ffffff;
                border-left: 8px solid #007BFF;
                border-radius: 10px;
                box-shadow: 0 0 6px #ccc;
            }
            .route button {
                display: block;
                background-color: #000;
                color: #fff;
                border: none;
                padding: 18px 28px;
                font-size: 22px;
                border-radius: 8px;
                cursor: pointer;
                margin: 0 auto;
            }
            .route button:hover {
                background-color: #333;
            }
            .route p {
                text-align: center;
                margin-top: 15px;
                font-size: 20px;
                color: #222;
            }

/* --- Кнопка переключения режима --- */
            #vision-btn {
                position: fixed;
                top: 20px;
                right: 20px;
                background-color: #007BFF;
                color: white;
                border: none;
                padding: 12px 22px;
                font-size: 18px;
                border-radius: 8px;
                cursor: pointer;
            }
            #vision-btn:hover {
                background-color: #0056b3;
            }

            /* --- Стили для слабовидящих --- */
            body.high-contrast {
                background-color: #000;
                color: #FFD700;
                font-size: 28px;
            }
            body.high-contrast .route {
                background-color: #111;
                border-left: 8px solid #FFD700;
                box-shadow: 0 0 10px #FFD700;
            }
            body.high-contrast .route button {
                background-color: #FFD700;
                color: #000;
                font-size: 28px;
            }
            body.high-contrast .route p {
                color: #FFD700;
                font-size: 26px;
            }
        </style>
    </head>
    <body>
        <button id="vision-btn" onclick="toggleVision()">👁 Режим для слабовидящих</button>
        <h1>Выберите маршрут</h1>

        {% for name, (url, desc) in routes.items() %}
            <div class="route">
                <form action="{{ url }}" method="get">
                    <button type="submit">{{ name }}</button>
                </form>
                <p>{{ desc }}</p>
            </div>
        {% endfor %}

        <script>
            // Сохраняем состояние режима
            if (localStorage.getItem('visionMode') === 'on') {
                document.body.classList.add('high-contrast');
            }

            function toggleVision() {
                document.body.classList.toggle('high-contrast');
                const isOn = document.body.classList.contains('high-contrast');
                localStorage.setItem('visionMode', isOn ? 'on' : 'off');
            }
        </script>
    </body>
    </html>
    """
    return render_template_string(html, routes=ROUTES)

@app.route('/go/<route>')
def go(route):
    url = ROUTES.get(route)
    if url:
        return redirect(url[0])
    return "Маршрут не найден", 404

if __name__ == "__main__":
    app.run(debug=True)