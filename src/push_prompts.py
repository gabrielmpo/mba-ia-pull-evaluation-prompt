"""
Script para fazer push de prompts otimizados ao LangSmith Prompt Hub.

Este script:
1. Lê os prompts otimizados de prompts/bug_to_user_story_v2.yml
2. Valida os prompts
3. Faz push PÚBLICO para o LangSmith Hub
4. Adiciona metadados (tags, descrição, técnicas utilizadas)

SIMPLIFICADO: Código mais limpo e direto ao ponto.
"""

import os
import sys
from dotenv import load_dotenv
from pathlib import Path
from langchain import hub
from langsmith import Client
from langchain_core.prompts import ChatPromptTemplate
from utils import load_yaml, check_env_vars, print_section_header

load_dotenv()

PROMPT_FILE = "prompts/bug_to_user_story_v2.yml"
PROMPT_NAME = "bug_to_user_story_v2"


def push_prompt_to_langsmith(prompt_name: str, prompt_data: dict) -> bool:
    try:
        client = Client()

        username = os.getenv("USERNAME_LANGSMITH_HUB")
        full_prompt_name = f"{username}/{prompt_name}"

        client.push_prompt(
            full_prompt_name,
            object=prompt_data,
            is_public=True,
            description=(
                "Converte relatos de bugs em User Stories utilizando "
                "Few-Shot Learning, Role Prompting e Skeleton of Thought."
            ),
            tags=[
                "prompt-engineering",
                "few-shot-learning",
                "role-prompting",
                "skeleton-of-thought",
                "user-story",
                "bug-analysis",
            ],
        )
        print(f"Prompt publicado: {full_prompt_name}")

        return True

    except Exception as ex:
        print(f"Erro ao publicar prompt: {ex}")
        return False


def validate_prompt(prompt_data: dict) -> tuple[bool, list]:
    errors = []

    if not prompt_data:
        errors.append("Prompt vazio.")

    if "kwargs" not in prompt_data:
        errors.append("Campo 'kwargs' não encontrado.")

    kwargs = prompt_data.get("kwargs", {})

    if "messages" not in kwargs:
        errors.append("Campo 'messages' não encontrado.")

    elif not kwargs["messages"]:
        errors.append("Lista de mensagens vazia.")

    return len(errors) == 0, errors

def main():
    print_section_header("Push de Prompt para LangSmith")

    check_env_vars(
        [
            "LANGSMITH_API_KEY",
            "USERNAME_LANGSMITH_HUB",
        ]
    )

    prompt_path = Path(PROMPT_FILE)

    if not prompt_path.exists():
        print(f"Arquivo não encontrado: {prompt_path}")
        return 1

    prompt_data = load_yaml(prompt_path)

    is_valid, errors = validate_prompt(prompt_data)

    if not is_valid:
        print("Prompt inválido:")

        for error in errors:
            print(f" - {error}")

        return 1

    print("Prompt validado")

    success = push_prompt_to_langsmith("bug_to_user_story_v2", prompt_data)

    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())