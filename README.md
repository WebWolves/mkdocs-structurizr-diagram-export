# MkDocs Structurizr Diagram Export

Install the package with pip:

```bash
pip install git+https://github.com/WebWolves/mkdocs-structurizr-diagram-export.git
```

## Requirements
You need to have Docker installed

## Configuration
> **Note:** Default config is described below, you may similarly use `structurizr-diagram-export` plugin with any additional configuration.

```yaml
plugins:
    - structurizr-diagram-export:
        workspacePath: 'workspace.dsl' # determines workspace file location
        format: 'mermaid' # determines export format
        outputPath: 'docs/diagrams/' # determines output location
```
