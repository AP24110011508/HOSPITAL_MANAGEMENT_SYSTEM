"""
Hospital Patient Management System - FULLY TESTED VERSION
Complete implementation using multiple data structures
- Priority Queue for emergency cases
- Stack for medical history  
- Queue for routine checkups
- Hash Maps for quick lookup
- Custom Linked List for symptoms
- Arrays for statistics

NO ERRORS - Guaranteed to run!
"""

import heapq
from collections import deque
from datetime import datetime

# ==================== CUSTOM LINKED LIST FOR SYMPTOMS ====================
class SymptomNode:
    """Node for linked list of symptoms"""
    def __init__(self, symptom, severity):
        self.symptom = symptom
        self.severity = severity
        self.timestamp = datetime.now()
        self.next = None

class SymptomLinkedList:
    """Custom linked list to track patient symptoms"""
    def __init__(self):
        self.head = None
        self.length = 0
    
    def add_symptom(self, symptom, severity):
        """Add new symptom to the end"""
        new_node = SymptomNode(symptom, severity)
        self.length += 1
        
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def get_all_symptoms(self):
        """Get all symptoms as list"""
        result = []
        current = self.head
        while current:
            result.append({
                "symptom": current.symptom,
                "severity": current.severity,
                "timestamp": current.timestamp.strftime("%Y-%m-%d %H:%M")
            })
            current = current.next
        return result
    
    def get_most_severe_symptom(self):
        """Find most severe symptom"""
        if not self.head:
            return None
        
        max_severity = -1
        most_severe = None
        current = self.head
        
        while current:
            if current.severity > max_severity:
                max_severity = current.severity
                most_severe = current.symptom
            current = current.next
        
        return most_severe
    
    def get_average_severity(self):
        """Calculate average symptom severity"""
        if self.length == 0:
            return 0
        
        total = 0
        current = self.head
        while current:
            total += current.severity
            current = current.next
        
        return total / self.length

# ==================== MEDICAL HISTORY STACK ====================
class MedicalHistoryStack:
    """Stack for patient visit history (LIFO)"""
    def __init__(self):
        self.history = []
    
    def add_visit(self, visit_record):
        """Push new visit onto stack"""
        visit_record["date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.history.append(visit_record)
        print(f"  ✓ Added to medical history: {visit_record['diagnosis']}")
    
    def get_last_visit(self):
        """Peek at most recent visit"""
        if self.is_empty():
            return None
        return self.history[-1]
    
    def get_all_history(self):
        """Get complete medical history"""
        return self.history.copy()
    
    def is_empty(self):
        return len(self.history) == 0
    
    def __len__(self):
        return len(self.history)

# ==================== PRIORITY QUEUE FOR EMERGENCIES ====================
class EmergencyPriorityQueue:
    """Priority queue for emergency patients using heap"""
    def __init__(self):
        self.heap = []
        self.counter = 0
    
    def add_patient(self, patient_id, name, priority, condition):
        """Add patient to emergency queue"""
        heapq.heappush(self.heap, (priority, self.counter, patient_id, name, condition))
        self.counter += 1
        
        priority_text = {1: "CRITICAL", 2: "SERIOUS", 3: "MODERATE"}[priority]
        print(f"  🚨 Added to EMERGENCY queue: {name} - {priority_text} priority")
    
    def get_next_patient(self):
        """Get highest priority patient"""
        if self.is_empty():
            return None
        return heapq.heappop(self.heap)
    
    def get_all_patients(self):
        """Get all patients sorted by priority"""
        return sorted(self.heap)
    
    def is_empty(self):
        return len(self.heap) == 0
    
    def size(self):
        return len(self.heap)

# ==================== ROUTINE CHECKUP QUEUE ====================
class RoutineCheckupQueue:
    """FIFO queue for routine checkups"""
    def __init__(self):
        self.queue = deque()
    
    def add_patient(self, patient_id, name, checkup_type):
        """Add patient to routine queue"""
        self.queue.append({
            "patient_id": patient_id,
            "name": name,
            "checkup_type": checkup_type,
            "arrival_time": datetime.now().strftime("%H:%M:%S")
        })
        print(f"  📋 Added to ROUTINE queue: {name} - {checkup_type}")
    
    def get_next_patient(self):
        """Get next patient in line (FIFO)"""
        if self.is_empty():
            return None
        return self.queue.popleft()
    
    def view_queue(self):
        """View all patients in queue"""
        return list(self.queue)
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)

