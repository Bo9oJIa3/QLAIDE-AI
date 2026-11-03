REQUIRED_FIELDS = ["name", "role", "instructions"]


def test_agent(agent):
    errors = []

    for field in REQUIRED_FIELDS:
        if not agent.get(field):
            errors.append(f"Нет обязательного поля: {field}")

    if errors:
        return False, errors

    return True, ["Базовая проверка пройдена"]