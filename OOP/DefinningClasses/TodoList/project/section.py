from .task import Task


class Section:

    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task.name not in [t.name for t in self.tasks]:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"
        else:
            return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str):
        if task_name in [t.name for t in self.tasks]:
            for t in self.tasks:
                if t.name == task_name:
                    t.completed = True
                    return f"Completed task {task_name}"
        else:
            return f"Could not find task with the name {task_name}"

    def clean_section(self):
        amount = 0
        for t in self.tasks:
            if t.completed:
                self.tasks.remove(t)
                amount += 1

        return f"Cleared {amount} tasks."

    def view_section(self):
        name_info = f"Section {self.name}:"
        tasks_info = "\n".join([t.details() for t in self.tasks])
        if len(self.tasks) > 0:
            return name_info + "\n" + tasks_info + "\n"
        else:
            return name_info + "\n"