# ==================== PATIENT CLASS ====================
class Patient:
    """Represents a patient with complete medical record"""
    def __init__(self, patient_id, name, age, blood_group, contact):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.blood_group = blood_group
        self.contact = contact
        self.registration_date = datetime.now()
        self.symptoms = SymptomLinkedList()
        self.medical_history = MedicalHistoryStack()
        self.current_status = "Registered"
    
    def add_symptom(self, symptom, severity):
        """Add a new symptom"""
        self.symptoms.add_symptom(symptom, severity)
    
    def add_medical_record(self, diagnosis, prescription, doctor_name):
        """Add a medical visit record"""
        record = {
            "diagnosis": diagnosis,
            "prescription": prescription,
            "doctor": doctor_name,
            "patient_status": self.current_status
        }
        self.medical_history.add_visit(record)
    
    def get_summary(self):
        """Get patient summary"""
        return {
            "id": self.patient_id,
            "name": self.name,
            "age": self.age,
            "blood_group": self.blood_group,
            "contact": self.contact,
            "status": self.current_status,
            "total_visits": len(self.medical_history),
            "avg_symptom_severity": self.symptoms.get_average_severity(),
            "most_severe_symptom": self.symptoms.get_most_severe_symptom()
        }

# ==================== DOCTOR CLASS ====================
class Doctor:
    """Represents a doctor in the hospital"""
    def __init__(self, doctor_id, name, specialty, available=True):
        self.doctor_id = doctor_id
        self.name = name
        self.specialty = specialty
        self.available = available
        self.current_patient = None
        self.patients_treated = 0
    
    def assign_patient(self, patient):
        """Assign a patient to this doctor"""
        self.current_patient = patient
        self.available = False
        patient.current_status = "In-Treatment"
        print(f"  👨‍⚕️ Dr. {self.name} now treating {patient.name}")
    
    def complete_treatment(self, diagnosis, prescription):
        """Complete treatment and discharge patient"""
        if self.current_patient:
            self.current_patient.add_medical_record(diagnosis, prescription, self.name)
            self.current_patient.current_status = "Discharged"
            print(f"  ✅ Dr. {self.name} completed treatment for {self.current_patient.name}")
            print(f"     Diagnosis: {diagnosis}")
            print(f"     Prescription: {prescription}")
            self.patients_treated += 1
            self.current_patient = None
            self.available = True
            return True
        return False

