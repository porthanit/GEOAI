"""Render a preview image of the price list table for the README."""

import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# use a Thai-capable font if available, else fall back to default
for candidate in ["Tahoma", "Leelawadee UI", "Segoe UI"]:
    matches = [f.name for f in fm.fontManager.ttflist if candidate.lower() in f.name.lower()]
    if matches:
        plt.rcParams["font.family"] = matches[0]
        break

df = pd.read_csv("Gistda_Price_List.csv", keep_default_na=False, na_values=[])
preview = df[df["ประเภทข้อมูล (Category)"] == "รายละเอียดสูงมาก (30 – 50 ซม.)"]
preview = preview[
    ["ดาวเทียม/ระบบ (Satellite)", "รายละเอียดภาพ (Resolution)",
     "ข้อมูลในคลัง (Standard Archive)", "ข้อมูลชนิดสั่งถ่าย (Standard Tasking)", "หน่วย (Unit)"]
]
col_labels = [
    "ดาวเทียม/ระบบ\n(Satellite)", "รายละเอียดภาพ\n(Resolution)",
    "ข้อมูลในคลัง\n(Standard Archive)", "ข้อมูลชนิดสั่งถ่าย\n(Standard Tasking)", "หน่วย\n(Unit)",
]

fig, ax = plt.subplots(figsize=(10, 4.6))
ax.axis("off")
ax.set_title("GISTDA Price List — รายละเอียดสูงมาก (30 – 50 ซม.)", fontsize=13, weight="bold", pad=14)

table = ax.table(
    cellText=preview.values,
    colLabels=col_labels,
    colWidths=[0.24, 0.19, 0.22, 0.22, 0.16],
    cellLoc="center",
    loc="center",
)
table.auto_set_font_size(False)
table.set_fontsize(9)
table.scale(1, 1.8)

for (row, col), cell in table.get_celld().items():
    if row == 0:
        cell.set_facecolor("#1a5276")
        cell.set_text_props(color="white", weight="bold")
    elif row % 2 == 0:
        cell.set_facecolor("#f4f6f7")

plt.tight_layout()
plt.savefig("docs/preview.png", dpi=150, bbox_inches="tight")
print("saved docs/preview.png")
