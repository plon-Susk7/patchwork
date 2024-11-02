```python
import pytest
from patchwork.steps import Patchflows
from patchflows.GenerateUnitTests import GenerateUnitTests
from patchwork.common.utils.step_typing import LLM

# Initialize Patchflows with GenerateUnitTests step
patchflows_step = GenerateUnitTests({
    "prompt_id": "GenerateUnitTests",
    "folder_path": "./tests", 
