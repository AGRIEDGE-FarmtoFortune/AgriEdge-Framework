import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls

def set_cell_background(cell, fill_hex):
    tcPr = cell._element.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._element.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

doc = docx.Document()

# Page Margins
sections = doc.sections
for section in sections:
    section.top_margin = Inches(0.75)
    section.bottom_margin = Inches(0.75)
    section.left_margin = Inches(0.75)
    section.right_margin = Inches(0.75)

# Styling Constants
COLOR_PRIMARY = RGBColor(6, 78, 59)      # Deep Emerald (#064e3b)
COLOR_SECONDARY = RGBColor(5, 150, 105)  # Emerald 600 (#059669)
COLOR_TEXT = RGBColor(15, 23, 42)        # Slate 900 (#0f172a)
COLOR_MUTED = RGBColor(71, 85, 105)      # Slate 600 (#475569)

# Base Style setup
style_normal = doc.styles['Normal']
style_normal.font.name = 'Calibri'
style_normal.font.size = Pt(10.5)
style_normal.font.color.rgb = COLOR_TEXT

# Title
p_title = doc.add_paragraph()
p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
run_title = p_title.add_run("🚜 Farm-to-Fortune (Agri-Edge)")
run_title.font.size = Pt(22)
run_title.font.bold = True
run_title.font.color.rgb = COLOR_PRIMARY

p_sub = doc.add_paragraph()
p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
run_sub = p_sub.add_run("Prototype Step-by-Step Process & Workflow Guide")
run_sub.font.size = Pt(13)
run_sub.font.bold = True
run_sub.font.color.rgb = COLOR_SECONDARY
p_sub.paragraph_format.space_after = Pt(16)

# Callout Banner
table_banner = doc.add_table(rows=1, cols=1)
table_banner.alignment = WD_TABLE_ALIGNMENT.CENTER
cell_b = table_banner.cell(0, 0)
set_cell_background(cell_b, "ecfdf5")  # Emerald-50
set_cell_margins(cell_b, top=140, bottom=140, left=200, right=200)

p_b = cell_b.paragraphs[0]
r_b1 = p_b.add_run("📋 Overview of Prototype Execution:\n")
r_b1.bold = True
r_b1.font.color.rgb = COLOR_PRIMARY
r_b1.font.size = Pt(11)

r_b2 = p_b.add_run(
    "Yeh document hamare Farm-to-Fortune (Agri-Edge) Web Prototype (index.html) ke andar hone wali har ek process "
    "ko kadam-ba-kadam (step-by-step) detail mein samjhata hai. Internal Hackathon judges ke saamne live demo dete waqt "
    "kya kya click hota hai, peeche kya logic chalta hai, aur screen par kya badalta hai — woh sab yahan likha hai."
)
r_b2.font.size = Pt(10)
r_b2.font.color.rgb = COLOR_TEXT

doc.add_paragraph().paragraph_format.space_after = Pt(12)

# Section 1: Process Flow Diagram
p_h1 = doc.add_heading(level=1)
r_h1 = p_h1.add_run("1. 🔄 Complete End-to-End Workflow Map")
r_h1.font.color.rgb = COLOR_PRIMARY
r_h1.font.bold = True

p_flow = doc.add_paragraph()
p_flow.paragraph_format.space_after = Pt(12)
r_flow = p_flow.add_run(
    "[Step 1: Kisan Login & Node Handshake]\n"
    "       ↓\n"
    "[Step 2: Crop Sample Selection & Optical AI Scan]\n"
    "       ↓\n"
    "[Step 3: Defect Segmentation & Grade A/B/C Verdict]\n"
    "       ↓\n"
    "[Step 4: Dynamic SVG QR Quality Certificate & Hash]\n"
    "       ↓\n"
    "[Step 5: APMC Mandi Price Matching & Trade Lock]\n"
    "       ↓\n"
    "[Step 6: Cold-Chain IoT Transit Telemetry Monitoring]\n"
    "       ↓\n"
    "[Step 7: Pitch Presentation Live Demo Simulation]"
)
r_flow.font.name = 'Consolas'
r_flow.font.size = Pt(9.5)
r_flow.font.color.rgb = COLOR_SECONDARY
p_flow.alignment = WD_ALIGN_PARAGRAPH.CENTER


# Section 2: Detailed Steps
p_h2 = doc.add_heading(level=1)
r_h2 = p_h2.add_run("2. 📌 Step-by-Step Detailed Process Explanation")
r_h2.font.color.rgb = COLOR_PRIMARY
r_h2.font.bold = True

