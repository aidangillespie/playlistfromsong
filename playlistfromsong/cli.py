# -*- coding: utf-8 -*-

"""Console script for playlistfromsong."""

import click
from sys import exit

# For running as package
from playlistfromsong import run
from server import run_server

# # For running as script
# from playlistfromsong import run
# from server import run_server

@click.command()
@click.option('--num','-n', default=1, help='Number of songs.')
@click.option('--song','-s', default=None, help='Artist + Song to seed.')
@click.option('--bearer','-b', default=None, help='Bearer token for Spotify.')
@click.option('--folder','-f', default=None, help='Folder to save files.')
@click.option('--serve', is_flag=True, help='Start personal web server.')
@click.option('--port', default="5000", help='Internal port to run server (e.g. 5000).')
def main(num, song, bearer, folder, serve, port):
    """Console script for playlistfromsong."""
    if serve:
        click.echo("Starting server")
        run_server(folder, port)
    elif song != None:
        click.echo("Generating playlist for %d songs from '%s'" % (num, song))
        run(song, num, bearer, folder)
    else:
        click.echo("Specify a song with --song 'The Beatles Let It Be'")
        
if __name__ == "__main__":
    main()
