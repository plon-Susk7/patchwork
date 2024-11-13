flowchart TD
    subgraph "GenerateUnitTests"
        style fill:#f9f,stroke:#333,stroke-width:2px
        path1["/home/priyash7/Desktop/open-source/patchwork/patchwork/patchflows/GenerateUnitTests/GenerateUnitTests.py"] -->|Python Script| path2["/home/priyash7/Desktop/open-source/patchwork/patchwork/patchflows/GenerateUnitTests/defaults.yml"]
        path2 -->|YAML Config| path3["/home/priyash7/Desktop/open-source/patchwork/patchwork/patchflows/GenerateUnitTests/__init__.py"]
        path4["/home/priyash7/Desktop/open-source/patchwork/patchwork/patchflows/GenerateUnitTests/README.md"] -.-> path1
        path5["/home/priyash7/Desktop/open-source/patchwork/patchwork/patchflows/GenerateUnitTests/default_prompt.json"] -->|JSON Config| path1
    end
