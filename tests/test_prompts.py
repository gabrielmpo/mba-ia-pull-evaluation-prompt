import pytest
import yaml
import sys
from pathlib import Path

# Adicionar src ao path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from utils import validate_prompt_structure

PROMPT_FILE = "prompts/bug_to_user_story_v2.yml"

def load_prompts(file_path: str):
    with open(file_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def get_system_prompt(prompt):
    """
    Extrai o texto do System Prompt.
    """

    return (
        prompt["kwargs"]["messages"][0]
        ["kwargs"]["prompt"]["kwargs"]["template"]
    )

class TestPrompts:

    @pytest.fixture
    def prompt(self):
        return load_prompts(PROMPT_FILE)

    def test_prompt_has_system_prompt(self, prompt):
        """Verifica se o campo existe e não está vazio."""

        system_prompt = get_system_prompt(prompt)

        assert system_prompt is not None
        assert len(system_prompt.strip()) > 0

    def test_prompt_has_role_definition(self, prompt):
        """Verifica se o prompt define uma persona."""

        system_prompt = get_system_prompt(prompt)

        assert "Você é" in system_prompt

    def test_prompt_mentions_format(self, prompt):
        """Verifica se o prompt exige formato User Story."""

        system_prompt = get_system_prompt(prompt)

        assert (
            "User Story" in system_prompt
            or "FORMATO OBRIGATÓRIO" in system_prompt
        )

    def test_prompt_has_few_shot_examples(self, prompt):
        """Verifica se existem exemplos de entrada e saída."""

        system_prompt = get_system_prompt(prompt)

        assert "EXEMPLO 1" in system_prompt
        assert "EXEMPLO 2" in system_prompt
        assert "Entrada:" in system_prompt
        assert "Saída:" in system_prompt

    def test_prompt_no_todos(self, prompt):
        """Garante que não existem TODOs pendentes."""

        system_prompt = get_system_prompt(prompt)

        assert "[TODO]" not in system_prompt
        assert "TODO" not in system_prompt

    def test_minimum_techniques(self, prompt):
        """
        Verifica se pelo menos duas técnicas foram listadas nos metadados.
        """

        metadata = (
            prompt
            .get("kwargs", {})
            .get("metadata", {})
        )

        techniques = metadata.get("techniques", [])

        assert len(techniques) >= 2

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])