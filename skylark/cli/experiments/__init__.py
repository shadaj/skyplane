import typer
from skylark.cli.experiments.util import get_max_throughput, util_grid_throughput, util_grid_cost
from skylark.cli.experiments.profile import latency_grid, throughput_grid

app = typer.Typer(name="experiments")
app.command()(latency_grid)
app.command()(throughput_grid)
app.command()(get_max_throughput)
app.command()(util_grid_throughput)
app.command()(util_grid_cost)
