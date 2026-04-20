from flask_jwt_extended import create_access_token, jwt_required
from flask_login import login_user
from app.blueprints import user_blp, task_blp
from app.schemas import UserSchema, TaskSchema, LoginSchema, TokenSchema
from app.core import (
    create_task_service,
    get_tasks_service,
    register_user_service,
    login_user_service
)

# -------- TASK -------- #
# Note: Currently using flask_smorest for documentation.
# If using flasgger, you can use @swag_from instead:
# from flasgger import swag_from

@task_blp.response(200, TaskSchema(many=True))
@jwt_required()
# @swag_from('docs/task_docs.yml')  # This would link to get_tasks in the YAML
def get_tasks_view():
    """List tasks"""
    tasks = get_tasks_service()
    return tasks

@task_blp.arguments(TaskSchema)
@task_blp.response(201, TaskSchema)
@jwt_required()
# @swag_from('docs/task_docs.yml')  # This would link to create_task in the YAML
def create_task_view(task_data):
    """Create a new task"""
    task = create_task_service(task_data)
    return task

# -------- USER -------- #
def register_user_view(user_data):
    user = register_user_service(user_data)
    if not user:
        return {"error": "Username already exists"}, 400
    return user

def login_user_view(login_data):
    user = login_user_service(login_data)
    if not user:
        return {"error": "Invalid credentials"}, 401
    
    access_token = create_access_token(identity=str(user.id))
    
    # 🔥 session login
    login_user(user)

    return {"message": "Login successful", "access_token": access_token}