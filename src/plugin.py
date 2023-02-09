from mkdocs.plugins import BasePlugin
from mkdocs.config.base import Config
from mkdocs.config import config_options as c
from pathlib import Path

from .utils import spawnProcessSync

class ExportStructurizrDiagramsConfig(Config):
    """defines the plugin configuration"""
    # determines workspace file location
    workspacePath = c.Type(str, default='workspace.dsl')

    # determines export format
    format = c.Type(str, default='mermaid')

    # determines output location
    outputPath = c.Type(str, default='docs/diagrams/')


class ExportStructurizrDiagrams(BasePlugin[ExportStructurizrDiagramsConfig]):
    """Export Structurizr diagrams to defined format"""

    def export(self, config):
        spawnProcessSync('docker pull ghcr.io/aidmax/structurizr-cli-docker')
        spawnProcessSync(f'docker run --rm -v {Path.cwd()}:/root/data -w /root/data ghcr.io/aidmax/structurizr-cli-docker \
            export --workspace {self.config.workspacePath} --format {self.config.format} --output {self.config.outputPath}')

    def on_serve(self, config):
        self.export()
