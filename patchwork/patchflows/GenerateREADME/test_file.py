import unittest
from unittest.mock import patch
from pathlib import Path
from patchwork.patchflows.GenerateREADME.GenerateREADME import GenerateREADME

class TestGenerateREADME(unittest.TestCase):

    @patch("patchwork.patchflows.GenerateREADME.GenerateREADME.Path")
    @patch("patchwork.patchflows.GenerateREADME.GenerateREADME.yaml")
    def test_init(self, mock_yaml, mock_path):
        inputs = {"key": "value"}
        generate_readme = GenerateREADME(inputs)
        self.assertEqual(generate_readme.inputs["branch_prefix"], "generatereadme-")
        self.assertEqual(generate_readme.inputs["prompt_template_file"], mock_path.return_value / "generate_readme_prompt.json")
        self.assertEqual(generate_readme.inputs["prompt_id"], "generateREADME")
        self.assertEqual(generate_readme.inputs["folder_path"], Path.cwd())
        self.assertEqual(generate_readme.inputs["pr_title"], "PatchWork GenerateREADME")

    @patch("patchwork.patchflows.GenerateREADME.GenerateREADME.CallCode2Prompt")
    @patch("patchwork.patchflows.GenerateREADME.GenerateREADME.LLM")
    @patch("patchwork.patchflows.GenerateREADME.GenerateREADME.ModifyCode")
    @patch("patchwork.patchflows.GenerateREADME.GenerateREADME.PR")
    def test_run(self, mock_pr, mock_modify, mock_llm, mock_call_code):
        generate_readme = GenerateREADME({})
        generate_readme.inputs = {"modified_code_files": ["file1.py", "file2.py"]}
        mock_call_code.return_value.run.return_value = {"prompt_values": "prompt", "response_partitions": {"patch": []}}
        mock_llm.return_value.run.return_value = {"llm_output": "llm"}
        mock_modify.return_value.run.return_value = {"modified_code_files": ["file1.py", "file2.py"]}
        mock_pr.return_value.run.return_value = {"pr_output": "pr"}
        
        result = generate_readme.run()
        
        self.assertEqual(result["pr_header"], "This pull request from patchwork adds 2 READMEs.")
        self.assertEqual(result["pr_output"], "pr")

if __name__ == '__main__':
    unittest.main()
