from flask_smorest import Blueprint

user_blp = Blueprint("users", "users", url_prefix="/api", description="Operations on users")
task_blp = Blueprint("tasks", "tasks", url_prefix="/api", description="Operations on tasks")
