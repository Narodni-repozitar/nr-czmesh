from pathlib import Path

import click

from nr_czmesh import run


@click.command("czmesh")
@click.option("-i", "--input", type=str, help="It is path of .mrc file")
@click.option("-o", "--output", type=str, help="File where ")
def czmesh(output: str = None, input: str = None):
    """
    Programme for translating information from mrc file to csv.
    """
    if not input:
        input = str(
            Path(__file__).parent.absolute() / ".." / "data" / "2020" / "MeSH2020_Marc21-DW.mrc")
    if not output:
        output = str(Path().absolute() / 'czmesh.csv')
    assert output.endswith(".csv"), "Output file have to end with .csv"
    assert input.endswith("mrc"), "Input file have to end with .csv"
    run(input, output)
