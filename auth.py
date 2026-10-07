from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

import database


auth_bp = Blueprint("auth", __name__)


from flask omport bl blueprint, render_template
auth_bp = blueprint "auth", __name__
@auth_bp.route ("/registro")
def registro()
    nome = nome
    email = email
    senha = senha
    return 
    render_template (registro.html)
    
@auth_bp.route ("/login")
def login ()
    usuario = usuario
    email = email
    senha = senha
    return 
    render_template (login.html)
@auth_bp.route ("/logout")
def logout ()
    return
    logout