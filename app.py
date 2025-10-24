
from flask import Flask, render_template_string, redirect

app = Flask(__name__)

# Маршруты: название -> (ссылка, описание)
ROUTES = {
    "Маршрут №1": ("https://mapmagic.app/map?routes=9Kb7dd6", "От общежития №1 (ул. Михаила Морозова 5) до СКФУ корпус №6 (пл. Ленина 3а)"),
    "Маршрут №2": ("https://mapmagic.app/map?routes=6lBNdpV", "От общежития №1 (ул. Михаила Морозова 5) до Театра драмы им. Лермонтова (пл. Ленина 1а)"),
    "Маршрут №3 (с препятствиями)": ("https://mapmagic.app/map?routes=V1BEJM0", "От общежития №1 (ул. Михаила Морозова 5) до Кампус-центра СКФУ (ул. Пушкина 1а)"),
    "Маршрут №3 (без препятствий)": ("https://mapmagic.app/map?routes=0yBOgk6", "От общежития №1 (ул. Михаила Морозова 5) до Кампус-центра СКФУ (ул. Пушкина 1а)"),
    "Маршрут №4": ("https://mapmagic.app/map?routes=6qpNMX0", "От общежития №1 (ул. Михаила Морозова 5) до Андреевского собора (ул. Дзержинского 157)"),
    "Маршрут №5": ("https://mapmagic.app/map?routes=VbMgqb9", "От общежития №1 (ул. Михаила Морозова 5) до торговых точек (Пятёрочка, МКС) на ул. Михаила Морозова 14"),
    "Маршрут №6": ("https://mapmagic.app/map?routes=V1BnXW0", "От кампус-центра СКФУ (ул. Пушкина 1а) до торговых точек (Пятёрочка, Магнит) на ул. Дзержинского 134"),
    "Маршрут №7": ("https://mapmagic.app/map?routes=6jglr79", "От кампус-центра СКФУ до музея-заповедника (ул. Дзержинского 135). Автобусы: 32, 32а, 48; троллейбус: 2"),
    "Маршрут №8": ("https://mapmagic.app/map?routes=9Nv7p89", "От кампус-центра СКФУ до Александровской площади. Автобусы: 32, 32а, 48; троллейбус: 2"),
    "Маршрут №9": ("https://mapmagic.app/map?routes=VB3nyJ0", "От кампус-центра СКФУ до площади Ленина. Автобусы: 32, 32а, 48; троллейбус: 2"),
    "Маршрут №10": ("https://mapmagic.app/map?routes=63AnvDV", "От кампус-центра СКФУ до стадиона «Динамо» (пр. Октябрьской Революции 33)"),
    "Маршрут №11": ("https://mapmagic.app/map?routes=VbMg7P9", "От кампус-центра СКФУ до Парка Культуры и Отдыха Центральный (пр. Октябрьской Революции 22)"),
    "Маршрут №12": ("https://mapmagic.app/map?routes=VQBpAb0", "От кампус-центра СКФУ до СКФУ корпус №8 (ул. Ленина 133б). Автобус №48"),
    "Маршрут №13": ("https://mapmagic.app/map?routes=07q3Ln9", "От кампус-центра СКФУ до ТЦ «Европейский» (пр. Карла Маркса 53). Автобусы: 32, 32а; троллейбус: 2"),
    "Маршрут №14": ("https://mapmagic.app/map?routes=64aKxQ9", "От кампус-центра СКФУ до филармонии (пр. Карла Маркса 61). Автобусы: 32, 32а; троллейбус: 2"),
    "Маршрут №15": ("https://mapmagic.app/map?routes=V1BnAL0", "От общежития №9 (пр. Кулакова 2, корп. 6) до Кампуса-север СКФУ (пр. Кулакова 2)"),
    "Маршрут №16": ("https://mapmagic.app/map?routes=6jglbm9", "От общежития №9 (пр. Кулакова 2, корп. 6) до торговых точек (Пятёрочка, аптека) на ул. Ленина 480/1"),
    "Маршрут №17": ("https://mapmagic.app/map?routes=9Kb71W6", "От общежития №9 (пр. Кулакова 2, корп. 6) до кинотеатра «Салют Юг» (ул. 50 лет ВЛКСМ 1). Автобус №9 (Маршрут предполагает комбинированное передвижение: основную часть пути необходимо преодолеть на маршрутном такси (участок выделен синим цветом), а до ближайшей остановки и от конечной точки маршрута — пройтись пешком)"),
    "Маршрут №18": ("https://mapmagic.app/map?routes=VbMJvX9", "От общежития №9 (пр. Кулакова 2, корп. 6) до Парка Победы (ул. Шпаковская 111к5). Автобус №9 (Маршрут предполагает комбинированное передвижение: основную часть пути необходимо преодолеть на маршрутном такси (участок выделен синим цветом), а до ближайшей остановки и от конечной точки маршрута — пройтись пешком)"),
    "Маршрут №19": ("https://mapmagic.app/map?routes=64aKyB9", "От Кампуса-север СКФУ (пр. Кулакова 2) до храма Сергия Радонежского (пр. Кулакова 2а/1)"),
    "Маршрут №20": ("https://mapmagic.app/map?routes=9DzLPq0", "От общежития №1 (ул. Михаила Морозова 5) до городской клинической поликлиники № 1"),
    "Маршрут №21": ("https://mapmagic.app/map?routes=0XBMKm9", "От кампус Кулакова до соц защиты ул.Ленина 415Б"),
}

