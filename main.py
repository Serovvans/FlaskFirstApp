from flask import Flask
from utils import *

app = Flask(__name__)


@app.route("/")
def page_index() -> str:
    candidates = get_all()
    return f"<pre>\n{candidates}\n</pre>"


@app.route("/candidate/<int:pk>")
def page_candidates(pk: int) -> str:
    candidate, image = get_by_pk(pk)
    return f"<img src='{image}'>\n\n<pre>\n{candidate}\n</pre>"


@app.route("/skills/<skill_name>")
def page_skills(skill_name: str) -> str:
    candidates = get_by_skill(skill_name)
    return f"<pre>\n{candidates}\n</pre>"


if __name__ == "__main__":
    app.run()
