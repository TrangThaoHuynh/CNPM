from flask import render_template, request

from app import app

import dao

@app.route("/")
def index():
    category_id = request.args.get('category_id')
    cates = dao.load_categorie()
    prods = dao.load_products(category_id)
    return render_template('index.html', categories=cates, products=prods)


if __name__ == '__main__':
    app.run(debug=True)
