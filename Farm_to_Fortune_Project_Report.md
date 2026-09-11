# 🚜 Farm-to-Fortune (Agri-Edge) — Comprehensive Project Architecture & Technical Roadmap Report

**Project Name**: Farm-to-Fortune (Agri-Edge)  
**One-Line Pitch**: An on-device AI and IoT hardware ecosystem designed to automate crop grading, prevent post-harvest cold-chain losses, and ensure fair APMC mandi pricing for farmers.  
**Target Audience**: Internal Hackathon Judges, Technical Evaluators, & Project Team Members  

---

## 📌 Executive Summary

This document presents a comprehensive technical breakdown of the **Farm-to-Fortune (Agri-Edge)** platform. It details the **Frontend Prototype** built for judges during the internal hackathon, how it simulates the end-to-end system vision, and the **Technical Roadmap & Pending Work** required to turn this prototype into a full hardware-integrated, production-scale Agri-Tech product.

---

## 1. 🎯 Problem & Solution Overview

### The Core Problem
1. **Manual & Biased Crop Grading**: Mandi traders/middlemen rely on subjective visual inspection, often under-grading high-quality crops to Grade-C to maximize trader margins at the farmer's expense.
2. **Lack of Certified Quality Proof**: Farmers lack a tamper-proof digital certificate to prove their crop's premium quality to external buyers or distant mandis.
3. **Transit Spoilage (25-30% Losses)**: Poor temperature and humidity regulation during transit between farm gates and distant mandis causes massive post-harvest wastage.

### The Agri-Edge Solution
- **Edge-AI Grading Booth**: On-farm optical booth with camera + local TinyML model for offline, instant (<200 ms) crop defect classification and grade verdict (Grade A/B/C).
- **Sensor Fusion**: Capacitive moisture sensors and DHT environmental sensors test crop moisture and ambient conditions.
- **Tamper-Proof Digital QR Certificate**: Encodes batch ID, grade verdict, moisture %, timestamp, and cryptographic hash into a verifiable QR code.
- **IoT Cold-Chain Telemetry & Mandi Discovery**: Real-time vehicle monitoring (Temp, Humidity, GPS) linked with direct APMC market price discovery to eliminate middleman cuts.

---

## 2. 💻 What We Have Built (Current Interactive Frontend Prototype)

To create an impactful, interactive live demo for hackathon judges, we developed a standalone, production-ready Web Application in **`index.html`**.

### Frontend Technology Stack Used:
- **HTML5 & Vanilla JavaScript State Engine**: Zero external framework overhead; state handles language switching, auth flow, crop selection, metrics generation, canvas animations, and modal windows.
- **Tailwind CSS (via CDN)**: Custom dark emerald aesthetic (`#080d0b`, `#065f46`), glassmorphism card overlays (`backdrop-blur-md`), keyframe animations (laser scan sweep, float effects, glowing borders).
- **Lucide Icons Library**: Scalable UI icons for sensors, hardware nodes, vehicle tracking, APMC mandis, and QR certificates.
- **Chart.js (via CDN)**: Interactive 12-hour cold-chain IoT telemetry line chart plotting real-time Temperature (°C) and Relative Humidity (%) trends with emerald gradients.
- **Web Audio API**: Browser-native sound synthesizer generating high-tech laser scan sweep sound effects and button feedback without requiring external audio MP3 assets.

---

### Implemented Frontend Modules & Features:

