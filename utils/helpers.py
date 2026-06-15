from rich.console import Console
from rich.table import Table

console = Console()


def print_table(title, columns, rows):
    table = Table(title=title)

    for col in columns:
        table.add_column(col)

    for row in rows:
        table.add_row(*row)

    console.print(table)