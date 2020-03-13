import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cofferupApp.models import Coffer
from django.contrib.auth.models import User

def get_coffer(coffer_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT l.id, l.title, l.address
        FROM cofferapp_coffer l
        WHERE l.id = ?
        """,
        (coffer_id,))

        coffer_to_view = db_cursor.fetchone()

        return coffer_to_view

@login_required
def coffer_details(request, coffer_id):
    if request.method == 'GET':
        coffer = get_coffer(coffer_id)

        template = 'coffers/detail.html'
        context = {'coffer': coffer}

        return render(request, template, context)