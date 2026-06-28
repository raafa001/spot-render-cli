import click
import requests

from .config import load_config, save_config


@click.command()
@click.option("--file", "file_path", type=click.Path(exists=True), required=True)
@click.option("--project", required=True)
@click.option("--variation", required=True)
@click.option("--api", "api_url", default="http://localhost:8000")
def main(file_path, project, variation, api_url):
    cfg = load_config()
    artist = cfg.get("artist")
    if not artist:
        artist = click.prompt("Qual é o seu nome?")
        cfg["artist"] = artist
        save_config(cfg)

    data = {"project": project, "variation": variation, "artist": artist}
    with open(file_path, "rb") as fh:
        files = {"file": fh}
        resp = requests.post(f"{api_url}/uploads/", files=files, data=data, timeout=60)
        resp.raise_for_status()
        click.echo(resp.json())
