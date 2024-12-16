from patchwork.patchflows.GenerateUnitTests.GenerateUnitTests import GenerateUnitTests

# Define inputs for generating unit tests
inputs = {
    "test_file_extension": "java",
    "folder_path": "/path/to/project",
    "prompt_template_file": "/path/to/custom_prompt.json"
}

# Create an instance of GenerateUnitTests step
generate_tests_step = GenerateUnitTests(inputs)

# Run the step to generate unit tests
result = generate_tests_step.run()

# Print the final inputs after generating unit tests
print(result)
