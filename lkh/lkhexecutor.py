import os
import subprocess
import re

def execute_command(filename):
    open('_out.txt', 'w').close()
    cmd = f"python3 lkhcli.py --instance {filename} >> _out.txt"
    subprocess.run(cmd, shell=True)

    with open("_out.txt", "r") as f:
        content = f.readlines()

    cost = None
    pattern = r"Cost.min = (\d+)"
    for line in content:
        match = re.search(pattern, line)
        if match:
            cost = match.group(1)
            break

    return cost

def main():
    folder_path = "./instances"
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    open('tabela.txt', 'w').close()
    with open("tabela.txt", "w") as table:
        table.write("Instância\tRepetição\tSeed\tResultado\n")

        for file in files:
            for _ in range(10):
                cost = execute_command("./instances/"+file)
                table.write(f"{file}\t{_}\t{file}\t{cost}\n")

if __name__ == "__main__":
    main()

