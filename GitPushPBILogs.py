import subprocess as cmd
import os

os.popen("git add .")
os.popen("git commit -m 'ok'")
os.popen("git push -u origin master -f")
#cp = cmd.run("git add .", check=True, shell=True)
#cp = cmd.run("git commit -m 'ok'", check=True, shell=True)
#cp = cmd.run("git push -u origin master -f", check=True, shell=True)