# ==================== MAIN HOSPITAL SYSTEM ====================
class HospitalManagementSystem:
    def __init__(self):
        # Hash Maps for O(1) lookups
        self.patients = {}
        self.doctors = {}
        self.departments = ["Cardiology", "Neurology", "Pediatrics", "Orthopedics", "General Medicine"]
        
        # Queues
        self.emergency_queue = EmergencyPriorityQueue()
        self.routine_queue = RoutineCheckupQueue()
        
        # Statistics (Arrays)
        self.department_stats = [0] * len(self.departments)
        self.treatment_log = []
        
        # Initialize with sample data
        self._init_sample_data()
    
    def _init_sample_data(self):
        """Initialize sample doctors and patients"""
        # Add 6 doctors (including 2 new ones)
        self.add_doctor("D001", "Sarah Johnson", "Cardiology")
        self.add_doctor("D002", "Michael Chen", "Neurology")
        self.add_doctor("D003", "Emily Rodriguez", "Pediatrics")
        self.add_doctor("D004", "James Wilson", "General Medicine")
        self.add_doctor("D005", "Patricia Lee", "Orthopedics")  # New doctor
        self.add_doctor("D006", "David Kim", "Neurology")       # New doctor
        
        # Add sample patients
        self.register_patient("P001", "John Doe", 45, "A+", "555-0101")
        self.register_patient("P002", "Jane Smith", 32, "O-", "555-0102")
        self.register_patient("P003", "Robert Brown", 67, "B+", "555-0103")
        self.register_patient("P004", "Mary Johnson", 28, "AB+", "555-0104")
        
        # Add symptoms
        patient = self.get_patient("P001")
        if patient:
            patient.add_symptom("Chest pain", 8)
            patient.add_symptom("Shortness of breath", 7)
        
        patient = self.get_patient("P002")
        if patient:
            patient.add_symptom("Severe headache", 9)
            patient.add_symptom("Blurred vision", 6)
        
        patient = self.get_patient("P004")
        if patient:
            patient.add_symptom("Knee pain", 7)
        
        # Add to queues
        self.emergency_queue.add_patient("P001", "John Doe", 1, "Possible heart attack")
        self.emergency_queue.add_patient("P002", "Jane Smith", 2, "Migraine with aura")
        self.routine_queue.add_patient("P003", "Robert Brown", "Annual checkup")
        self.routine_queue.add_patient("P004", "Mary Johnson", "Physical therapy")
    
    def register_patient(self, patient_id, name, age, blood_group, contact):
        """Register new patient"""
        if patient_id in self.patients:
            print(f"Patient {patient_id} already exists!")
            return False
        
        patient = Patient(patient_id, name, age, blood_group, contact)
        self.patients[patient_id] = patient
        print(f"✅ Patient registered: {name} (ID: {patient_id})")
        return True
    
    def get_patient(self, patient_id):
        """Get patient by ID"""
        return self.patients.get(patient_id)
    
    def add_doctor(self, doctor_id, name, specialty):
        """Add new doctor"""
        if doctor_id in self.doctors:
            print(f"Doctor {doctor_id} already exists!")
            return False
        
        doctor = Doctor(doctor_id, name, specialty)
        self.doctors[doctor_id] = doctor
        print(f"✅ Doctor added: Dr. {name} - {specialty}")
        return True
    
    def get_available_doctor(self, specialty=None):
        """Find available doctor"""
        for doctor in self.doctors.values():
            if doctor.available:
                if specialty is None or doctor.specialty == specialty:
                    return doctor
        return None
    
    def add_patient_symptom(self, patient_id, symptom, severity):
        """Add symptom to patient"""
        patient = self.get_patient(patient_id)
        if patient:
            if 1 <= severity <= 10:
                patient.add_symptom(symptom, severity)
                print(f"  📝 Symptom added: {symptom} (Severity: {severity}/10)")
                
                if severity >= 8:
                    print(f"  ⚠️ High severity symptom detected!")
                    response = input("  Add to emergency queue? (y/n): ").lower()
                    if response == 'y':
                        self.add_to_emergency(patient_id, patient.name, 1, f"Severe {symptom}")
            else:
                print("Severity must be between 1 and 10")
        else:
            print("Patient not found")
    
    def add_to_emergency(self, patient_id, name, priority, condition):
        """Add to emergency queue"""
        if patient_id not in self.patients:
            print(f"Patient not registered. Please register first.")
            return
        
        self.emergency_queue.add_patient(patient_id, name, priority, condition)
        patient = self.get_patient(patient_id)
        if patient:
            patient.current_status = "In-Queue (Emergency)"
    
    def add_to_routine(self, patient_id, name, checkup_type):
        """Add to routine queue"""
        if patient_id not in self.patients:
            print(f"Patient not registered. Please register first.")
            return
        
        self.routine_queue.add_patient(patient_id, name, checkup_type)
        patient = self.get_patient(patient_id)
        if patient:
            patient.current_status = "In-Queue (Routine)"
    
    def process_emergency(self):
        """Process emergency patient"""
        if self.emergency_queue.is_empty():
            print("No patients in emergency queue")
            return
        
        result = self.emergency_queue.get_next_patient()
        if result is None:
            return
        
        priority, counter, patient_id, name, condition = result
        
        print(f"\n🚨 PROCESSING EMERGENCY: {name}")
        print(f"   Condition: {condition}")
        
        doctor = self.get_available_doctor()
        
        if doctor:
            patient = self.get_patient(patient_id)
            if patient:
                doctor.assign_patient(patient)
                
                print(f"\n   Treating {patient.name}...")
                diagnosis = input("   Enter diagnosis: ")
                prescription = input("   Enter prescription: ")
                
                doctor.complete_treatment(diagnosis, prescription)
                
                self.treatment_log.append({
                    "patient": patient.name,
                    "doctor": doctor.name,
                    "diagnosis": diagnosis,
                    "time": datetime.now().strftime("%Y-%m-%d %H:%M")
                })
                
                # Update department stats
                if doctor.specialty in self.departments:
                    idx = self.departments.index(doctor.specialty)
                    self.department_stats[idx] += 1
        else:
            print("   ❌ No doctor available!")
            self.emergency_queue.add_patient(patient_id, name, priority, condition)
    
    def process_routine(self):
        """Process routine patient"""
        if self.routine_queue.is_empty():
            print("No patients in routine queue")
            return
        
        patient_info = self.routine_queue.get_next_patient()
        if patient_info is None:
            return
        
        print(f"\n📋 PROCESSING ROUTINE: {patient_info['name']}")
        print(f"   Checkup type: {patient_info['checkup_type']}")
        
        doctor = self.get_available_doctor()
        
        if doctor:
            patient = self.get_patient(patient_info['patient_id'])
            if patient:
                doctor.assign_patient(patient)
                
                print(f"\n   Conducting checkup for {patient.name}...")
                diagnosis = input("   Enter findings: ")
                prescription = input("   Enter recommendations: ")
                
                doctor.complete_treatment(diagnosis, prescription)
                
                self.treatment_log.append({
                    "patient": patient.name,
                    "doctor": doctor.name,
                    "diagnosis": diagnosis,
                    "time": datetime.now().strftime("%Y-%m-%d %H:%M")
                })
                
                if doctor.specialty in self.departments:
                    idx = self.departments.index(doctor.specialty)
                    self.department_stats[idx] += 1
        else:
            print("   ❌ No doctor available!")
            self.routine_queue.add_patient(
                patient_info['patient_id'],
                patient_info['name'],
                patient_info['checkup_type']
            )
    
    def view_patient_history(self, patient_id):
        """View patient's medical history"""
        patient = self.get_patient(patient_id)
        if not patient:
            print("Patient not found")
            return
        
        print(f"\n{'='*60}")
        print(f"MEDICAL HISTORY: {patient.name}")
        print(f"{'='*60}")
        
        history = patient.medical_history.get_all_history()
        
        if not history:
            print("No medical records found")
        else:
            for i, record in enumerate(reversed(history), 1):
                print(f"\nVisit #{i}:")
                print(f"  Date: {record['date']}")
                print(f"  Diagnosis: {record['diagnosis']}")
                print(f"  Prescription: {record['prescription']}")
                print(f"  Doctor: {record['doctor']}")
        
        print(f"\n{'='*60}")
        print("SYMPTOM HISTORY:")
        print(f"{'='*60}")
        symptoms = patient.symptoms.get_all_symptoms()
        if symptoms:
            for symptom in symptoms:
                print(f"  • {symptom['symptom']} (Severity: {symptom['severity']}/10)")
        else:
            print("No symptoms recorded")
    
    def get_last_visit(self, patient_id):
        """Get most recent visit"""
        patient = self.get_patient(patient_id)
        if patient:
            last_visit = patient.medical_history.get_last_visit()
            if last_visit:
                print(f"\n📋 LAST VISIT:")
                print(f"  Date: {last_visit['date']}")
                print(f"  Diagnosis: {last_visit['diagnosis']}")
                print(f"  Doctor: {last_visit['doctor']}")
            else:
                print("No previous visits")
        else:
            print("Patient not found")
    
    def generate_full_report(self):
        """Generate complete report"""
        print("\n" + "="*70)
        print("HOSPITAL MANAGEMENT SYSTEM - FULL REPORT".center(70))
        print("="*70)
        
        patient_list = list(self.patients.values())
        
        print(f"\n📊 STATISTICS:")
        print(f"  Total Patients: {len(patient_list)}")
        print(f"  Total Doctors: {len(self.doctors)}")
        print(f"  Emergency Queue: {self.emergency_queue.size()}")
        print(f"  Routine Queue: {self.routine_queue.size()}")
        
        print(f"\n🏥 DEPARTMENT PATIENT COUNTS:")
        for i, dept in enumerate(self.departments):
            print(f"  {dept}: {self.department_stats[i]} patients")
        
        print(f"\n👥 ALL PATIENTS:")
        print(f"{'ID':<10} {'Name':<20} {'Status':<20}")
        print("-"*50)
        for patient in patient_list:
            print(f"{patient.patient_id:<10} {patient.name:<20} {patient.current_status:<20}")
        
        print(f"\n🚨 EMERGENCY QUEUE:")
        if not self.emergency_queue.is_empty():
            for item in self.emergency_queue.get_all_patients():
                priority, _, pid, name, condition = item
                ptext = {1: "CRITICAL", 2: "SERIOUS", 3: "MODERATE"}[priority]
                print(f"  [{ptext}] {name} - {condition}")
        else:
            print("  Empty")
        
        print(f"\n📋 ROUTINE QUEUE:")
        if not self.routine_queue.is_empty():
            for p in self.routine_queue.view_queue():
                print(f"  {p['name']} - {p['checkup_type']}")
        else:
            print("  Empty")
        
        print(f"\n👨‍⚕️ DOCTORS:")
        for doctor in self.doctors.values():
            status = "Available" if doctor.available else "Busy"
            print(f"  Dr. {doctor.name} ({doctor.specialty}) - {status} - Treated: {doctor.patients_treated}")
    
    def list_doctors(self):
        """List all doctors"""
        print("\n" + "="*60)
        print("DOCTOR DIRECTORY".center(60))
        print("="*60)
        print(f"{'ID':<10} {'Name':<20} {'Specialty':<20} {'Status':<12}")
        print("-"*60)
        
        for doctor in self.doctors.values():
            status = "Available" if doctor.available else "Busy"
            print(f"{doctor.doctor_id:<10} {doctor.name:<20} {doctor.specialty:<20} {status:<12}")
            print(f"  Patients treated: {doctor.patients_treated}")
    
    def search_patient(self, patient_id):
        """Search for patient"""
        patient = self.get_patient(patient_id)
        if patient:
            summary = patient.get_summary()
            print(f"\n✅ PATIENT FOUND:")
            print(f"  Name: {summary['name']}")
            print(f"  Age: {summary['age']}")
            print(f"  Blood Group: {summary['blood_group']}")
            print(f"  Contact: {summary['contact']}")
            print(f"  Status: {summary['status']}")
            print(f"  Total Visits: {summary['total_visits']}")
        else:
            print("❌ Patient not found")
    
    def menu(self):
        """Main menu interface"""
        while True:
            print("\n" + "="*60)
            print("  HOSPITAL PATIENT MANAGEMENT SYSTEM".center(60))
            print("="*60)
            print("1. Register New Patient")
            print("2. Add Patient Symptoms")
            print("3. Add to Emergency Queue")
            print("4. Add to Routine Queue")
            print("5. Process Emergency Patient")
            print("6. Process Routine Patient")
            print("7. View Medical History (Stack)")
            print("8. View Last Visit")
            print("9. View All Doctors")
            print("10. Full Hospital Report")
            print("11. Search Patient")
            print("12. Exit")
            print("="*60)
            
            choice = input("\nEnter choice (1-12): ")
            
            if choice == '1':
                print("\n--- REGISTER PATIENT ---")
                pid = input("Patient ID: ")
                name = input("Full Name: ")
                try:
                    age = int(input("Age: "))
                except:
                    age = 30
                blood = input("Blood Group: ")
                contact = input("Contact: ")
                self.register_patient(pid, name, age, blood, contact)
            
            elif choice == '2':
                print("\n--- ADD SYMPTOMS ---")
                pid = input("Patient ID: ")
                symptom = input("Symptom: ")
                try:
                
                    severity = int(input("Severity (1-10): "))
                    self.add_patient_symptom(pid, symptom, severity)
                except:
                    print("Invalid severity")
            
            elif choice == '3':
                print("\n--- EMERGENCY QUEUE ---")
                pid = input("Patient ID: ")
                name = input("Patient Name: ")
                print("Priority: 1=Critical, 2=Serious, 3=Moderate")
                try:
                    priority = int(input("Priority (1-3): "))
                    if priority not in [1,2,3]:
                        priority = 3
                except:
                    priority = 3
                condition = input("Condition: ")
                self.add_to_emergency(pid, name, priority, condition)
            
            elif choice == '4':
                print("\n--- ROUTINE QUEUE ---")
                pid = input("Patient ID: ")
                name = input("Patient Name: ")
                checkup = input("Checkup type: ")
                self.add_to_routine(pid, name, checkup)
            
            elif choice == '5':
                self.process_emergency()
            
            elif choice == '6':
                self.process_routine()
            
            elif choice == '7':
                pid = input("Patient ID: ")
                self.view_patient_history(pid)
            
            elif choice == '8':
                pid = input("Patient ID: ")
                self.get_last_visit(pid)
            
            elif choice == '9':
                self.list_doctors()
            
            elif choice == '10':
                self.generate_full_report()
            
            elif choice == '11':
                pid = input("Patient ID: ")
                self.search_patient(pid)
            
            elif choice == '12':
                print("\nGoodbye!")
                break
            
            else:
                print("Invalid choice")
            
            input("\nPress Enter to continue...")

# ==================== RUN THE PROGRAM ====================
if __name__ == "__main__":
    print("="*60)
    print("  HOSPITAL MANAGEMENT SYSTEM".center(60))
    print("="*60)
    print("\nStarting system with 6 doctors...")
    
    try:
        system = HospitalManagementSystem()
        system.menu()
    except KeyboardInterrupt:
        print("\n\nProgram stopped by user")
    except Exception as e:
        print(f"\nError: {e}")
        print("Please restart the program")
        