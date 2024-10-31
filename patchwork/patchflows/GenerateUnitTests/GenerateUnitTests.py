import json
from pathlib import Path

import yaml

from patchwork.step import Step
from patchwork.steps import (
    LLM,
    ReadFile,
)

_DEFAULT_INPUT_FILE = Path(__file__).parent / "defaults.yml"
_DEFAULT_PROMPT_JSON = Path(__file__).parent / "prompt.json"

# Allow users to specify classes to test
# Automatically generate unit tests for methods in those classes
# Decide on what framework we will use for generating tests

# We'll first use pytest for this purpose


class GenerateUnitTests(Step):

    def __init__(self, inputs):
        super().__init__(inputs)

        final_inputs = yaml.safe_load(_DEFAULT_INPUT_FILE.read_text())
        self_inputs = final_inputs
        print(final_inputs)

    def run(self):
        with open(self.file, "r") as f:
            file_contents = f.read()

        return dict(file_path=self.file, file_content=file_contents)