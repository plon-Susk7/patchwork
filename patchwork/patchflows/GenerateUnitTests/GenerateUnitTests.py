import json
from pathlib import Path
import yaml

from patchwork.common.utils.step_typing import validate_steps_with_inputs
from patchwork.step import Step
from patchwork.steps import (
    LLM, 
    ReadFile,
)

_DEFAULT_INPUT_FILE = Path(__file__).parent / "defaults.yml"
_DEFAULT_PROMPT_JSON = Path(__file__).parent / "prompt.json"

class GenerateUnitTests(Step):
    def __init__(self, inputs):
        super().__init__(inputs)

        final_inputs = yaml.safe_load(_DEFAULT_INPUT_FILE.read_text())
        if final_inputs is None:
            final_inputs = {}
        
        final_inputs.update(inputs)

        # if "prompt_id" not in final_inputs.keys():
        #     final_inputs["prompt_id"] = "fixprompt"

        final_inputs["prompt_id"] = "GenerateUnitTests"
        if "prompt_template_file" not in final_inputs:
            final_inputs["prompt_template_file"] = _DEFAULT_PROMPT_JSON

        validate_steps_with_inputs(
            set(final_inputs.keys()).union({"prompt_values"}), LLM, ReadFile
        )
        print(final_inputs)
        self.inputs = final_inputs

    def run(self):
        output =ReadFile(self.inputs).run()
        self.inputs.update(output)
        self.inputs["prompt_values"] = [output]
        outputs = LLM(self.inputs).run()
        print(outputs)
        # print(output)


# Assuming you have a valid SARIF file called 'example.sarif' in the same directory
# input = {
#     "path": "/home/priyash7/Desktop/open-source/patchwork/patchwork/patchflows/GenerateUnitTests/GenerateUnitTests.py",  # Path to your SARIF file
# }

# generate_unit_tests = GenerateUnitTests(input)
# generate_unit_tests.run()
