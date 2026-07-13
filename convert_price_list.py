"""Convert GISTDA satellite price list PDF into CSV, XLSX and HTML.

Data below is transcribed directly from Gistda_Price_List.pdf (7 pages),
grouped by the same categories the source document uses, since each
category has a genuinely different column layout (optical vs radar).
"""

import pandas as pd

OUT_BASE = "Gistda_Price_List"

CATEGORY_VERY_HIGH = "รายละเอียดสูงมาก (30 – 50 ซม.)"
CATEGORY_HIGH = "รายละเอียดสูง (60 ซม. – 2 ม.)"
CATEGORY_MEDIUM = "รายละเอียดปานกลาง (มากกว่า 2 เมตร)"
CATEGORY_RADAR = "ระบบเรดาร์ (SAR)"

# Each row: [category, system(satellite/radar family), mode, resolution,
#            polarization, standard_archive, standard_tasking, unit]
rows = []

for name, res, archive, tasking in [
    ("Pléiades NEO", "30 cm.", 880, 1270),
    ("WorldView-4", "30 cm.", 920, 1560),
    ("SuperView-2", "42 cm.", 700, 1100),
    ("WorldView-1", "50 cm.", 700, 1100),
    ("WorldView-2", "50 cm.", 700, 1100),
    ("WorldView-3", "50 cm.", 700, 1100),
    ("GeoEye-1", "50 cm.", 700, 1100),
    ("Pléiades", "50 cm.", 490, 830),
    ("EarthScanner", "50 cm.", 400, 800),
    ("SuperView-1", "50 cm.", 500, 900),
    ("KOMPSAT-3", "50 cm.", 400, 700),
    ("SKYSAT", "50 cm.", 300, 560),
]:
    rows.append([CATEGORY_VERY_HIGH, name, "-", res, "-", archive, tasking, "บาท/ตร.กม."])

for name, res, archive, tasking, unit in [
    ("QuickBird", "60 cm.", 700, "N/A", "บาท/ตร.กม."),
    ("GaoFen-7", "65 cm.", 400, 700, "บาท/ตร.กม."),
    ("Jilin", "75 cm.", 300, 600, "บาท/ตร.กม."),
    ("DailyVision", "75 cm.", 300, 600, "บาท/ตร.กม."),
    ("GaoFen-2", "80 cm.", 300, 400, "บาท/ตร.กม."),
    ("IKONOS", "1 m.", 400, "N/A", "บาท/ตร.กม."),
    ("Video Constellation", "1 m.", 142500, 285000, "บาท/30 วินาที"),
    ("Night Imaging", "1 m.", 800, 1400, "บาท/ตร.กม."),
    ("SPOT-6", "1.5 m.", 190, 230, "บาท/ตร.กม."),
    ("SPOT-7", "1.5 m.", 190, 230, "บาท/ตร.กม."),
    ("ไทยโชต", "2 m.", 700, 6500, "บาท/ภาพ"),
]:
    rows.append([CATEGORY_HIGH, name, "-", res, "-", archive, tasking, unit])

for name, res, archive, tasking, unit in [
    ("LANDSAT-5", "30 m.", 150, "N/A", "บาท/ภาพ"),
    ("LANDSAT-7", "30 m.", 150, "N/A", "บาท/ภาพ"),
    ("LANDSAT-8", "30 m.", 150, "N/A", "บาท/ภาพ"),
    ("LANDSAT-9", "30 m.", 150, "N/A", "บาท/ภาพ"),
    ("PLANETSCOPE", "3 m.", 180, 240, "บาท/ตร.กม./ปี"),
]:
    rows.append([CATEGORY_MEDIUM, name, "-", res, "-", archive, tasking, unit])

RADAR_SYSTEM = "RADARSAT-2 (C band)"
for mode, res, archive, tasking in [
    ("Standard", "25 m.", 57600, 57600),
    ("Spotlight A", "1 m.", 134400, 134400),
    ("Utra-Fine", "3 m.", 86400, 86400),
    ("Wide Utra-Fine", "3 m.", 124800, 124800),
    ("Multi-Look Fine", "8 m.", 67200, 67200),
    ("Wide Multi-Look Fine", "8 m.", 120000, 120000),
    ("Fine", "8 m.", 57600, 57600),
    ("Wide", "30 m.", 57600, 57600),
    ("ScanSAR Narrow", "50 m.", "N/A", 57600),
    ("ScanSAR Wide", "100 m.", "N/A", 57600),
    ("Extended High, Low", "25 m.", 57600, 57600),
    ("Fine Quad-Pol", "8 m.", 86400, "N/A"),
    ("Wide Fine Quad-Pol", "8 m.", 124800, "N/A"),
]:
    rows.append([CATEGORY_RADAR, RADAR_SYSTEM, mode, res, "-", archive, tasking, "บาท/ภาพ"])

RADAR_SYSTEM = "TerraSar X (X band)"
for mode, res, archive, tasking in [
    ("Staring Spotlight (ST)", "0.25 m.", 162630, 325260),
    ("High Res Spotlight (HS)", "1 m.", 139230, 278460),
    ("Spotlight", "2 m.", 99450, 198900),
    ("StripMap", "3 m.", 69030, 138060),
    ("ScanSAR", "18.5 m.", 40950, 81900),
    ("Wide ScanSAR", "40 m.", 40950, 81900),
]:
    rows.append([CATEGORY_RADAR, RADAR_SYSTEM, mode, res, "-", archive, tasking, "บาท/ภาพ"])

