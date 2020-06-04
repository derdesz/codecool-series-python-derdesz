from flask import Flask, render_template, url_for, request
from data import queries

app = Flask('codecool_series')


@app.route('/')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)


@app.route('/design')
def design():
    return render_template('design.html')

@app.route('/pa3')
def pa3():
    return render_template('pa5.html')


@app.route('/pa2')
def pa2():
    pa2_query_result = queries.pa2()
    return render_template('pa2.html', pa2_query_result=pa2_query_result)

@app.route('/pa7')
def pa7():
    genre = request.args.get('genre')
    pa7_result = queries.pa7(genre)
    return render_template('pa7.html', pa7_result=pa7_result)

def main():
    app.run(debug=True)



if __name__ == '__main__':
    main()