steps_data = [
    {
        "step": "STEP 1: Kisan Authentication & Edge Node Handshake",
        "action": "Kisan portal screen par aata hai aur login select karta hai.",
        "details": [
            "Language Selector: Top-right pills (EN | हिंदी | मराठी) se language switch kar sakta hai. Poori UI instantly translate ho jaati hai.",
            "Dual Login Modes: Tab toggle karke Mobile OTP (+91 9823011409, auto OTP 4109) ya Kisan ID / Aadhaar Number (KCC-MH-2026-8941) se login kar sakta hai.",
            "Demo Quick Login (Judge Special): 1-click 'Demo Quick Login (Farmer Profile)' button par click karke typing bypass karke turant enter ho sakta hai.",
            "Node Credential Loader: Login click karte hi ek full-screen loading spinner overlay aata hai: 'Verifying Node Credentials & Edge Keys...' jo ESP32 Edge Node #MH-FPO-04 ke hardware verification ko simulate karta hai."
        ]
    },
    {
        "step": "STEP 2: Real-Time Optical AI Grading Booth (The Core AI Demo)",
        "action": "Kisan Edge Booth camera viewport ke samne fasal rakhta hai aur inspect karta hai.",
        "details": [
            "Crop Sample Selector: Top dropdown se crop select kar sakta hai — 🍅 Fresh Tomatoes, 🍎 Red Apples, 🥭 Alphonso Mangoes, ya 🧅 Red Onions.",
            "Simulated Camera Viewport: Black optical chamber viewport ke andar crop ka SVG visual, camera reticle crosshairs, aur AI bounding box (Confidence: 98.6%) dikhta hai.",
            "Scan New Batch Button: 'Scan New Batch' click karte hi 2-second ke liye green laser scan sweep beam viewport par chalti hai.",
            "Web Audio Beep Synth: Scan hone par browser-native sound synthesizer high-tech laser scan beep play karta hai.",
            "AI Metric Analysis: Optical AI model crop ka Defect % (e.g. 1.8%), Color Uniformity % (96.2%), aur Moisture % (11.5%) analyze karke final Quality Verdict badge generate karta hai (GRADE A - Export / Premium, GRADE B, ya GRADE C)."
        ]
    },
    {
        "step": "STEP 3: Dynamic Digital Quality Certificate Generation",
        "action": "Inspected crop ka tamper-proof digital quality proof generate hota hai.",
        "details": [
            "Digital Certificate Modal: Kisan 'Digital Certificate' button par click karta hai.",
            "Dynamic SVG QR Matrix: JS runtime mein ek real SVG QR code matrix generate hoti hai jisme batch data encode rehta hai.",
            "Encrypted Metadata: Batch ID (BATCH-2026-8941), Inspected Crop Grade, Inspection Time (IST), aur Cryptographic Hash (0x8f3a9c1e...4109) dikhta hai.",
            "Share / Print Action: 'Share / Print Certificate' click karne par cryptographic hash clipboard par copy ho jata hai aur success toast alert aata hai."
        ]
    },
    {
        "step": "STEP 4: APMC Mandi Real-Time Price Matching & Price Lock",
        "action": "Grade ke aadhar par direct APMC mandi bhav match karke middleman cut bypass hota hai.",
        "details": [
            "Grade-Mapped Market Table: Inspected Grade A Tomato ke liye nearby mandis ke rates compare hote hain — Pune APMC (₹42/kg - Recommended Highest), Vashi Mandi (₹39/kg), Nashik APMC (₹37/kg), vs Unregulated Middleman Rate (₹31/kg crossed out).",
            "+28% Farmer Margin Gain Callout: Direct callout card dikhata hai ki middlemen bypass karne se farmer ko ₹11/kg extra direct revenue milta hai.",
            "Trade Price Lock Modal: 'Lock Price' click karne par contract window khulti hai:",
            "  • Batch Weight Slider: 100 kg se 2000 kg tak slider move karke total volume adjust kar sakta hai.",
            "  • Automatic Payout Calculator: 500 kg @ ₹42/kg = ₹21,000 live calculate hota hai.",
            "  • Cold-Chain Pickup Slot: Cold truck transport slot select kar sakta hai.",
            "  • Confirm Contract: Click karte hi Transport Pass #TR-8941 issue ho jata hai."
        ]
    },
    {
        "step": "STEP 5: Cold-Chain IoT Transit Telemetry Monitoring",
        "action": "Khet se mandi tak transport ke dauran fasal ko kharab hone se bachane ke liye IoT monitoring hoti hai.",
        "details": [
            "Vehicle Tracker Card: Transport Truck #MH-12-AZ-9981 (Pune to Vashi Cold Corridor NH-48) live tracking card.",
            "Live Sensor Gauges: Internal Temperature (18.4°C), Relative Humidity (62%), aur GPS Geofence Status (Active).",
            "Chart.js Telemetry Graph: 12-hour historical trend line graph Internal Temp aur Humidity levels ko continuous emerald/teal curves mein plot karta hai taaki cold-chain breakdown na ho."
        ]
    },
    {
        "step": "STEP 6: Pitch Presentation Live Demo Simulation Mode",
        "action": "Presentation ke dauran judges ke samne screen ko bina kisi touch ke continuously live run karna.",
        "details": [
            "Floating Control Button: Screen ke bottom-right mein 'Demo Mode: Simulate Live Inflow' floating button.",
            "5-Second Automated Inflow Loop: Enable karte hi har 5 second mein naye crop batch scan hote hain, defect % randomize hota hai, Chart.js telemetry line mein naya data point add hota hai, aur toast notifications aati hain."
        ]
    }
]

