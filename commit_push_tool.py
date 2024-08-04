import subprocess
import sys

def commit_and_push(commit_message):
    try:
        # Stage all changes
        subprocess.run(['git', 'add', '.'], check=True)
        # Commit changes
        subprocess.run(['git', 'commit', '-m', commit_message], check=True)
        # Push changes
        subprocess.run(['git', 'push'], check=True)
        print('Changes committed and pushed successfully.')
    except subprocess.CalledProcessError as e:
        print(f'Error during Git operation: {e}')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python commit_push_tool.py <commit_message>')
    else:
        commit_and_push(sys.argv[1])