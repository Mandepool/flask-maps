
from flask import Flask, render_template_string, redirect

app = Flask(__name__)

# Маршруты: название -> (ссылка, описание)
ROUTES = {
    "Маршрут №1": ("https://mapmagic.app/map?routes=9Kb7dd6", "От общежития №1 (ул. Михаила Морозова 5) до СКФУ корпус №6 (пл. Ленина 3а). Особенности маршрута: Удобный пандус и тактильные ступени при входе в 6 корпус"),
    "Маршрут №2": ("https://mapmagic.app/map?routes=6lBNdpV", "От общежития №1 (ул. Михаила Морозова 5) до Театра драмы им. Лермонтова (пл. Ленина 1а)"),
    "Маршрут №3 (с препятствиями)": ("https://mapmagic.app/map?routes=V1BEJM0", "От общежития №1 (ул. Михаила Морозова 5) до Кампус-центра СКФУ (ул. Пушкина 1а)"),
    "Маршрут №3 (без препятствий)": ("https://mapmagic.app/map?routes=0yBOgk6", "От общежития №1 (ул. Михаила Морозова 5) до Кампус-центра СКФУ (ул. Пушкина 1а). Особенности маршрута: Небольшие перепады высоты, ступеньки и пандус посередине пути"),
    "Маршрут №4": ("https://mapmagic.app/map?routes=6qpNMX0", "От общежития №1 (ул. Михаила Морозова 5) до Андреевского собора (ул. Дзержинского 157). Особенности маршрута: Маленькие перепады высоты, ступеньки и пандус посередине пути"),
    "Маршрут №5": ("https://mapmagic.app/map?routes=VbMgqb9", "От общежития №1 (ул. Михаила Морозова 5) до торговых точек (Пятёрочка, МКС) на (ул. Михаила Морозова 14)"),
    "Маршрут №6": ("https://mapmagic.app/map?routes=V1BnXW0", "От кампус-центра СКФУ (ул. Пушкина 1а) до торговых точек (Пятёрочка, Магнит) на (ул. Дзержинского 134). Особенности маршрута: Некрупные перепады высоты, ступеньки, а на входе в торговые объекты оборудованы пандусом"),
    "Маршрут №7": ("https://mapmagic.app/map?routes=6jglr79", "От кампус-центра СКФУ до музея-заповедника (ул. Дзержинского 135). Автобусы: 32, 32а, 48; троллейбус: 2"),
    "Маршрут №8": ("https://mapmagic.app/map?routes=9Nv7p89", "От кампус-центра СКФУ до Александровской площади. Автобусы: 32, 32а, 48; троллейбус: 2"),
    "Маршрут №9": ("https://mapmagic.app/map?routes=VB3nyJ0", "От кампус-центра СКФУ до площади Ленина. Автобусы: 32, 32а, 48; троллейбус: 2"),
    "Маршрут №10": ("https://mapmagic.app/map?routes=63AnvDV", "От кампус-центра СКФУ до стадиона «Динамо» (пр. Октябрьской Революции 33)"),
    "Маршрут №11": ("https://mapmagic.app/map?routes=VbMg7P9", "От кампус-центра СКФУ до Парка Культуры и Отдыха Центральный (пр. Октябрьской Революции 22). Особенности маршрута: Есть перепады высоты и небольшие ступени"),
    "Маршрут №12": ("https://mapmagic.app/map?routes=VQBpAb0", "От кампус-центра СКФУ до СКФУ корпус №8 (ул. Ленина 133б). Автобус №48. Особенности маршрута: Перемены высоты, ступеньки, а в 8 корпусе предусмотрены ступеньки с тактильным покрытием и подъемник для инвалидов-колясочников"),
    "Маршрут №13": ("https://mapmagic.app/map?routes=07q3Ln9", "От кампус-центра СКФУ до ТЦ «Европейский» (пр. Карла Маркса 53). Автобусы: 32, 32а; троллейбус: 2. Особенности маршрута: Различия в высоте, наличие пандусов, а при входе в ТЦ «Европейский»  имеются маленькие ступеньки и пандус"),
    "Маршрут №14": ("https://mapmagic.app/map?routes=64aKxQ9", "От кампус-центра СКФУ до филармонии (пр. Карла Маркса 61). Автобусы: 32, 32а; троллейбус: 2. Особенности маршрута: Встречаются перепады высоты, ступеньки и пандусы, при входе в филармонию присутствуют тактильные ступени и пандус"),
    "Маршрут №15": ("https://mapmagic.app/map?routes=V1BnAL0", "От общежития №9 (пр. Кулакова 2, корп. 6) до Кампуса-север СКФУ (пр. Кулакова 2)"),
    "Маршрут №16": ("https://mapmagic.app/map?routes=6jglbm9", "От общежития №9 (пр. Кулакова 2, корп. 6) до торговых точек (Пятёрочка, аптека) на (ул. Ленина 480/1). Особенности маршрута: При входе в торговую точку имеются ступеньки и пандус"),
    "Маршрут №17": ("https://mapmagic.app/map?routes=9Kb71W6", "От общежития №9 (пр. Кулакова 2, корп. 6) до кинотеатра «Салют Юг» (ул. 50 лет ВЛКСМ 1). Автобус №9 (Маршрут предполагает комбинированное передвижение: основную часть пути необходимо преодолеть на маршрутном такси (участок выделен синим цветом), а до ближайшей остановки и от конечной точки маршрута — пройтись пешком). Особенности маршрута: Могут встретиться перепады высоты и ступеньки"),
    "Маршрут №18": ("https://mapmagic.app/map?routes=VbMJvX9", "От общежития №9 (пр. Кулакова 2, корп. 6) до Парка Победы (ул. Шпаковская 111к5). Автобус №9 (Маршрут предполагает комбинированное передвижение: основную часть пути необходимо преодолеть на маршрутном такси (участок выделен синим цветом), а до ближайшей остановки и от конечной точки маршрута — пройтись пешком). Особенности маршрута: Возможны перепады высоты и ступеньки"),
    "Маршрут №19": ("https://mapmagic.app/map?routes=64aKyB9", "От Кампуса-север СКФУ (пр. Кулакова 2) до храма Сергия Радонежского (пр. Кулакова 2а/1)"),
    "Маршрут №20": ("https://mapmagic.app/map?routes=9DzLPq0", "От общежития №1 (ул. Михаила Морозова 5) до городской клинической поликлиники № 1. Особенности маршрута: Возникают перепады высоты и ступеньки, на входе в поликлинику есть пандус"),
    "Маршрут №21": ("https://mapmagic.app/map?routes=0XBMKm9", "От Кампуса-север СКФУ (пр. Кулакова 2) до социальной защиты (ул. Ленина 415Б). Особенности маршрута: Появляются перепады высоты и ступеньки, на входе в здание предусмотрен пандус"),
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
                font-family: Arial, sans-serif;
                font-size: 20px;
                color: #111;
                line-height: 1.6;
                margin: 0;
                padding: 0;
                transition: background-color 0.3s, color 0.3s;
            }
            h1.header-with-logos {
                display: flex;
                align-items: center;
                justify-content: center;
                background-color: #003366;
                color: white;
                margin: 0;
                padding: 20px 0;
                gap: 20px;
            }
            h1.header-with-logos .logo {
                height: 50px;
                width: auto;
            }
            .container {
                width: 85%;
                max-width: 1000px;
                margin: 30px auto 60px;
            }
            .route-card {
                background-color: white;
                border-radius: 10px;
                box-shadow: 0 3px 8px rgba(0,0,0,0.1);
                margin-bottom: 25px;
                padding: 20px;
                border-left: 6px solid #003366;
                transition: transform 0.2s, box-shadow 0.2s;
            }
            .route-card:hover {
                transform: scale(1.01);
                box-shadow: 0 6px 12px rgba(0,0,0,0.15);
            }
            button {
                font-size: 18px;
                padding: 10px 20px;
                background-color: #003366;
                color: white;
                border: none;
                border-radius: 8px;
                cursor: pointer;
                margin-bottom: 10px;
            }
            button:hover {
                background-color: #0055a5;
            }
            p {
                font-size: 18px;
                color: #222;
                background-color: #f3f6f9;
                padding: 10px;
                border-radius: 6px;
                margin-top: 5px;
            }
            /* Кнопка для слабовидящих */
            .accessibility-btn {
                position: fixed;
                top: 15px;
                right: 15px;
                background-color: #FFD700;
                color: #000;
                border: none;
                padding: 8px 12px;
                font-size: 14px;
                border-radius: 6px;
                cursor: pointer;
                z-index: 1000;
            }
            .accessibility-btn:hover {
                background-color: #ffcc00;
            }
            /* Режим для слабовидящих */
            body.accessible {
                background-color: #000;
                color: #fff;
            }
            body.accessible .route-card {
                background-color: #222;
                border-left: 6px solid #FFD700;
            }
            body.accessible p {
                background-color: #333;
                color: #fff;
            }
            body.accessible button {
                background-color: #FFD700;
                color: #000;
            }
            body.accessible h1.header-with-logos {
                background-color: #000;
                color: #FFD700;
            }
            body.accessible h1.header-with-logos .logo {
                filter: brightness(0) invert(1);
            }
            .feedback {
                text-align: center;
                margin: 60px 0;
                padding: 30px;
                background-color: #f1f1f1;
                border-radius: 10px;
            }
            .feedback h2 {
    margin-bottom: 15px;
                }
                .feedback button {
                    background-color: #28a745;
                    font-size: 18px;
                    border: none;
                    border-radius: 8px;
                    padding: 10px 20px;
                    cursor: pointer;
                }
                .feedback button:hover {
                    background-color: #218838;
                }
                a {
                    text-decoration: none;
                }
            </style>
            <script>
                function toggleAccessibility() {
                    document.body.classList.toggle('accessible');
                }
            </script>
        </head>
        <body>
            <button class="accessibility-btn" onclick="toggleAccessibility()">👁 Режим</button>
            <h1 class="header-with-logos">
                <img src="{{ url_for('static', filename='logo-left.png') }}" alt="Левый логотип" class="logo">
                Маршруты СКФУ
                <img src="{{ url_for('static', filename='logo-right.png') }}" alt="Правый логотип" class="logo">
            </h1>
            <div class="container">
                {% for title, (link, desc) in routes.items() %}
                    <div class="route-card">
                        <a href="{{ link }}" target="_blank" rel="noopener noreferrer">
                            <button type="button" aria-label="{{ title }}">{{ title }}</button>
                        </a>
                        <p>{{ desc }}</p>
                    </div>
                {% endfor %}
            </div>
            <div class="feedback">
                <h2>Оставьте отзыв</h2>
                <button>Отправить отзыв</button>
            </div>
        </body>
        </html>
        """
    return render_template_string(html, routes=routes)


if __name__ == "__main__":
    app.run(debug=True)