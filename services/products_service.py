from repositories.products_repository import ProductRepository

class ProductService:
    @staticmethod
    def create_product(name, description):
        return ProductRepository.create_product(name, description)
    
    @staticmethod
    def update_product_description(name, description):
        return ProductRepository.update_product_description(name, description)
    
    @staticmethod
    def get_product_by_name(name):
        return ProductRepository.get_product_by_name(name)
