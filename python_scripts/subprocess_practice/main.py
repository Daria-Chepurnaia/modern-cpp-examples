import subprocess

result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print(result.stdout)

if result.returncode == 0:
    print("Command succeeded")
else:
    print("Command failed")

result = subprocess.run(["docker", "ps"], capture_output=True, text=True)
print(result.stdout)