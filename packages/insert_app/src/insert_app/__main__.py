import sqlite3
import os
from flask import Flask, render_template_string, request

from insert_app.config import FORM_HTML

app = Flask(__name__)


def init_sqlite() -> None:
    conn = sqlite3.connect(os.environ.get("TABLE_PATH", "/var/lib/metadata.db"))
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS base_data(
        tag text,
        show_name text, 
        show_nr integer, 
        dj_name text,
        picture text,
        description text,
        'tags-0-tag' text,
        'tags-1-tag' text,
        'tags-2-tag' text,
        'tags-3-tag' text,
        'tags-4-tag' text,
        live boolean
        )
    ''')
    conn.commit()


def insert_base_data(input: dict) -> None:
    conn = sqlite3.connect(os.environ.get("TABLE_PATH", "/var/lib/metadata.db"))
    cursor = conn.cursor()
    sql = '''
        INSERT INTO base_data(tag, show_name, show_nr, dj_name, picture, description, 'tags-0-tag','tags-1-tag','tags-2-tag', 'tags-3-tag', 'tags-4-tag', live)
        VALUES(:tag, :show_name, :show_nr, :dj_name, :picture, :description, :tags_0,:tags_1,:tags_2, :tags_3, :tags_4, :live)
    '''
    cursor.execute(sql, input)
    conn.commit()


@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        item={
            "tag": request.form.get("tag"),
            "show_name": request.form.get("show_name"),
            "show_nr": request.form.get("show_nr"),
            "dj_name": request.form.get("dj_name"),
            "picture": request.form.get("picture"),
            "description": request.form.get("description"),
            "tags_0": request.form.get("tags_0"),
            "tags_1": request.form.get("tags_1"),
            "tags_2": request.form.get("tags_2"),
            "tags_3": request.form.get("tags_3"),
            "tags_4": request.form.get("tags_4", None),
            "live": request.form.get("live") == "true"
        }

        insert_base_data(item)

        return f"Inserted succesfully"

    return render_template_string(FORM_HTML)

def run():
    init_sqlite()
    app.run(host="localhost", port=5001)

if __name__ == "__main__":
    run()
