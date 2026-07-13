# GEOAI — GISTDA Satellite Price List Extractor

แปลงไฟล์ PDF ราคาข้อมูลจากดาวเทียมของ [GISTDA](https://www.gistda.or.th) ให้เป็น CSV, XLSX และ HTML โดยอัตโนมัติด้วย Python

## ที่มาของข้อมูล

- ไฟล์ต้นฉบับ: [Gistda_Price_List.pdf](https://www.gistda.or.th/download/Gistda_Price_List.pdf)
- เนื้อหา: ราคาข้อมูลจากดาวเทียม Optical (30 ซม. – มากกว่า 2 เมตร) และดาวเทียมระบบเรดาร์ (SAR) รวม 64 รายการ

## ผลลัพธ์

| ไฟล์ | รายละเอียด |
|---|---|
| [`Gistda_Price_List.csv`](Gistda_Price_List.csv) | ตารางเดียว long-format แยกคอลัมน์ ประเภทข้อมูล / ดาวเทียม/ระบบ / โหมด / ราคา |
| [`Gistda_Price_List.xlsx`](Gistda_Price_List.xlsx) | แยก sheet ตามหมวดหมู่ (4 หมวด) |
| [`Gistda_Price_List.html`](Gistda_Price_List.html) | หน้าเว็บแสดงตารางราคา แยกหมวดหมู่พร้อมสไตล์ |

### ตัวอย่างผลลัพธ์

![ตัวอย่างตารางราคาข้อมูลดาวเทียม](docs/preview.png)

## วิธีใช้

### 1. ติดตั้ง environment

```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
pip install pandas openpyxl pdfplumber matplotlib
```

### 2. ดาวน์โหลดไฟล์ PDF ต้นฉบับ

```bash
curl -o Gistda_Price_List.pdf https://www.gistda.or.th/download/Gistda_Price_List.pdf
```

### 3. รันสคริปต์แปลงไฟล์

```bash
python convert_price_list.py
```

จะได้ไฟล์ `Gistda_Price_List.csv`, `.xlsx`, `.html` ในโฟลเดอร์เดียวกัน

## โครงสร้างโปรเจกต์

```
GEOAI/
├── Gistda_Price_List.pdf      # ไฟล์ต้นฉบับจาก GISTDA
├── convert_price_list.py      # สคริปต์แปลง PDF -> CSV/XLSX/HTML
├── Gistda_Price_List.csv
├── Gistda_Price_List.xlsx
├── Gistda_Price_List.html
├── make_preview_image.py      # สคริปต์สร้างภาพตัวอย่างสำหรับ README
└── docs/preview.png
```

## หมวดหมู่ข้อมูล

1. รายละเอียดสูงมาก (30 – 50 ซม.) — เช่น Pléiades NEO, WorldView-4
2. รายละเอียดสูง (60 ซม. – 2 ม.) — เช่น QuickBird, SPOT-6/7, ไทยโชต
3. รายละเอียดปานกลาง (มากกว่า 2 เมตร) — LANDSAT, PLANETSCOPE
4. ระบบเรดาร์ (SAR) — RADARSAT-2, TerraSAR X, COSMO SkyMed, GaoFen-3
