# 🏥 Hospital Patient Management System

> A Python-based Terminal Application using Core Data Structures

---

## 📋 Project Overview

The **Hospital Patient Management System** is a terminal-based application developed in Python that simulates real-world hospital operations. It efficiently manages patients, doctors, emergency triage, and medical records using fundamental Data Structures concepts.

This project was developed as part of the **Data Structures and Algorithms** coursework at **SRM University, Andhra Pradesh**.

---

## 👨‍💻 Team Members

| Name | Roll Number |
|------|-------------|
| Dinesh CH | AP24110011504 |
| Charan Koya | AP24110011508 |
| Ranjith Vijay Raavi | AP24110011505 |
| Sai Chaturvedi Nallana | AP24110011463 |
| b.shashank | AP24110011496 |

---

## 🧠 Data Structures Used

| Data Structure | Where It's Applied |
|---|---|
| **Linked List** | Dynamically stores and traverses patient symptoms |
| **Stack (LIFO)** | Maintains patient medical visit history |
| **Queue (FIFO)** | Manages routine checkup patient ordering |
| **Priority Queue (Min-Heap)** | Handles emergency patients by severity level |
| **Hash Map (Dictionary)** | O(1) lookup for patients and doctors |
| **Arrays** | Department-wise patient statistics tracking |

---

## ⚙️ Features

- ✅ Patient registration with unique ID
- 📝 Add and track symptoms with severity rating (1–10)
- 🚨 Emergency queue with priority levels (Critical / Serious / Moderate)
- 📋 Routine checkup queue (FIFO ordering)
- 👨‍⚕️ Doctor assignment and treatment completion
- 🗂️ Full medical history tracking per patient (Stack-based)
- 📊 Hospital-wide report generation
- 🔍 Search patient by ID
- 📈 Department-level statistics

---

## 📸 Screenshots

### 🖥️ Main Menu
<img width="464" height="262" alt="Screenshot 2026-04-30 at 11 41 43 PM" src="https://github.com/user-attachments/assets/5461d9e0-d9ee-4679-a627-e841efaaebed" />

### 👤 Patient Registration
<img width="540" height="160" alt="Screenshot 2026-04-30 at 11 42 28 PM" src="https://github.com/user-attachments/assets/928e6597-eb9f-4c3b-89e2-63b0073ef676" />


### 👨‍⚕️ Doctor Directory
<img width="483" height="308" alt="Screenshot 2026-04-30 at 11 43 25 PM" src="https://github.com/user-attachments/assets/4d1e113a-2247-4951-8c37-931b77d087bc" />

### 🗂️ Medical History (Stack)
<img width="451" height="218" alt="Screenshot 2026-04-30 at 11 43 03 PM" src="https://github.com/user-attachments/assets/9093f11f-497c-4a2e-aaee-2933dcd64cd3" />


### 📊 Full Hospital Report
<img width="567" height="651" alt="Screenshot 2026-04-30 at 11 43 44 PM" src="https://github.com/user-attachments/assets/b238a5df-1624-4b71-aeab-6cdda00437f4" />

---

project report
[Hospital_Management_System_Report (1).docx](https://github.com/user-attachments/files/27257053/Hospital_Management_System_Report.1.docx)




## 🗂️ Project Structure

```
HOSPITAL_MANAGEMENT_SYSTEM/
│
├── hospital_management.py      # Main application file
└── README.md                   # Project documentation
```

---

## ▶️ How to Run

**Requirements:** Python 3.x

```bash
# Clone the repository
git clone https://github.com/AP24110011508/HOSPITAL_MANAGEMENT_SYSTEM.git

# Navigate to the project folder
cd HOSPITAL_MANAGEMENT_SYSTEM

# Run the application
python hospital_management.py
```

---

## 🖥️ System Menu

```
============================================================
      HOSPITAL PATIENT MANAGEMENT SYSTEM
============================================================
1.  Register New Patient
2.  Add Patient Symptoms
3.  Add to Emergency Queue (Priority)
4.  Add to Routine Queue (FIFO)
5.  Process Next Emergency Patient
6.  Process Next Routine Patient
7.  View Patient Medical History (Stack)
8.  View Patient Last Visit
9.  View All Doctors
10. Generate Full Hospital Report
11. Search Patient
12. Exit
============================================================
```

---

## 🔍 Core Implementation Details

### Symptom Tracking — Linked List
Each patient's symptoms are stored in a custom singly linked list. Each node holds the symptom name, severity score, and timestamp. This allows dynamic addition and traversal without a fixed array size.

### Medical History — Stack
Patient visit records are pushed onto a stack after each treatment, providing O(1) access to the most recent visit and maintaining chronological history (LIFO).

### Routine Queue — Deque (FIFO)
Routine checkup patients are enqueued using Python's `collections.deque`, ensuring fair first-come-first-served ordering.

### Emergency Queue — Min-Heap (Priority Queue)
Emergency patients are managed using Python's `heapq` module. Priority `1` (Critical) is treated with highest urgency. A tie-breaking counter ensures stable ordering.

### Patient & Doctor Lookup — Hash Map
Both patients and doctors are stored in Python dictionaries keyed by their IDs, enabling O(1) lookup regardless of system size.

---

## 🎯 Conclusion

This project demonstrates the practical application of multiple data structures in a real-world medical context. It efficiently handles patient flow, doctor assignment, and emergency prioritization — all while maintaining clean, modular Python code.

---

## 📄 License

This project is submitted for academic purposes at SRM University AP.
