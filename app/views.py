from flask import Blueprint

admin_bp = Blueprint("admin",__name__)

@admin_bp.route("/")
def dashboard():
    return "esta na home"

@admin_bp.route("/admin")
def admin_page():
    return "Admin"


@admin_bp.route("/pagina")
def index():
    return "pagina_1"

@admin_bp.route("/pagina2")
def pangia():
    return "pagina_2"