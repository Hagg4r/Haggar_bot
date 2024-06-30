import subprocess

def avvia_maxphisher():
    comando = ["maxphisher"]
    processo = subprocess.Popen(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = processo.communicate()

    print(stdout.decode())
    if stderr:
        print(stderr.decode())

if __name__ == "__main__":
    avvia_maxphisher()
