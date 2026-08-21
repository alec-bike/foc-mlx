"""Plotting functions.

Use polars DataFrame and Altair Chart to generate plots of FOC waveforms.
"""

from altair import Chart, ConcatChart, HConcatChart
from polars import DataFrame, col
from polars.selectors import matches


def _line_chart(df: DataFrame, regex: str, idx: str, ylab: str) -> Chart:
    """Helper function to generate Chart from DataFrame.

    Match columns by regex selector, unpivot from wide to long format.
    Generate line plot with index (x) vs matched columns (y).

    Parameters:
        df: data in DataFrame.
        regex: column selector string.
        idx: index column string.
        ylab: plot y-label string.

    Returns:
        line plot Chart.
    """
    grplab: str = "var"  # group-by label

    return (
        Chart(
            df.unpivot(
                on=matches(regex),
                index=idx,
                value_name=ylab,
                variable_name=grplab,
            ),
        )
        .mark_line(tooltip=True)
        .encode(x=idx, y=ylab, color=grplab)  # ty: ignore
    )


def plot_df(df: DataFrame) -> ConcatChart | HConcatChart:
    """Plot DataFrame waveforms.

    Returns:
        Concatenated line Chart.
    """
    # Add i_c column using 3-phase relation: i_a + i_b + i_c == 0.
    df = df.with_columns([(-col("i_a") - col("i_b")).alias("i_c")])

    return (
        _line_chart(df, "i[_].", "theta", "current (Amp)")
        | _line_chart(df, "V[_].", "theta", "voltage (Volt)")
        | _line_chart(df, "T[_].", "theta", "duty cycle")
    )
