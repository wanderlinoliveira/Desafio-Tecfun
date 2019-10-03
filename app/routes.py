from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from moment import Moment
from app import app
from app.forms import ItemForm, SearchForm, LoginForm
from app.models import Item, User
from app import db
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.urls import url_parse

year = Moment.now().year

"""
@app.route('/index')
def index():    
    items = Item.query.all()
    return render_template('index.jade', title='Home', year=year, items= items)
"""
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():  
    form = SearchForm()  
    #if request.method == 'GET':
    if form.validate_on_submit(): #post request
        #content = request.json
        #items = Item.query.filter_by(name=  content["name"]).first()
        name = str(form.name.data)
        responsavel = str(form.responsavel.data)
        print(responsavel)
        startsitems = Item.query.filter(Item.name.startswith(name)).all()
        endsitems = Item.query.filter(Item.name.endswith(name)).all()
        items = startsitems + endsitems
        filtermsg = "Exibindo resultados para `" + name + "´"
        return render_template('index.jade', title='Home', year=year, items= items, form=form, name= name,filtermsg=filtermsg)    
    else:
        items = Item.query.all()
        return render_template('index.jade', title='Home', year=year, items= items, form=form, name="" , filtermsg="")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect( url_for('index') )
    form = LoginForm()  
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return render_template('login.jade', title='Login', year=year, form=form, error='Login ou Senha Inválido')
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect( next_page )   
    else:
        return render_template('login.jade', title='Login', year=year, form=form, error='')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/new', methods=['GET', 'POST'])
@login_required
def new():  
    item = {
        "item" : "",
        "number" : 1000,
        "qtt" : 1,
        "responsavel" : "",
        "retornar" : 1
    }
    form = ItemForm()
    if form.validate_on_submit():
        flash('Create item {}'.format(form.name.data))
        newItem = Item(form.name.data, form.number.data)
        newItem.qtt = form.qtt.data
        newItem.responsavel = form.responsavel.data
        newItem.retornar = form.retornar.data
        try:
            db.session.add(newItem)
            db.session.commit()
            return redirect( url_for('index') )
        except  SQLAlchemyError as err:
            error = str(err.__dict__['orig'])
            return render_template('form.jade', title='New', year=year, form=form, item= item, error = error, pageoption='Novo')      
    else:
        return render_template('form.jade', title='New', year=year, form=form, item= item, error = "", pageoption='Novo')

@app.route('/edit/<id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    item = Item.query.filter_by(id= str(id)).first()
    form = ItemForm()
    if form.validate_on_submit():
        flash('Edit Item {}'.format(form.name.data))
        item.name = form.name.data
        item.qtt = form.qtt.data
        item.responsavel = form.responsavel.data
        item.retornar =  form.retornar.data
        db.session.commit()
        return redirect( url_for('index') )  
    form.responsavel.default = item.responsavel
    #form.number.render_kw = {"disabled": ""}
    form.process()
    return render_template('form.jade', title='Edit', year=year, form=form, item= item, pageoption='Editar')

@app.route('/show/<id>')
@login_required
def show(id):    
    item = Item.query.filter_by(id= str(id)).first()
    return render_template('show.jade', title='Show', year=year, item= item)

@app.route('/delete/<id>')
@login_required
def delete(id):    
    item = Item.query.filter_by(id= str(id)).first()
    db.session.delete(item)
    db.session.commit()
    return redirect( url_for('index') )  
