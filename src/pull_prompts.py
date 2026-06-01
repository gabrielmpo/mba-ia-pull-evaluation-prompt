import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from langchain import hub
from langchain_core.load import dumpd
from langsmith import Client
from utils import save_yaml, check_env_vars, print_section_header

load_dotenv()

PROMPT_NAME = "leonanluppi/bug_to_user_story_v1"
OUTPUT_FILE = Path("prompts/bug_to_user_story_v1.yml")

def pull_prompts_from_langsmith():
    client = Client()
    prompt = client.pull_prompt(PROMPT_NAME)    
    prompt_dict = dumpd(prompt)
    save_yaml(prompt_dict, OUTPUT_FILE)

    print(f"Prompt salvo em: {OUTPUT_FILE}")

def main():
    try:
        pull_prompts_from_langsmith()
        return 0
    except Exception as ex:
        print(f"Erro ao realizar pull do prompt: {ex}")
        return 1

if __name__ == "__main__":
    sys.exit(main())