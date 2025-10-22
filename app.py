
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
    "Маршрут №17": ("https://mapmagic.app/map?routes=9Kb71W6", "От общежития №9 (пр. Кулакова 2, корп. 6) до кинотеатра «Салют Юг» (ул. 50 лет ВЛКСМ 1). Автобус №9"),
    "Маршрут №18": ("https://mapmagic.app/map?routes=VbMJvX9", "От общежития №9 (пр. Кулакова 2, корп. 6) до Парка Победы (ул. Шпаковская 111к5). Автобус №9"),
    "Маршрут №19": ("https://mapmagic.app/map?routes=64aKyB9", "От Кампуса-север СКФУ (пр. Кулакова 2) до храма Сергия Радонежского (пр. Кулакова 2а/1)"),
    "Маршрут №20": ("https://mapmagic.app/map?routes=9DzLPq0", "От общежития №1 (ул. Михаила Морозова 5) до городской клинической поликлиники № 1"),
    "Маршрут №21": ("https://mapmagic.app/map?routes=0XBMKm9", "От кампус Кулакова до соц защиты ул.Ленина 415Б"),
}

@app.route('/')
def index():
    html = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Маршруты СКФУ</title>
        <style>
            body {
                background-color: #f4f4f4;
                font-family: Arial, sans-serif;
                font-size: 22px;
                color: #111;
                margin: 0;
                padding: 0;
                line-height: 1.8;
                transition: 0.3s;
            }
            h1 {
                text-align: center;
                font-size: 2.5em;
                background-color: #002b5c;
                color: #fff;
                margin: 0;
                padding: 25px 0;
            }
            .container {
                width: 85%;
                max-width: 1000px;
                margin: 30px auto;
            }
            .route-card {
                background-color: #fff;
                border-radius: 12px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.1);
                margin-bottom: 25px;
                padding: 20px;
                border-left: 8px solid #002b5c;
            }
            a {
                text-decoration: none;
            }
            button {
                font-size: 22px;
                padding: 14px 28px;
                background-color: #002b5c;
                color: white;
                border: none;
                border-radius: 10px;
                cursor: pointer;
                width: 100%;
            }
            button:hover {
                background-color: #0055a5;
            }
            p {
                margin-top: 10px;
                font-size: 20px;
                color: #222;
            }

            /* ====== РЕЖИМ ДЛЯ СЛАБОВИДЯЩИХ ====== */
            body.high-contrast {
                background-color: #000;
                color: #fff;
            }
            body.high-contrast h1 {
                background-color: #000;
                color: #FFD700;
            }
            body.high-contrast .route-card {
                background-color: #111;
                border-color: #FFD700;
            }
            body.high-contrast button {
                background-color: #FFD700;
                color: #000;
                font-weight: bold;
            }

            /* ====== КНОПКА ВЕРХУ ====== */
            .accessibility-toggle {
                position: fixed;
                top: 12px;
                right: 12px;
                background-color: #FFD700;
                color: #000;
                border: none;
                padding: 8px 14px;
                font-size: 14px;
                border-radius: 8px;
                cursor: pointer;
                z-index: 1000;
                box-shadow: 0 2px 5px rgba(0,0,0,0.3);
                }
                .accessibility-toggle:hover {
                    background-color: #ffeb3b;
                }

                /* ====== БЛОК С ФОРМОЙ ====== */
                .feedback {
                    background-color: #fff;
                    margin: 40px auto;
                    padding: 25px;
                    border-radius: 10px;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                    text-align: center;
                    width: 80%;
                    max-width: 800px;
                }
                .feedback p {
                    font-size: 20px;
                    color: #444;
                }
            </style>
        </head>
        <body>
            <button class="accessibility-toggle" onclick="toggleMode()">👁 Режим</button>
            <h1>Маршруты СКФУ</h1>
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
                <h2>Форма обратной связи</h2>
                <p>https://docs.google.com/forms/d/e/1FAIpQLSe6HXh596_Ct3lPN4t5_mpEAUzOgTVoX-ZfmcReMg-P-eOQ1g/viewform?usp=header</p>
            </div>

            <script>
                function toggleMode() {
                    document.body.classList.toggle('high-contrast');
                    localStorage.setItem('contrastMode', document.body.classList.contains('high-contrast'));
                }
                if (localStorage.getItem('contrastMode') === 'true') {
                    document.body.classList.add('high-contrast');
                }
            </script>
        </body>
        </html>
        """
    return render_template_string(html, routes=ROUTES)


if __name__ == '__main__':
    app.run(debug=True)