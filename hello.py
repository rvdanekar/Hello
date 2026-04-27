import os
from datetime import datetime

user = os.environ.get("USERNAME", "User")
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print("====================")
print(f"Hello {user}! Today is {now}")
print("====================")
