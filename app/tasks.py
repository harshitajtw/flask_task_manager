from celery import Celery

celery=Celery('tasks', broker='redis://localhost:6379/0')

@celery.task
def send_welcome_email(username):
    import time 
    time.sleep(5)


    print(f"Email sent to {username}")