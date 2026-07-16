from datetime import timedelta

def next_date(task):

    if task.recurring_type == "daily":
        return task.due_date + timedelta(days=1)

    if task.recurring_type == "weekly":
        return task.due_date + timedelta(days=7)

    if task.recurring_type == "monthly":
        return task.due_date + timedelta(days=30)

    if task.recurring_type == "yearly":
        return task.due_date + timedelta(days=365)