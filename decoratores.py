# import time

# def log_execution(func):
#     def wrapper(*args,**kwargs):
#         print(f" Execution function {func.__name__} started")
#         result = func(*args,**kwargs)
#         print(f" Execution function {func.__name__} ended")
#         return result
#     return wrapper

# @log_execution
# def train_model():
#     print("Training model...")
#     time.sleep(1)
#     print("Model training in progress...")
#     time.sleep(1)
#     print("Finalizing model...")

#     # Simulate training with a sleep or complex logic
#     print("Model trained successfully!")

# train_model()

def login_required(func):
    def wrapper(user,*args,**kwargs):
        if not user.get("login"):
            print("User not logged in. Access denied.")
            return None
        return func(user,*args,**kwargs)
    return wrapper

@login_required
def dashbord(user):
    print(f"Welcome to your dashboard, {user['name']}!")

user1 = {"name":"Alice","login":True}
user2 = {"name":"Bob","login":False}
dashbord(user1)
dashbord(user2)