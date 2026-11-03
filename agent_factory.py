import json
import re
from pathlib import Path

from quality.tester import test_agent


OUTPUT_DIR = Path("generated_agents")


def create_agent(name, role, instructions):
    agent = {
        "name": name.strip(),
        "role": role.strip(),
        "instructions": instructions.strip()
    }

    passed, errors = test_agent(agent)

    if not passed:
        return False, errors

    OUTPUT_DIR.mkdir(exist_ok=True)

    filename = re.sub(
        r"[^a-zA-Z0-9_-]",
        "_",
        name.lower()
    ).strip("_")

    if not filename:
        return False, ["Некорректное имя агента"]

    path = OUTPUT_DIR / f"{filename}.json"

    if path.exists():
        return False, ["Агент с таким именем уже существует"]

    path.write_text(
        json.dumps(agent, ensure_ascii=False, indent=4),
        encoding="utf-8"
    )

    return True, [f"Агент сохранён: {path}"]