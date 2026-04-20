from app.blueprints import user_blp, task_blp
from app.views import (
    register_user_view,
    login_user_view,
    create_task_view,
    get_tasks_view
)

# --- User Routes ---
user_blp.route("/register", methods=["POST"])(register_user_view)
user_blp.route("/login", methods=["POST"])(login_user_view)

# --- Task Routes ---
task_blp.route("/tasks", methods=["GET"])(get_tasks_view)
task_blp.route("/tasks", methods=["POST"])(create_task_view)