RADAR_SYSTEM = "COSMO SkyMed (X band)"
for mode, res, polar, acquisition in [
    ("Spotlight-2", "1x1 m.", "HH, VV", 180000),
    ("StripMap Himage", "3x3–5x5 m.", "HH, HV, VH, VV", 93000),
    ("StripMap PingPong", "10x12–20x20 m.", "HH,VV หรือ HH,HV หรือ VV,VH", 68000),
    ("ScanSAR Wide", "14x22–30x30 m.", "HH, HV, VH, VV", 78000),
    ("ScanSAR Huge", "14x38–100x100 m.", "HH, HV, VH, VV", 78000),
]:
    rows.append([CATEGORY_RADAR, RADAR_SYSTEM, mode, res, polar, "-", acquisition, "บาท/ภาพ"])

RADAR_SYSTEM = "GaoFen-3 (C band)"
for mode, res, polar, archive, tasking in [
    ("Spotlight (SL)", "1 m.", "HH, VV", 116400, 180500),
    ("Ultra-fine Stripmap (UFS)", "3 m.", "HH, VV", 68900, 118800),
    ("Fine Stripmap (FSI)", "5 m.", "HH, VV", 64200, 95000),
    ("Wide Fine Stripmap (FSII)", "10 m.", "HH, HV / VV, VH", 64200, 90300),
    ("Standard Stripmap (SS)", "25 m.", "HH, HV / VV, VH", 54700, 85500),
    ("Narrow ScanSAR (NSC)", "50 m.", "HH, HV / VV, VH", 32100, 42800),
    ("Wide ScanSAR (WSC)", "100 m.", "HH, HV / VV, VH", 32100, 45800),
    ("Quad-pol Stripmap (QPSI)", "8 m.", "HH, HV / VV, VH", 71300, 137800),
    ("Wide Quad-pol Stripmap (QPSII)", "25 m.", "HH, HV / VV, VH", 71300, 137800),
    ("Wave (WAV)", "10 m.", "HH, HV / VV, VH", 10700, 14300),
    ("Global Observation (GLO)", "500 m.", "HH, HV / VV, VH", 10700, 14300),
    ("Extended Incidence Angle (EXT)", "25 m.", "HH, HV / VV, VH", 42800, 57000),
]:
    rows.append([CATEGORY_RADAR, RADAR_SYSTEM, mode, res, polar, archive, tasking, "บาท/ภาพ"])

COLUMNS = [
    "ประเภทข้อมูล (Category)",
    "ดาวเทียม/ระบบ (Satellite)",
    "โหมด (Mode)",
    "รายละเอียดภาพ (Resolution)",
    "Polarization",
    "ข้อมูลในคลัง (Standard Archive)",
    "ข้อมูลชนิดสั่งถ่าย (Standard Tasking)",
    "หน่วย (Unit)",
]

df = pd.DataFrame(rows, columns=COLUMNS)

# ---- CSV: single long-format table ----
df.to_csv(f"{OUT_BASE}.csv", index=False, encoding="utf-8-sig")

# ---- XLSX: one sheet per category ----
with pd.ExcelWriter(f"{OUT_BASE}.xlsx", engine="openpyxl") as writer:
    for category, group in df.groupby("ประเภทข้อมูล (Category)", sort=False):
        sheet_name = category[:31]
        group.drop(columns=["ประเภทข้อมูล (Category)"]).to_excel(writer, sheet_name=sheet_name, index=False)

# ---- HTML: one section per category, styled ----
html_parts = [
    "<html lang='th'><head><meta charset='utf-8'>",
    "<title>GISTDA Price List</title>",
    "<style>",
    "body{font-family:Tahoma,Arial,sans-serif;margin:2rem;color:#222}",
    "h1{font-size:1.4rem} h2{margin-top:2rem;font-size:1.1rem;color:#1a5276}",
    "table.tbl{border-collapse:collapse;width:100%;margin-bottom:1rem}",
    "table.tbl th{background:#1a5276;color:#fff;padding:6px 10px;text-align:left}",
    "table.tbl td{padding:6px 10px;border-bottom:1px solid #ddd}",
    "table.tbl tr:nth-child(even){background:#f4f6f7}",
    "</style></head><body>",
    "<h1>GISTDA Price List — ราคาข้อมูลจากดาวเทียม</h1>",
    "<p class='meta'>ที่มา: <a href='https://www.gistda.or.th/download/Gistda_Price_List.pdf'>Gistda_Price_List.pdf</a> (สทอภ. — สำนักงานพัฒนาเทคโนโลยีอวกาศและภูมิสารสนเทศ)</p>",
]

for category, group in df.groupby("ประเภทข้อมูล (Category)", sort=False):
    display_cols = [c for c in group.columns if c != "ประเภทข้อมูล (Category)"]
    if category != CATEGORY_RADAR:
        display_cols = [c for c in display_cols if c not in ("โหมด (Mode)", "Polarization")]
    html_parts.append(f"<h2>{category}</h2>")
    html_parts.append(group[display_cols].to_html(index=False, classes="tbl", border=0))

html_parts.append("</body></html>")

with open(f"{OUT_BASE}.html", "w", encoding="utf-8") as f:
    f.write("\n".join(html_parts))

print("rows:", len(df))
print(df["ประเภทข้อมูล (Category)"].value_counts())
