from app import app

@app.route('/2')
def f2():
    return '2'