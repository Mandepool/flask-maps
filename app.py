
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
    mode = request.args.get("mode", "normal")
    html = """
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Доступный городской маршрут</title>
        <style>
            body {
                background-color: {% if mode == 'vision' %}#fff7cc{% else %}#f9f9f9{% endif %};
                font-family: Arial, sans-serif;
                font-size: {% if mode == 'vision' %}22px{% else %}18px{% endif %};
                color: {% if mode == 'vision' %}#000{% else %}#111{% endif %};
                line-height: 1.5;
                margin: 0;
                padding: 0;
            }
            header {
                display: flex;
                align-items: center;
                justify-content: space-between;
                background-color: {% if mode == 'vision' %}#000{% else %}#003366{% endif %};
                color: white;
                padding: 12px 20px;
            }
            h1 {
                font-size: {% if mode == 'vision' %}2.2em{% else %}1.8em{% endif %};
                margin: 0;
            }
            header img {
                height: {% if mode == 'vision' %}90px{% else %}70px{% endif %};
                width: auto;
                border-radius: 6px;
            }
            .container {
                width: 90%;
                max-width: 900px;
                margin: 20px auto;
            }
            .route-card {
                background-color: {% if mode == 'vision' %}#fff{% else %}white{% endif %};
                border-radius: 8px;
                box-shadow: 0 2px 6px rgba(0,0,0,0.1);
                margin-bottom: 18px;
                padding: 15px;
                border-left: 5px solid {% if mode == 'vision' %}#000{% else %}#003366{% endif %};
            }
            .route-card:hover {
                transform: scale(1.01);
                transition: 0.2s;
                box-shadow: 0 4px 8px rgba(0,0,0,0.15);
            }
            button {
                font-size: {% if mode == 'vision' %}20px{% else %}16px{% endif %};
                padding: 12px 28px;
                background-color: {% if mode == 'vision' %}#000{% else %}#003366{% endif %};
                color: white;
                border: none;
                border-radius: 6px;
                cursor: pointer;
                margin-bottom: 8px;
            }
            button:hover {
                background-color: {% if mode == 'vision' %}#222{% else %}#0055a5{% endif %};
            }
            p {
                font-size: {% if mode == 'vision' %}20px{% else %}16px{% endif %};
                color: {% if mode == 'vision' %}#000{% else %}#222{% endif %};
                margin: 5px 0 0 0;
            }
            /* Кнопка для слабовидящих — внизу справа */
            .toggle-btn {
                position: fixed;
                bottom: 20px;
                right: 20px;
                background-color: {% if mode == 'vision' %}#000{% else %}#ffcc00{% endif %};
                color: {% if mode == 'vision' %}#fff{% else %}#000{% endif %};
                font-size: 16px;
                padding: 14px 24px;
                border-radius: 50px;
                border: none;
                cursor: pointer;
                font-weight: bold;
                box-shadow: 0 2px 8px rgba(0,0,0,0.3);
                z-index: 100;
            }
            .toggle-btn:hover {
                background-color: {% if mode == 'vision' %}#222{% else %}#ffdb4d{% endif %};
            }
            .feedback {
    text-align: center;
                    margin: 30px 0 20px 0;
                }
                .feedback a {
                    text-decoration: none;
                    background-color: {% if mode == 'vision' %}#000{% else %}#003366{% endif %};
                    color: white;
                    padding: 10px 20px;
                    border-radius: 6px;
                    font-size: {% if mode == 'vision' %}20px{% else %}16px{% endif %};
                }
                .feedback a:hover {
                    background-color: {% if mode == 'vision' %}#222{% else %}#0055a5{% endif %};
                }
            </style>
        </head>
        <body>
            <header>
                <img src="{{ url_for('static', filename='photo_2025-10-23_18-18-24.jpg') }}" alt="Логотип слева">
                <h1>Доступный городской маршрут</h1>
                <img src="{{ url_for('static', filename='photo_2025-10-24_17-04-27.jpg') }}" alt="Логотип справа">
            </header>

            <a href="{{ url_for('index', mode='vision' if mode == 'normal' else 'normal') }}">
                <button class="toggle-btn">
                    {% if mode == 'normal' %}Версия для слабовидящих{% else %}Обычный режим{% endif %}
                </button>
            </a>

            <div class="container">
                {% for title, data in routes.items() %}
                    <div class="route-card">
                        <form action="{{ data[0] }}" method="get" target="_blank">
                            <button type="submit">{{ title }}</button>
                        </form>
                        <p>{{ data[1] }}</p>
                    </div>
                {% endfor %}
            </div>

            <div class="feedback">
                <p>Оставьте отзыв о маршрутах:</p>
                <a href="https://docs.google.com/forms/d/e/1FAIpQLSe6HXh596_Ct3lPN4t5_mpEAUzOgTVoX-ZfmcReMg-P-eOQ1g/viewform?usp=header" target="_blank">Открыть форму</a>
            </div>
        </body>
        </html>
        """
    return render_template_string(html, routes=ROUTES, mode=mode)


if __name__ == '__main__':
    app.run(debug=True)