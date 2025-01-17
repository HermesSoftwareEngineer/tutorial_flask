import functools
from flask import (
    Blueprint, render_template, redirect, url_for, g, request, flash, session
)
from werkzeug.security import check_password_hash, generate_password_hash
from .db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        error = None
        db = get_db()

        if username is None:
            error = 'O usuário é obrigatório!'
        elif password is None:
            error = 'A senha é obrigatória!'

        if error is None:
            try:
                db.execute(
                    'INSERT INTO user (username, password) VALUES (?, ?)',
                    (username, generate_password_hash(password))
                )
            except db.IntegrityError:
                error = 'Usuário já cadastrado!'
            else:
                return redirect(url_for('auth.login'))
        
        flash(error)

    return render_template('auth/register.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None
        db = get_db()

        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone

        if user is None:
            error = 'Usuário inválido!'
        elif not check_password_hash(user['password', password]):
            error = 'Senha inválida!'
        
        if error is None:
            session.clear()
            session['user_id'] = user['id']
            redirect(url_for('index'))

        flash(error) 

    return render_template('auth/login.html')

@bp.before_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone

@bp.route('/logout')
def logout():
    session.clear()
    redirect(url_for('index'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('index'))
        return view(**kwargs)
    
    return wrapped_view