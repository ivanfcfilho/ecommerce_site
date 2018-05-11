from flask import Flask, render_template, json, request, session
from ajax import Ajax
from werkzeug import generate_password_hash, check_password_hash

app = Flask(__name__)
aj = Ajax()

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/login')
def showLogin():
    return render_template('login.html')

@app.route('/signup')
def showSignUp():
    return render_template('signup.html')

@app.route('/ajax/signup', methods=['POST'])
def ajaxSignup():
    return aj.signUp(request.form)

@app.route('/ajax/login', methods=['POST'])
def ajaxLogin():
    r = aj.login(request.form)
    if(r[1] == 200):
        session['username'] = 'user'
        session.modified = True
    else:
        print('Erro')
    return r

@app.route('/logout', methods=['GET'])
def logout():
    session.pop('username', None)
    session.modified = True
    return render_template('index.html')
    
@app.route('/product/<string:productId>')
def productPage(productId):
    return render_template('product.html')
    
@app.route('/product_search/')
def productSearch():
    return render_template('product_search.html')
    
@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/ajax/product_details/<string:productId>')
def showProduct(productId):
    r = aj.getProduct(productId)
    if(r[1] != 200):
        print('Erro')
    return r

@app.route('/ajax/product_search/')
def searchProduct():
    dic = {}
    if(request.args.get('brand')): dic["brand"] = request.args.get('brand')
    if(request.args.get('category_id')): dic["category_id"] = request.args.get('category_id')
    if(request.args.get('highlight')): dic["highlight"] = request.args.get('highlight')
    if(request.args.get('max_price')): dic["max_price"] = request.args.get('max_price')
    if(request.args.get('min_price')): dic["min_price"] = request.args.get('min_price')
    if(request.args.get('name')): dic["name"] = request.args.get('name')
    if(request.args.get('page')): dic["page"] = request.args.get('page')
    if(request.args.get('parent_product')): dic["parent_product"] = request.args.get('parent_product')
    r = aj.searchProduct(dic)
    if(r[1] != 200):
        print('Erro')
    return r
    
@app.route('/ajax/category_search/')
def searchCategory():
    dic = {}
    if(request.args.get('name')): dic["name"] = request.args.get('name')
    if(request.args.get('page')): dic["page"] = request.args.get('page')
    if(request.args.get('parent_category')): dic["parent_category"] = request.args.get('parent_category')
    r = aj.searchCategory(dic)
    if(r[1] != 200):
        print('Erro')
    return r
    
@app.route('/add_to_cart', methods=['POST'])
def addToCart():
    data = request.get_json()
    if data is None:
        print("Erro. Nenhum produto enviado")
        return "400"
    #
    #add data para session
    #
    return "200"
    
@app.route('/get_cart', methods=['GET'])
def getCart():
    #
    #get cart de session
    #return json
    #
    return "200"
    
if __name__ == "__main__":
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.run(port=5000)
