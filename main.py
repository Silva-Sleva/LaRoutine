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


def main():
    # db_session.global_init("db/blogs.db")
    # add_user()
    # add_job()
    app.run(port=8085, host='127.0.0.1', debug=True)

if __name__ == '__main__':
    main()