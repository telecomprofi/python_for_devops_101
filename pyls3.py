from subprocess import PIPE, run

command = ['ls', '-l']
result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True)
print(result.returncode, result.stdout, result.stderr)
