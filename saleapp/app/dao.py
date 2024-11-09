from app.models import Category, Product

def load_categorie():
    return Category.query.order_by('id').all()

def load_products(category_id =None):
   query = Product.query
   if category_id:
       query = query.filter(Product.category_id == int(category_id))
    return query.all()