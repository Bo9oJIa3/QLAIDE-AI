from agents.registry import list_agents


def choose_agent(task):
    task = task.lower()
    agents = list_agents()

    for agent_id, agent in agents.items():
        for keyword in agent["keywords"]:
            if keyword in task:
                return agent_id, agent

    return "researcher", agents["researcher"]


def handle_task(task):
    agent_id, agent = choose_agent(task)

    return {
        "task": task,
        "selected_agent": agent["name"],
        "role": agent["role"],
        "status": "Задача назначена"
    }
