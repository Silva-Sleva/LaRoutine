from flask import Flask, request, url_for, render_template, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def start():
    return render_template('base.html', title='Миссия Колонизация Марса')


@app.route('/bags')
def bags():
    return render_template('bags.html', title='Миссия Колонизация Марса')


@app.route('/tshirt')
def tshirt():
    return render_template('tshirt.html', title='Миссия Колонизация Марса')


@app.route('/basket', methods=['GET', 'POST'])
def basket():
    return render_template('basket.html', title='Миссия Колонизация Марса')


@app.route('/about')
def about():
    return render_template('about.html', title='La Routine')

@app.route('/reviews')
def reviews():
    reviews_html = """
        <div class="reviews-page">
            <h2 class="text-center mb-5">Отзывы наших клиентов</h2>

            <div class="row justify-content-center">
                <div class="col-md-8">
                    <div class="reviews-list">
                        <div class="review-card mb-4 p-4" style="background-color: white; border-radius: 5px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
                            <div class="d-flex justify-content-between mb-2">
                                <h5>Анна К.</h5>
                                <div class="text-warning">★★★★★</div>
                            </div>
                            <p class="text-muted small mb-2">15 мая 2025</p>
                            <p>Футболка просто потрясающая! Качество ткани на высоте, принт не выгорает после стирок. Буду заказывать ещё!</p>
                        </div>

                        <div class="review-card mb-4 p-4" style="background-color: white; border-radius: 5px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
                            <div class="d-flex justify-content-between mb-2">
                                <h5>Михаил С.</h5>
                                <div class="text-warning">★★★★☆</div>
                            </div>
                            <p class="text-muted small mb-2">10 мая 2025</p>
                            <p>Сумка очень стильная и удобная, но для меня немного маленькая. Материал приятный на ощупь, швы аккуратные. Носил уже месяц — всё отлично!</p>
                        </div>

                        <div class="review-card mb-4 p-4" style="background-color: white; border-radius: 5px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
                            <div class="d-flex justify-content-between mb-2">
                                <h5>Елена В.</h5>
                                <div class="text-warning">★★★★★</div>
                            </div>
                            <p class="text-muted small mb-2">5 мая 2025</p>
                            <p>Заказала несколько вещей в подарок — все пришли идеально упакованными. Качество превзошло ожидания! Отдельное спасибо за открытку ручной работы — приятный бонус.</p>
                        </div>

                        <div class="review-card mb-4 p-4" style="background-color: white; border-radius: 5px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
                            <div class="d-flex justify-content-between mb-2">
                                <h5>Дмитрий П.</h5>
                                <div class="text-warning">★★★★★</div>
                            </div>
                            <p class="text-muted small mb-2">28 апреля 2025</p>
                            <p>Футболка просто огонь! Сидит идеально, материал водонепроницаемый. Заказывал размер M (рост 180 см) — подошло как влитая.</p>
                        </div>

                        <div class="review-card mb-4 p-4" style="background-color: white; border-radius: 5px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
                            <div class="d-flex justify-content-between mb-2">
                                <h5>Ксения Р.</h5>
                                <div class="text-warning">★★★★★</div>
                            </div>
                            <p class="text-muted small mb-2">12 апреля 2025</p>
                            <p>Быстрая доставка! Сумка просто шикарная. Уже второй раз заказываю у вас — не разочаровали!</p>
                        </div>

                        <div class="review-card mb-4 p-4" style="background-color: white; border-radius: 5px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
                            <div class="d-flex justify-content-between mb-2">
                                <h5>Иван К.</h5>
                                <div class="text-warning">★★★★★</div>
                            </div>
                            <p class="text-muted small mb-2">5 апреля 2025</p>
                            <p>Заказывал сумку — материал приятный, пахнет натуральной кожей, швы ровные. Выглядит дороже, чем стоит. Доставка быстрая, упаковка аккуратная.</p>
                        </div>

                        <div class="review-card mb-4 p-4" style="background-color: white; border-radius: 5px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
                            <div class="d-flex justify-content-between mb-2">
                                <h5>Алиса Т.</h5>
                                <div class="text-warning">★★★★☆</div>
                            </div>
                            <p class="text-muted small mb-2">30 марта 2025</p>
                            <p>Рисунок просто огонь! Но внутренние швы на горловине немного жестковаты — первые пару дней натирали шею. После нескольких стирок стало лучше.</p>
                        </div>

                        <div class="review-card mb-4 p-4" style="background-color: white; border-radius: 5px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
                            <div class="d-flex justify-content-between mb-2">
                                <h5>Сергей В.</h5>
                                <div class="text-warning">★★★★★</div>
                            </div>
                            <p class="text-muted small mb-2">25 марта 2025</p>
                            <p>Заказал костюм — пришёл идеально упакованным, без единого дефекта. Размер подошёл идеально. Буду рекомендовать ваш магазин!</p>
                        </div>
                    </div>

                    <div class="alert alert-info mt-5 text-center">
                        <p class="mb-0">Хотите оставить отзыв? Напишите нам в <a href="#" class="alert-link">Instagram</a> или на почту <strong>reviews@laroutine.ru</strong>, и мы опубликуем его здесь!</p>
                    </div>
                </div>
            </div>
        </div>

        <style>
            .review-card {
                transition: transform 0.3s;
            }

            .review-card:hover {
                transform: translateY(-5px);
            }

            .text-warning {
                color: #ffc107;
                font-size: 1.2rem;
            }

            .review-photo img {
                border: 1px solid #eee;
            }

            .alert-info {
                background-color: var(--secondary-bg);
                border-color: var(--accent-color);
                color: #333;
            }
        </style>
        """

    return f"""
        <!DOCTYPE html>
        <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Отзывы | La Routine</title>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.8.0/font/bootstrap-icons.css">
            <link rel="stylesheet" type="text/css" href="/static/css/style.css">
        </head>
        <body>
            {reviews_html}
        </body>
        </html>
        """

def main():
    app.run(port=8085, host='127.0.0.1', debug=True)


if __name__ == '__main__':
    main()
