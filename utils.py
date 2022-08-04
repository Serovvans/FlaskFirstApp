import json
import os

from typing import List, Dict, Tuple


def load_candidates() -> List[Dict]:
    file = os.path.join("data", "candidates.json")
    with open(file, encoding="utf-8") as read_data:
        candidates = json.load(read_data)
    return candidates


def get_all() -> str:
    candidates = load_candidates()
    str_candidates = []
    for candidate in candidates:
        str_candidates.append(f"{candidate['name']}\n{candidate['position']}\n{(candidate['skills'])}")

    return "\n\n".join(str_candidates)


def get_by_pk(pk: int) -> Tuple[str, str]:
    candidates = load_candidates()
    for candidate in candidates:
        if candidate["pk"] == pk:
            return f"{candidate['name']}\n{candidate['position']}\n{(candidate['skills'])}",\
                   candidate["picture"]


def get_by_skill(skill_name: str) -> str:
    candidates = load_candidates()
    str_candidates = []
    for candidate in candidates:
        if skill_name.lower() in candidate["skills"].lower().split(", "):
            str_candidates.append(f"{candidate['name']}\n{candidate['position']}\n{(candidate['skills'])}")

    return "\n\n".join(str_candidates)
