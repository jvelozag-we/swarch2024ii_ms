from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from services.products_service import ProductService
product_blueprint = Blueprint('products', __name__)
@product_blueprint.route('/products', methods=['POST'])
def create_product():
    data = request.form
    name = data.get('name')
    description = data.get('description')
    if not name:
        return jsonify({'error': 'Name is required'}), 400
    existing_product= ProductService.get_product_by_name(name)
    if existing_product:
        ProductService.update_product_description(name, description)
    else:
        ProductService.create_product(name, description)

    return redirect(url_for('products.index'))
@product_blueprint.route('/')
def index():
    return render_template('index.html')