| Module | Feature Implemented in Frontend Demo | Judge Impact / Purpose |
| :--- | :--- | :--- |
| **Authentication Portal** | Dual-login switch (**Mobile OTP** & **Kisan ID/Aadhaar**), **Language Switcher (EN, हिंदी, मराठी)**, & 1-Click **"Demo Quick Login"**. | Demonstrates accessibility for rural farmers in regional languages and allows instant judge login bypass. |
| **Node Loader** | Simulated "Verifying Node Credentials & Edge Keys..." spinner overlay. | Mimics ESP32 hardware handshake and TinyML model sync before entering the main dashboard. |
| **KPI Telemetry Bar** | 4 Summary KPI Cards: Total Batches (1,248), Pass Rate (87.4%), Avg Moisture (11.2%), Active Transit (4 In-Route). | Gives judges an immediate high-level overview of farm cooperative operations. |
| **Optical AI Grading Booth** | Crop sample selector (Tomatoes 🍅, Apples 🍎, Mangoes 🥭, Onions 🧅), simulated camera viewport with AI bounding boxes, laser beam scan animation, live metrics (defect %, color %, moisture %), and **Grade A/B/C** verdict badge. | Core interactive demo showing how AI visual inspection operates at the farm gate. |
| **Digital Quality Certificate** | Modal rendering a dynamic **SVG QR Code matrix**, Batch ID (`BATCH-2026-8941`), timestamp, cryptographic verification hash (`0x8f3a...`), and share action. | Demonstrates tamper-proof verification for buyers and cooperative transparent ledgers. |
| **APMC Mandi Price Matching** | Comparison table mapping crop grade to Pune APMC (₹42/kg), Vashi Mandi (₹39/kg), Nashik APMC (₹37/kg) vs Middleman cut (₹31/kg), with **+28% Net Margin Gain** callout. | Highlights the economic value proposition for farmers bypassing middleman exploitation. |
| **Price Lock & Pickup Modal** | Interactive trade modal with weight slider (100kg-2000kg), automatic payout calculator (₹21,000), pickup slot selector, and transport pass issuer. | Shows end-to-end commercial transaction flow from grading to logistics booking. |
| **Cold-Chain IoT Telemetry** | Truck `#MH-12-AZ-9981` tracking card, live sensor gauges (Temp 18.4°C, Humidity 62%), and Chart.js historical trend line graph. | Demonstrates real-time post-harvest spoilage prevention along transport corridors. |
| **Pitch Demo Mode** | Floating **"Demo Mode: Simulate Live Inflow"** button auto-triggering crop scans, sensor data updates, chart data appends, and live toast alerts every 5 seconds. | Keeps the dashboard dynamic and self-running during pitch presentations. |

---

## 3. 🚧 What Remains to be Built (Technical Roadmap & Backend Pipeline)

While the frontend prototype successfully simulates the user experience and feature flow, the following hardware, AI model training, and backend cloud infrastructure components are pending for full product deployment:

```
+-----------------------------------------------------------------------------------+
|                            FULL PRODUCT ARCHITECTURE                              |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|  [ HARDWARE LAYER ]                                                               |
|  - ESP32-CAM / ESP32-S3 Microcontroller                                           |
|  - Lightbox Optical Booth Enclosure (Diffused LED Array)                           |
|  - Capacitive Moisture Sensor + DHT22 Temp/Humidity + Neo-6M GPS                  |
|                                 │                                                 |
|                                 ▼ (Camera Feed & Sensor Signals)                  |
|                                                                                   |
|  [ EDGE AI & PERCEPTION LAYER ]                                                   |
|  - MobileNetV3 / YOLOv8-nano Crop Defect Classification Model                     |
|  - TensorFlow Lite for Microcontrollers (TFLite Micro INT8 Quantized)             |
|  - Local Inference on ESP32-S3 (< 200 ms latency)                                 |
|                                 │                                                 |
|                                 ▼ (Grade Verdict & Sensor Payload)                |
|                                                                                   |
|  [ CONNECTIVITY & TELEMETRY LAYER ]                                               |
|  - MQTT Broker (Eclipse Mosquitto / HiveMQ) over GSM (SIM800L) or Wi-Fi           |
|                                 │                                                 |
|                                 ▼                                                 |
|                                                                                   |
|  [ BACKEND & CLOUD SERVICES ]                                                     |
|  - Python Flask / Node.js Express REST API                                        |
|  - PostgreSQL / Firebase Database (Inspection Logs & Farmer Ledger)               |
|  - Government Agmarknet / APMC Live Rate Scraping & API Integration               |
|                                 │                                                 |
|                                 ▼                                                 |
|                                                                                   |
|  [ FRONTEND & DISCOVERY PORTAL ] (CURRENTLY DEMO PROTOTYPE)                       |
|  - Web Application Dashboard (`index.html`)                                       |
|  - Kisan Portal & Buyer Verification Gateway                                      |
|                                                                                   |
+-----------------------------------------------------------------------------------+
```

### Detailed Breakdown of Pending Modules:

