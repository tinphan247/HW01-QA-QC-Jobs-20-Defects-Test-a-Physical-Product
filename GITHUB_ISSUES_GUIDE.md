# GitHub Issues Bug Logging Guide (Physical Device Defects)

**Student Name:** Phan Trung Tin (ID: 23120372)  
**Target Repository:** [https://github.com/tinphan247/HW01-QA-QC-Jobs-20-Defects-Test-a-Physical-Product](https://github.com/tinphan247/HW01-QA-QC-Jobs-20-Defects-Test-a-Physical-Product)  
**Issues URL:** [https://github.com/tinphan247/HW01-QA-QC-Jobs-20-Defects-Test-a-Physical-Product/issues](https://github.com/tinphan247/HW01-QA-QC-Jobs-20-Defects-Test-a-Physical-Product/issues)  
**Instructions:** Create the following 5 issues in your GitHub repository's **Issues** tab. Take a screenshot showing your GitHub account avatar/username in the top right corner and the list of these 5 closed/open issues for the submission!

---

### Issue 1
- **Title:** `[BUG-01] [Firmware] Volatile memory loss resets user settings to factory default on USB power-cycle`
- **Labels:** `bug`, `firmware`, `hardware-limitation`, `severity:medium`
- **Body:**
  ```markdown
  ### Description
  The USB LED desk lamp does not retain user-configured state (selected CCT light mode and brightness level) when disconnected from the USB power source.

  ### Environment
  - Device: USB-powered Adjustable LED Desk Lamp (OEM / 2023)
  - Power: 5V / 2.0A USB port
  - Serial: UN-****-2023

  ### Steps to Reproduce
  1. Turn the lamp ON and change CCT mode to Cool White (~6500K).
  2. Dim brightness down to Level 3 (~30%).
  3. Disconnect the USB-A cable from the power source.
  4. Wait 10 seconds, then reconnect the USB cable.
  5. Press the Power button to turn the lamp back ON.

  ### Expected Result
  The microcontroller should recall previous user settings from non-volatile memory (EEPROM / internal Flash emulated NVM) and restore Cool White at 30% brightness.

  ### Actual Result
  The lamp always boots into the factory default state: Warm+White (both LED channels at 100% brightness). All previous adjustments are wiped.

  ### Severity
  Medium (Major annoyance for end users requiring manual reconfiguration upon every session).
  ```

---

### Issue 2
- **Title:** `[BUG-02] [Thermal] Inline controller enclosure overheats (>55°C) during sustained dual-mode 100% brightness`
- **Labels:** `bug`, `thermal`, `safety`, `severity:high`
- **Body:**
  ```markdown
  ### Description
  The plastic housing of the 4-button inline controller reaches an uncomfortably high surface temperature (>55°C) when operating in combined Warm+White mode at maximum brightness for extended periods.

  ### Environment
  - Ambient Room Temp: 27°C
  - Power Supply: 5V / 2.4A Certified USB Charger
  - Continuous runtime: > 45 minutes

  ### Steps to Reproduce
  1. Power ON the lamp in dual-mode (Warm Yellow + Cool White combined).
  2. Increase brightness to Level 10 (100% maximum).
  3. Leave the lamp continuously operating on desk for 45 minutes.
  4. Touch the inline controller module with bare hands and measure with thermocouple/IR thermometer.

  ### Expected Result
  The inline control module should remain lukewarm (< 45°C) per consumer electronics safety standards (IEC 62368-1).

  ### Actual Result
  Controller surface reaches 56.4°C. The ABS plastic feels hot to the touch, and a subtle warm plastic resin smell is detected due to linear power dissipation in the onboard switching transistor / linear regulator without heatsinking.

  ### Severity
  High (Thermal discomfort, acceleration of component degradation, potential enclosure warping).
  ```

---

### Issue 3
- **Title:** `[BUG-03] [Power] Rapid flickering and MCU brownout reset when powered by standard USB 2.0 (500mA) port`
- **Labels:** `bug`, `power-system`, `edge-case`, `severity:high`
- **Body:**
  ```markdown
  ### Description
  When connected to a standard USB 2.0 port rated at 5V / 500mA (2.5W), setting the lamp to 100% brightness in dual-LED mode pulls excessive current, causing a host voltage drop and cyclic MCU brownout reset.

  ### Environment
  - Host: PC Motherboard Rear USB 2.0 Port (5V, 500mA spec)
  - Cable: Integrated 1.5m USB-A cable

  ### Steps to Reproduce
  1. Connect the lamp to a USB 2.0 port on the PC.
  2. Switch light mode to Dual CCT (Warm + White).
  3. Press Brightness (+) repeatedly up to 100%.

  ### Expected Result
  The lamp firmware should throttle brightness gracefully or operate within 500mA power envelope to prevent bus collapse.

  ### Actual Result
  At level 8 (~80% brightness), total current exceeds 500mA. The USB bus voltage sags below 4.3V. The microcontroller triggers a brownout reset, causing the lamp to strobe violently (ON-OFF-ON-OFF) at ~2 Hz until disconnected.

  ### Severity
  High (Hardware instability, potential risk of tripping motherboard USB port overcurrent polyfuses).
  ```

---

### Issue 4
- **Title:** `[BUG-04] [Debounce] Missing state transitions and UI lag during rapid actuation of Mode Switch button`
- **Labels:** `bug`, `firmware`, `ui-interaction`, `severity:medium`
- **Body:**
  ```markdown
  ### Description
  Rapidly pressing the Light Mode button within intervals of less than 150ms results in skipped state transitions and brief button unresponsiveness due to flawed software debounce filtering.

  ### Environment
  - Device: USB-powered Adjustable LED Desk Lamp
  - Input: Tactile micro-switch (Mode key)

  ### Steps to Reproduce
  1. Power ON lamp.
  2. Press the Light Mode button rapidly 10 consecutive times within 1.5 seconds.
  3. Observe the light output mode transitions.

  ### Expected Result
  Each tactile click should reliably register a mode transition (Warm -> Cool -> Mixed -> Warm...), completing 10 transitions cleanly.

  ### Actual Result
  Only 6 to 7 transitions are executed. The LED momentarily freezes on one mode for ~500ms before responding again, indicating blocking delays in the switch ISR/polling loop.

  ### Severity
  Medium (Degraded tactile feedback and frustrating user experience).
  ```

---

### Issue 5
- **Title:** `[BUG-05] [Mechanical] Articulated swing-arm joints exhibit downward creep under extended horizontal reach`
- **Labels:** `bug`, `mechanical`, `structural`, `severity:medium`
- **Body:**
  ```markdown
  ### Description
  When the swing arm is adjusted horizontally forward past an angle of 45°, the friction hinge cannot counteract the cantilever gravitational torque, causing the lamp head to slowly droop over 20 minutes.

  ### Environment
  - Mounting: Securely clamped to 25mm thick desk
  - Orientation: Horizontal extension at 45° angle

  ### Steps to Reproduce
  1. Mount the clamp firmly onto desk edge.
  2. Extend the upper swing arm horizontally forward at 45° angle.
  3. Tighten the hand-tightened thumb screw firmly.
  4. Measure lamp head height from desk surface (initial: 38 cm).
  5. Wait 20 minutes without touching the setup.

  ### Expected Result
  The articulated joints and internal counter-balance springs should keep the lamp head stable at 38 cm.

  ### Actual Result
  The lamp head sank to 31.5 cm (a 6.5 cm downward creep). Inspection reveals smooth nylon friction washers that slip under sustained cantilever moment.

  ### Severity
  Medium (Requires frequent readjustment during long study or working sessions).
  ```
