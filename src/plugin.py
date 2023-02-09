from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options as c
from pathlib import Path

from .utils import spawnProcessSync

class ExportStructurizrDiagrams(BasePlugin):
    """Export Structurizr diagrams to defined format"""

    config_scheme = (
        # determines workspace file name
        ('workspacePath', c.Type(str, default='workspace.dsl')),
        # determines export format
        ('format', c.Type(str, default='mermaid')),
        # determines output location
        ('outputPath', c.Type(str, default='docs/diagrams/'))
    )

    def export(self):
        spawnProcessSync('docker pull ghcr.io/aidmax/structurizr-cli-docker')
        spawnProcessSync(f'docker run --rm -v {Path.cwd()}:/root/data -w /root/data ghcr.io/aidmax/structurizr-cli-docker \
            export --workspace {self.config.workspacePath} --format {self.config.format} --output {self.config.outputPath}')

    def on_serve(self):
        self.export()
