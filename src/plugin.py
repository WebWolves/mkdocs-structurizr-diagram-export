from mkdocs.plugins import BasePlugin
from mkdocs.config.base import Config
from mkdocs.config import config_options as c
from pathlib import Path
from shutil import which

from .utils import spawnProcessSync, Colors

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

    def export(self):
        if which('docker'):
            print('Start exporting diagrams on mkdocs serve command')
            spawnProcessSync('docker pull ghcr.io/aidmax/structurizr-cli-docker')
            spawnProcessSync(f'docker run --rm -v {Path.cwd()}:/root/data -w /root/data ghcr.io/aidmax/structurizr-cli-docker \
                export --workspace {self.config.workspacePath} --format {self.config.format} --output {self.config.outputPath}')
            print('Diagrams exported successfully')
        else:
            print(f'{Colors.FAIL}Error: Docker is not installed{Colors.ENDC}')
            print('Diagrams are not exported')

    def on_serve(self, server, **kwargs):
        self.export()
        return server
