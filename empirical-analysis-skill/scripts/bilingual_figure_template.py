#!/usr/bin/env python3
"""Template for bilingual empirical figure finalization.

This script is intentionally generic. It expects plotting data that were
exported from Stata or generated from a confirmed Python replication script.
Use project-specific wrappers for model estimation, but keep final plotting
language, font, and layout logic centralized and auditable.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import pandas as pd


DEFAULT_CN_FONTS = ["SimSun", "Songti SC", "STSong", "Songti", "Arial Unicode MS"]
DEFAULT_EN_FONTS = ["Times New Roman"]


def resolve_font(candidates: list[str]) -> str:
    """Return the first installed font family from candidates, or fail loudly."""
    installed = {font.name for font in fm.fontManager.ttflist}
    for name in candidates:
        if name in installed:
            return name
    raise SystemExit(
        "Required figure font not found. Tried: " + ", ".join(candidates)
    )


def set_language_font(lang: str, cn_fonts: list[str], en_fonts: list[str]) -> str:
    if lang == "cn":
        font = resolve_font(cn_fonts)
        plt.rcParams["font.family"] = font
        plt.rcParams["font.sans-serif"] = [font]
        plt.rcParams["axes.unicode_minus"] = False
    elif lang == "en":
        font = resolve_font(en_fonts)
        plt.rcParams["font.family"] = font
        plt.rcParams["font.serif"] = [font]
        plt.rcParams["axes.unicode_minus"] = True
    else:
        raise SystemExit(f"Unsupported language: {lang}")
    return font


def load_labels(path: Path, lang: str) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if lang not in data:
        raise SystemExit(f"Label config must contain a '{lang}' object.")
    return data[lang]


def draw_line_figure(
    plot_data: Path,
    label_config: Path,
    output: Path,
    lang: str,
    x_col: str,
    y_col: str,
    group_col: str | None,
    cn_fonts: list[str],
    en_fonts: list[str],
    dpi: int,
) -> None:
    font = set_language_font(lang, cn_fonts, en_fonts)
    labels = load_labels(label_config, lang)
    df = pd.read_csv(plot_data)

    required = {x_col, y_col}
    if group_col:
        required.add(group_col)
    missing = required.difference(df.columns)
    if missing:
        raise SystemExit(f"Plot data missing required columns: {sorted(missing)}")

    fig, ax = plt.subplots(figsize=tuple(labels.get("figsize", [8.8, 5.6])))

    colors = labels.get(
        "colors",
        ["#4A90E2", "#50A878", "#F5A623", "#D0021B", "#7E57C2", "#4D4D4D"],
    )

    if group_col:
        for idx, (group, gdf) in enumerate(df.groupby(group_col, sort=False)):
            group_labels = labels.get("groups", {})
            shown_label = group_labels.get(str(group), str(group))
            ax.plot(
                gdf[x_col],
                gdf[y_col],
                label=shown_label,
                color=colors[idx % len(colors)],
                linewidth=2.4,
            )
    else:
        ax.plot(df[x_col], df[y_col], color=colors[0], linewidth=2.4)

    ax.axhline(0, color="#333333", linewidth=0.9, alpha=0.45)
    ax.grid(True, color="#eeeeee", linewidth=0.8)
    ax.set_facecolor("white")
    ax.set_title(labels.get("title", ""), fontsize=15, fontweight="bold", pad=16)
    ax.set_xlabel(labels.get("xlabel", x_col), fontsize=12, labelpad=8)
    ax.set_ylabel(labels.get("ylabel", y_col), fontsize=12, labelpad=8)

    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)
    for spine in ["left", "bottom"]:
        ax.spines[spine].set_color("#333333")
        ax.spines[spine].set_linewidth(1.0)

    ax.tick_params(axis="both", labelsize=10)

    if group_col:
        legend = labels.get("legend", {})
        ax.legend(
            loc=legend.get("loc", "upper center"),
            bbox_to_anchor=tuple(legend.get("bbox_to_anchor", [0.5, -0.14])),
            ncol=int(legend.get("ncol", 2)),
            frameon=False,
            fontsize=10,
        )

    note = labels.get("note")
    if note:
        fig.text(0.01, 0.01, note, ha="left", va="bottom", fontsize=9)

    output.parent.mkdir(parents=True, exist_ok=True)
    fig.tight_layout()
    fig.savefig(output, dpi=dpi, bbox_inches="tight")
    plt.close(fig)

    print(
        json.dumps(
            {
                "output": str(output),
                "language": lang,
                "font": font,
                "plot_data": str(plot_data),
                "x": x_col,
                "y": y_col,
                "group": group_col,
            },
            ensure_ascii=False,
            indent=2,
        )
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--plot-data", required=True, type=Path)
    parser.add_argument("--label-config", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--lang", required=True, choices=["cn", "en"])
    parser.add_argument("--x-col", default="x")
    parser.add_argument("--y-col", default="y")
    parser.add_argument("--group-col")
    parser.add_argument("--cn-font", action="append", default=[])
    parser.add_argument("--en-font", action="append", default=[])
    parser.add_argument("--dpi", type=int, default=600)
    args = parser.parse_args()

    draw_line_figure(
        plot_data=args.plot_data,
        label_config=args.label_config,
        output=args.output,
        lang=args.lang,
        x_col=args.x_col,
        y_col=args.y_col,
        group_col=args.group_col,
        cn_fonts=args.cn_font or DEFAULT_CN_FONTS,
        en_fonts=args.en_font or DEFAULT_EN_FONTS,
        dpi=args.dpi,
    )


if __name__ == "__main__":
    main()