@app.route('/')
def index():
    html = """
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Доступный городской маршрут</title>
        <style>
            body {
                background-color: #f0f4f8;
                font-family: "Arial", sans-serif;
                margin: 0;
                padding: 0;
                color: #111;
            }
            header {
                background-color: #ffffff;
                border-bottom: 4px solid #2e4a7d;
                display: flex;
                align-items: center;
                justify-content: space-between;
                padding: 15px 40px;
            }
            header img {
                width: 80px;
                height: auto;
                border-radius: 10px;
            }
            header h1 {
                color: #2e4a7d;
                font-size: 2.2em;
                text-align: center;
                margin: 0;
                flex: 1;
            }
            .container {
                width: 85%;
                max-width: 1000px;
                margin: 40px auto;
            }
            .route-card {
                background-color: #fff;
                border-radius: 12px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.1);
                margin-bottom: 25px;
                padding: 25px;
                border-left: 6px solid #2e4a7d;
            }
            .route-card:hover {
                transform: scale(1.01);
                transition: 0.2s;
                box-shadow: 0 6px 12px rgba(0,0,0,0.15);
            }
            button {
                font-size: 22px;
                padding: 14px 28px;
                background-color: #2e4a7d;
                color: white;
                border: none;
                border-radius: 10px;
                cursor: pointer;
                margin-bottom: 10px;
            }
            button:hover {
                background-color: #4669b1;
            }
            p {
                font-size: 20px;
                color: #222;
                margin: 8px 0 0 0;
            }
            footer {
                background-color: #e8eef5;
                border-top: 4px solid #2e4a7d;
                padding: 30px;
                text-align: center;
                margin-top: 40px;
            }
            .feedback button {
                font-size: 22px;
                padding: 14px 28px;
                background-color: #28a745;
                border: none;
                border-radius: 10px;
                color: white;
                cursor: pointer;
            }
            .feedback button:hover {
                background-color: #218838;
            }
        </style>
    </head>
    <body>
        <header>
            <img src="{{ url_for('static', filename='photo_2025-10-23_18-18-24.jpg') }}" Логотип слева">
            <h1>Доступный городской маршрут</h1>
            <img src="{{ url_for('static', filename='photo_2025-10-24_17-04-27.jpg') }}"Логотип справа">
        </header>

        <div class="container">
            {% for title, (url, desc) in routes.items() %}
                <div class="route-card">
                    <form action="{{ url }}" method="get" target="_blank">
    <button type="submit">{{ title }}</button>
                        </form>
                        <p>{{ desc }}</p>
                    </div>
                {% endfor %}
            </div>

            <footer>
                <p>Если вы хотите оставить отзыв, заполните форму ниже:</p>
                <div class="feedback">
                    <form action="https://docs.google.com/forms/d/e/1FAIpQLSe6HXh596_Ct3lPN4t5_mpEAUzOgTVoX-ZfmcReMg-P-eOQ1g/viewform?usp=header" target="_blank">
                        <button type="submit">Открыть Google Форму</button>
                    </form>
                </div>
            </footer>
        </body>
        </html>
        """
    return render_template_string(html, routes=ROUTES)


if __name__ == "__main__":
    app.run(debug=True)