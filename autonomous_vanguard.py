import os, subprocess
MY_NAME = "mohammad"
MY_EMAIL = "Tash2005msm@gmail.com"
# كود التشغيل السيادي المختصر
os.system(f"git config --global user.name '{MY_NAME}'")
os.system(f"git config --global user.email '{MY_EMAIL}'")
os.system("git init && git add . && git commit -m 'Fast Launch'")
os.system(f"gh repo create Vanguard-Final-{MY_NAME} --public --source=. --remote=origin --push")