#### 1. Hardware & Embedded Systems (Hardware Team)
- [ ] **Physical Lightbox Fabrication**: Design and 3D print/fabricate an enclosed acrylic optical chamber with uniform LED ring lights to eliminate ambient shadow variations during crop scanning.
- [ ] **ESP32-CAM / ESP32-S3 Firmware**: Write C++/Arduino firmware for camera initialization, frame buffer capture, and sensor reading over ADC and I2C/OneWire protocols.
- [ ] **Sensors Integration**: Interfacing physical Capacitive Moisture Sensors (ADC calibration for grain/vegetable water content), DHT22 (Temp & Humidity), and Neo-6M GPS (NMEA sentence parser over UART).
- [ ] **Power Circuit**: Battery management circuit (18650 Li-ion cells + TP4056 charger + Step-up Boost Converter + Solar Panel option for remote farm fields).

#### 2. Edge AI & Computer Vision (Edge AI Team)
- [ ] **Dataset Collection & Labeling**: Collect 5,000+ high-res images of target crops (Tomatoes, Apples, Mangoes, Onions) categorized by defect type (skin rot, pest damage, discoloration, size anomaly).
- [ ] **Model Architecture & Training**: Train lightweight Convolutional Neural Networks (MobileNetV3 / YOLOv8-nano) in PyTorch / TensorFlow.
- [ ] **Model Compression & Quantization**: Quantize model weights from FP32 to INT8 using TensorFlow Lite Converter to reduce memory footprint under 2MB.
- [ ] **TFLite Micro Deployment**: Deploy compiled C++ array model onto ESP32-S3 vector instruction extension (ESP-NN) to achieve sub-200ms local inference time without internet connectivity.

#### 3. Backend, Cloud & Connectivity (Software Team)
- [ ] **MQTT Gateway & Protocol**: Setup Mosquitto MQTT broker on AWS/GCP to receive lightweight telemetry JSON payloads from GSM SIM800L modules installed on cold-chain trucks and farm booths.
- [ ] **REST API Server**: Build Flask / Node.js backend endpoints for user authentication, batch record creation, QR verification lookup, and transport booking state machines.
- [ ] **Database Schema**: Implement PostgreSQL tables for:
  - `farmers` (Kisan ID, Mobile, FPO Cluster ID, Bank/UPI details)
  - `inspections` (Batch ID, Crop Type, Defect %, Moisture %, Grade Verdict, QR Hash, Image URL)
  - `mandi_rates` (Mandi ID, Crop Name, Grade A/B/C Rates, Updated Timestamp)
  - `transit_logs` (Vehicle ID, Lat/Lng, Internal Temp, Humidity, Timestamp)
- [ ] **Real Mandi Live API Integration**: Connect to Government Agmarknet APIs / APMC price feeds for live real-time rate sync across Maharashtra & national mandis.

---

## 4. 👥 Team Role Breakdown Matrix

| Team Role | Hackathon Responsibilities & Scope | Delivered in Prototype | Future Production Scope |
| :--- | :--- | :--- | :--- |
| **Hardware & Embedded Engineer** | Sensor selection, circuit schematics, booth fabrication, ESP32 microcontrollers. | Sensor UI gauges, vehicle tracker stats, hardware latency telemetry badges. | Physical booth build, PCB design, sensor ADC calibration, battery management. |
| **Edge AI & Vision Engineer** | Dataset building, model training, TFLite quantization, edge deployment. | Bounding box overlay, defect segmentation UI, multi-crop defect metric calculations. | Model training on 5,000+ crop images, INT8 quantization, TFLite Micro deployment on ESP32-S3. |
| **Software & Web Engineer** | Price discovery portal, QR certificate generation, UI dashboard, API integration. | Fully functional single-page Web Application (`index.html`) with interactive features, Chart.js telemetry, and presentation controls. | Flask/Node backend, PostgreSQL database, MQTT telemetry broker, live Agmarknet API integration. |

---

## 5. 💡 Summary for Hackathon Presentation

> *"In this internal hackathon prototype, we have built a **fully interactive, production-ready frontend experience (`index.html`)** that brings the entire **Farm-to-Fortune (Agri-Edge)** vision to life for judges. It showcases how a farmer logs in, scans a crop sample with simulated optical AI defect segmentation, receives a tamper-proof digital QR certificate, compares live APMC Mandi prices to gain **+28% higher profit margins**, and tracks cold-chain transport telemetry in real time. The next phase will connect this frontend interface to our ESP32-CAM optical hardware booth, quantized TinyML edge models, and MQTT backend cloud pipelines."*

---
*Report Generated for Farm-to-Fortune (Agri-Edge) Project Team • 2026*