for s in steps_data:
    p_s_title = doc.add_paragraph()
    r_st = p_s_title.add_run(s["step"])
    r_st.font.size = Pt(11.5)
    r_st.font.bold = True
    r_st.font.color.rgb = COLOR_PRIMARY
    p_s_title.paragraph_format.space_before = Pt(10)
    p_s_title.paragraph_format.space_after = Pt(2)

    p_act = doc.add_paragraph()
    r_act = p_act.add_run(f"Process Goal: {s['action']}")
    r_act.font.italic = True
    r_act.font.size = Pt(9.5)
    r_act.font.color.rgb = COLOR_MUTED
    p_act.paragraph_format.space_after = Pt(4)

    for d in s["details"]:
        p_d = doc.add_paragraph(style='List Bullet')
        r_d = p_d.add_run(d)
        r_d.font.size = Pt(10)
        p_d.paragraph_format.space_after = Pt(3)

doc.add_paragraph().paragraph_format.space_after = Pt(10)

# Section 3: Summary Table
p_h3 = doc.add_heading(level=1)
r_h3 = p_h3.add_run("3. 📊 Prototype UI Component to Process Mapping Table")
r_h3.font.color.rgb = COLOR_PRIMARY
r_h3.font.bold = True

table_map = doc.add_table(rows=1, cols=3)
table_map.alignment = WD_TABLE_ALIGNMENT.CENTER
hdr_cells = table_map.rows[0].cells
headers = ["UI Component in index.html", "Triggered Process / Action", "Backend / Hardware Hardware Vision"]

for i, h in enumerate(headers):
    hdr_cells[i].text = h
    set_cell_background(hdr_cells[i], "064e3b")
    p = hdr_cells[i].paragraphs[0]
    p.runs[0].font.bold = True
    p.runs[0].font.color.rgb = RGBColor(255, 255, 255)
    p.runs[0].font.size = Pt(9)

mapping_rows = [
    ("Language Switcher Pills (EN/HI/MR)", "Dynamic UI Dictionary Translation", "Frontend Translation Dictionary Engine"),
    ("Demo Quick Login Button", "Instant Auth Bypass & Node Handshake", "ESP32 Security Key Verification Simulation"),
    ("Crop Type Selector Dropdown", "Renders Crop SVG & Defect Preset", "Camera Frame Buffer Selection"),
    ("Scan New Batch Button", "2-Sec Laser Animation + Beep Audio", "ESP32-S3 TFLite Micro Model Defect Inference"),
    ("Digital Certificate Button", "Renders SVG QR Code & Hash Modal", "Blockchain / Tamper-Proof Cryptographic Hash"),
    ("APMC Lock Price Button", "Opens Trade Calculator & Volume Slider", "Direct Mandi Co-op Buyout API Contract"),
    ("Chart.js Telemetry Graph", "Appends Real-Time Temp/Humidity Data", "MQTT GSM Sensor Stream from Truck IoT Module"),
    ("Floating Demo Mode Toggle", "Auto 5s Inflow Loop Interval", "Continuous Production Pipeline Simulation")
]

for row_data in mapping_rows:
    row_cells = table_map.add_row().cells
    for i, item in enumerate(row_data):
        row_cells[i].text = item
        set_cell_margins(row_cells[i], top=80, bottom=80, left=100, right=100)
        p = row_cells[i].paragraphs[0]
        p.runs[0].font.size = Pt(8.5)

# Save Document
docx_filename = "c:/Users/acer/Documents/AGRIEDGE/Farm_to_Fortune_Prototype_Process_Guide.docx"
doc.save(docx_filename)
print("Docx created successfully at:", docx_filename)
