import json
import subprocess


PROTECTED_RUNS = [
    7051989759,
]


def get_workflow_runs():
    command = 'gh run list --json displayTitle,databaseId'
    result = subprocess.run(command, shell=True, capture_output=True)
    result = result.stdout.decode('utf-8')
    result = json.loads(result)
    # skip the first one
    result = result[1:]
    return result


def delete_workflow_runs():
    runs = get_workflow_runs()
    for run in runs:
        if run['databaseId'] not in PROTECTED_RUNS:
            command = f'gh run delete {run["databaseId"]}'
            subprocess.run(command, shell=True)
            print(f'Deleted run {run["databaseId"]}')


if __name__ == '__main__':
    for i in range(2):  # 24 * 2 // 20 + 1
        delete_workflow_runs()
