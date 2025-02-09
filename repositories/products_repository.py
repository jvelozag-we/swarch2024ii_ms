from models.products import Products, db

class ProductRepository:
    @staticmethod
    def create_product(name, description):
        existing_product = Products.query.filter_by(name=name).first()
        if existing_product:
            ProductRepository.update_product_description(name, description)
        else:
            product = Products(name=name, description=description)
            db.session.add(product)
            db.session.commit()
        return existing_product or product

    @staticmethod
    def update_product_description(name, description):
        product = Products.query.filter_by(name=name).first()
        if product:
            product.description = description
            db.session.commit()
        return product

    @staticmethod
    def get_product_by_name(name):
        return Products.query.filter_by(name=name).first()