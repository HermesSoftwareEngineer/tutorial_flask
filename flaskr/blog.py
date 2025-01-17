from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from .db import get_db
from flaskr.auth import login_required
from werkzeug.exceptions import abort


bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()

    return render_template('blog/index.html', posts=posts)

@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method=='POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'O título é obrigatório!'
        
        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (title, body, author_id) VALUES (?, ?, ?)',
                (title, body, g.user['id'])
            )
            db.commit()
            return redirect(url_for('index'))
        
    return render_template('blog/create.html')

def get_post(id, check_autor=True):
    post = get_db().execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, 'Postagem não encontrada!')
    elif check_autor and g.user['id'] != post['author_id']:
        abort(403)
    
    return post

@bp.route('/<int:id>/update', methods=['GET', 'POST'])
def update(id):
    post = get_post(id)

    if request.method=='POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'O título é obrigatório!'
        
        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE post SET title = ?, body = ?'
                ' WHERE id = ?',
                (title, body, id)
            )
            db.commit()
            return redirect(url_for('index'))
        
    return render_template('blog/update.html', post=post)

@bp.route('/<int:id>/delete', methods=['POST'])
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute(
        'DELETE FROM post WHERE id = ?', (id,)
    )
    db.commit()

    return redirect(url_for('index'))