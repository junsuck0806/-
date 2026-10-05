import json
import sys
from pathlib import Path

FILE = Path("todos.json")


def load():
    return json.loads(FILE.read_text(encoding="utf-8")) if FILE.exists() else []


def save(todos):
    FILE.write_text(json.dumps(todos, ensure_ascii=False, indent=2), encoding="utf-8")


def show(todos):
    if not todos:
        print("할 일이 없어요 🎉")
    for i, t in enumerate(todos, 1):
        print(f"{i}. [{'x' if t['done'] else ' '}] {t['title']}")


def main():
    args = sys.argv[1:]
    todos = load()

    if not args or args[0] == "list":
        show(todos)
    elif args[0] == "add" and len(args) > 1:
        todos.append({"title": " ".join(args[1:]), "done": False})
        save(todos)
        print("추가했어요!")
    elif args[0] == "done" and len(args) > 1:
        todos[int(args[1]) - 1]["done"] = True
        save(todos)
        print("완료!")
    elif args[0] == "remove" and len(args) > 1:
        todos.pop(int(args[1]) - 1)
        save(todos)
        print("삭제했어요.")
    else:
        print("사용법: python todo.py [list | add 내용 | done 번호 | remove 번호]")


if __name__ == "__main__":
    main()
