from master.orchestrator import handle_task
from factory.agent_factory import create_agent
from agents.registry import list_agents


def main():
    print("=" * 35)
    print("       QLAIDE AI v0.1")
    print("=" * 35)

    while True:
        print("\n1. Отправить задачу MASTER")
        print("2. Создать агента через FACTORY")
        print("3. Показать всех агентов")
        print("0. Выход")

        choice = input("\nВыбор: ").strip()

        if choice == "1":
            task = input("Твоя задача: ")
            result = handle_task(task)

            print("\nMASTER:")
            for key, value in result.items():
                print(f"{key}: {value}")

        elif choice == "2":
            name = input("Имя агента: ")
            role = input("Его роль: ")
            instructions = input("Инструкции агенту: ")

            success, messages = create_agent(
                name, role, instructions
            )

            print("\nFACTORY:")
            print("Успешно" if success else "Ошибка")

            for message in messages:
                print(message)

        elif choice == "3":
            for agent_id, agent in list_agents().items():
                print(f"{agent_id}: {agent['name']}")

        elif choice == "0":
            print("QLAIDE AI завершает работу.")
            break

        else:
            print("Неизвестная команда.")


if __name__ == "__main__":
    main()