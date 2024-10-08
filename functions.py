import os
import shutil

import pyfiglet
from InquirerPy import inquirer
from tabulate import tabulate

from bar_chart import get_bar_chart_app
from dashboard import get_dashboard_app
from data import get_fruit_df
from pizza_chart import get_pizza_chart_app
from scatter_plot import get_scatter_plot_app
from tree_graph import get_tree_graph_app


def center_figlet_text(figlet_text):
    lines = figlet_text.split("\n")
    try:
        terminal_width = os.get_terminal_size().columns
        centered_lines = [
            line.center(terminal_width) for line in lines if line.strip() != ""
        ]
        return "\n".join(centered_lines)
    except OSError:
        print("Please run this script in a terminal")
        exit()


def center_menu_options(text):
    total_width = shutil.get_terminal_size().columns - 10
    text_length = len(text)
    total_spaces = total_width - text_length - 2
    left_spaces = total_spaces // 2
    right_spaces = total_spaces - left_spaces

    return f"--<{' ' * left_spaces}{text}{' ' * right_spaces}>--"


def menu():
    header = pyfiglet.figlet_format("DuBI")
    centered_header = center_figlet_text(header)
    print("\n" + centered_header + "\n")

    options = [
        "Gráfico de barras",
        "Gráfico de pizza",
        "Gráfico de árvores",
        "Gráfico de dispersão",
        "Dashboard",
        "Base de dados",
        "Sair",
    ]

    centered_options = [center_menu_options(option) for option in options]

    choice = inquirer.select(
        message="\n",
        instruction="Selecione uma opção ('Ctrl'+'C' para sair):",
        choices=centered_options,
        default=centered_options[0],
        wrap_lines=False,
        border=True,
        pointer="👉",
        qmark="$",
    ).execute()

    if "Gráfico de barras" in choice:
        get_bar_chart_app(data=get_fruit_df())
    elif "Gráfico de pizza" in choice:
        get_pizza_chart_app(data=get_fruit_df())
    elif "Gráfico de árvores" in choice:
        get_tree_graph_app(data=get_fruit_df())
    elif "Gráfico de dispersão" in choice:
        get_scatter_plot_app(data=get_fruit_df())
    elif "Dashboard" in choice:
        get_dashboard_app(data=get_fruit_df())
    elif "Base de dados" in choice:
        print(tabulate(get_fruit_df(), headers="keys", tablefmt="pretty"))
    elif "Sair" in choice:
        print("Até mais!")
        exit()
