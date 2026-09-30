# e-Mandi Suvidha - Smart Mandi Procurement & Queue Management System

A production-grade, multi-lingual Single Page Web Application (SPA) designed to solve long waiting times, lack of schedule information, and procurement uncertainty for Indian farmers.

---

## 🌾 Overview

**e-Mandi Suvidha** is a production-grade, multi-lingual Single Page Web Application (SPA) designed to modernize Indian agricultural grain markets (Mandis). It eliminates chaotic queueing, eliminates information asymmetry, provides instant digital MSP receipts, and offers predictive traffic management for Mandi procurement officers.

---

## 🚀 Key Modules & Features

### 1. Top Navigation & System Controls
- **Dynamic Role Switcher**: Toggle seamlessly between `Farmer Portal` and `Procurement Officer / Admin Dashboard`.
- **Multi-Language Support**: Complete real-time translation for **English**, **Hindi (हिंदी)**, and **Tamil (தமிழ்)** across UI labels, SMS prompts, and receipts.
- **Live System Status Indicator**: Real-time Mandi capacity meter, operational status (`Online`), and live system clock.

### 2. Farmer Portal
- **Smart Slot Booking Engine**:
  - Commodity selection: Wheat (게हू), Paddy (धान), Maize (मक्का), Chana (चना) with Govt MSP pricing.
  - Crop Quantity (Quintals), Preferred Date, Time Slot selection.
  - **Dynamic Capacity Meter**: Real-time slot occupancy % feedback with high-demand warning badges.
  - **Instant Token Generator**: Generates unique Token ID (`TKN-2026-9842`), dynamic SVG QR pass, gate assignment, and estimated payout.
- **Live Token Tracker & Pipeline Stage Monitor**:
  - 6-Stage Interactive Stepper:
    1. `Slot Booked` ➔ 2. `Gate Checked-In` ➔ 3. `Quality Inspected` ➔ 4. `Weighbridge Weighed` ➔ 5. `Payment Initiated` ➔ 6. `Disbursed to Bank (DBT)`
  - Queue position counter, estimated waiting time clock, and stage completion badges.
- **Feature Phone Access Simulator (Inclusivity Feature)**:
  - Interactive SMS & USSD simulator (`BOOK WHEAT 50 12OCT`, `STATUS TKN-9842`) allowing non-smartphone farmers to interact with the Mandi system via basic text messages.

### 3. Procurement Officer / Admin Dashboard
- **Live Gate Scanner Desk**:
  - Simulated QR Code camera scanner viewport and manual Token ID lookup for instant gate check-in.
- **Automated Digital Inspection & Grading Module**:
  - Interactive sliders for Moisture Content (%), Foreign Matter (%), and Grain Damage (%).
  - Automated Grade Evaluator (`Grade A`, `Standard`, `Rejected`) calculating MSP deductions and net payout.
- **Mandi Traffic & Queue Management**:
  - Filterable table of all arriving vehicles with quick stage advancement actions.
- **Predictive Analytics & Bottleneck Monitor**:
  - High-resolution SVG Chart: Hourly Vehicle Arrivals vs. Weighbridge Processing Capacity.
  - Peak Bottleneck Hours Notice (11:00 AM - 01:00 PM alert).
  - Daily Procurement Volume Target Progress Bar and MSP Disbursement Totals.

---

## 🛠️ How to Run

1. Open a terminal in the project directory:
   ```powershell
   cd C:\Users\ragha\.gemini\antigravity\scratch\sih-mandi-procurement-spa
   ```

2. Start the local server:
   ```powershell
   python server.py
   ```

3. Open your browser and navigate to:
   ```
   http://localhost:8080
   ```
   Or open `index.html` directly in any web browser!
