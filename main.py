import time
from datetime import datetime, timedelta
import random

class AstronautHealthMonitor:
    
    def _init_(self, astronaut_name):
        self.astronaut_name = astronaut_name
        self.muscle_health = 100  # Starting value for muscle health (100%)
        self.bone_density = 100   # Starting value for bone density (100%)
        self.sleep_quality = 100  # Sleep quality percentage
        self.vitals = {
            "heart_rate": 70,    # Normal heart rate (bpm)
            "immune_function": 100,  # Immune function (100%)
            "muscle_health": self.muscle_health,
            "bone_density": self.bone_density
        }
        self.medicine_intake = {"Vitamin D": False, "Bisphosphonates": False}
        self.exercise_done_today = False
        self.sleep_tracking = {"hours_slept": 0, "quality": 100}
        self.last_exercise_time = datetime.now() - timedelta(days=1)
        
    def log_vitals(self):
        print(f"Vitals for {self.astronaut_name}:")
        for key, value in self.vitals.items():
            print(f"{key}: {value}")
        print("\n")

    def take_medicine(self, medicine_name):
        self.medicine_intake[medicine_name] = True
        print(f"{self.astronaut_name} has taken {medicine_name}.")
    
    def reset_medicine(self):
        self.medicine_intake = {med: False for med in self.medicine_intake}
    
    def perform_exercise(self):
        if (datetime.now() - self.last_exercise_time).days >= 1:
            print(f"{self.astronaut_name} is performing exercise.")
            self.vitals["muscle_health"] += 5
            self.vitals["bone_density"] += 5
            self.last_exercise_time = datetime.now()
            self.exercise_done_today = True
        else:
            print("Exercise has already been done today.")
        self.log_vitals()
    
    def track_sleep(self, hours_slept):
        self.sleep_tracking["hours_slept"] = hours_slept
        if hours_slept < 7:
            self.sleep_tracking["quality"] -= 20  # Decrease sleep quality if sleep is insufficient
        else:
            self.sleep_tracking["quality"] += 10  # Improve sleep quality with proper rest
        self.sleep_quality = max(0, min(100, self.sleep_tracking["quality"]))
        print(f"{self.astronaut_name}'s sleep quality is now {self.sleep_quality}% after {hours_slept} hours of sleep.")
    
    def sync_with_lighting(self, current_time):
        if 6 <= current_time.hour < 18:
            print("Daytime lighting mode enabled.")
        else:
            print("Nighttime lighting mode enabled for better circadian rhythm management.")
    
    def telemedicine_consultation(self, issue):
        print(f"Connecting {self.astronaut_name} with Earth for telemedicine consultation on {issue}...")
        time.sleep(2)  # Simulate telemedicine delay
        print("Consultation completed. Recommendations have been updated.")
    
    def monitor_vitals(self):
        self.vitals["heart_rate"] = random.randint(60, 80)  # Randomized simulation of heart rate
        self.vitals["immune_function"] = max(0, self.vitals["immune_function"] - random.randint(0, 5))  # Immune function decrease
        
        if self.vitals["immune_function"] < 50:
            print(f"Warning! {self.astronaut_name}'s immune function is below 50%. Consider taking countermeasures.\n")
        self.log_vitals()

# Simulating the app functionality

# Create astronaut health monitor
astronaut = AstronautHealthMonitor(astronaut_name="Commander Shepard")

# Daily routines

# 1. Track exercise
astronaut.perform_exercise()

# 2. Take medication (e.g., Vitamin D)
astronaut.take_medicine("Vitamin D")

# 3. Monitor vitals (with daily random variations)
astronaut.monitor_vitals()

# 4. Adjust sleep environment and track sleep
astronaut.sync_with_lighting(datetime.now())  # Sync lighting based on current time
astronaut.track_sleep(hours_slept=6)  # Simulate 6 hours of sleep

# 5. Telemedicine consultation
astronaut.telemedicine_consultation(issue="Low immune function")

# Reset for the next day
astronaut.reset_medicine()
