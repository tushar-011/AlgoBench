# AlgoBench

> A modern offline desktop application for system performance benchmarking, monitoring, stress testing, and algorithm-based performance comparison.

---

## Overview

**AlgoBench** is a Python-based offline desktop application designed to monitor and benchmark the performance of a computer system.

The application provides real-time system information, CPU and memory testing, performance comparison using different data-processing methods, controlled stress testing, complete system benchmarking, history tracking, theme customization, and a reference comparison for the final benchmark score.

AlgoBench is designed to be easy to understand for normal users while still using Data Structures and Algorithms concepts internally.

---

## Features

### Dashboard

The Dashboard provides a live overview of the system.

It displays:

- CPU Usage
- Memory Usage
- Battery Percentage
- Charging Status
- Storage Usage
- Live CPU Graph
- Live Memory Graph
- System Health Status

The dashboard updates automatically according to the refresh rate selected in Settings.

---

### System Overview

The System Overview page displays detailed hardware and system information.

It includes:

- Device Name
- Operating System
- Architecture
- Processor Name
- Physical CPU Cores
- CPU Threads
- Memory Usage
- Storage Usage
- Battery Status
- CPU Activity
- System Uptime

This page gives the user a quick overview of the hardware configuration of the machine running AlgoBench.

---

### CPU Performance Test

The CPU Performance Test measures how quickly the processor handles controlled workloads.

Available workload levels:

- Light
- Medium
- Heavy

The test displays:

- Performance Score
- Performance Rating
- Processing Time
- Work Completed
- Processing Rate
- Peak CPU Usage
- Average CPU Usage

Internally, the CPU benchmark uses **Merge Sort** as part of the processing workload.

---

### Memory Performance Test

The Memory Performance Test evaluates how efficiently the system handles memory-intensive operations.

Available workload levels:

- Light
- Medium
- Heavy

The test displays:

- Memory Score
- Performance Rating
- Processing Time
- Work Completed
- Peak Memory Usage
- Memory Increase

The application also tracks memory allocation during the benchmark.

---

### Performance Comparison

The Performance Comparison page compares multiple processing methods using the same dataset.

The methods currently included are:

- Basic Data Processing — Bubble Sort
- Sequential Data Processing — Insertion Sort
- Balanced Data Processing — Merge Sort
- Fast Partition Processing — Quick Sort

The application measures the execution time of each method and displays visual comparison bars.

The fastest method in the current test is shown as the best-performing method.

This result is based only on the selected workload and should not be treated as a universal ranking of algorithms.

---

### System Stress Test

The System Stress Test applies a controlled workload to the system for a selected duration.

Available stress levels:

- Light
- Medium
- Heavy

Available durations:

- 10 Seconds
- 20 Seconds
- 30 Seconds

Live monitoring includes:

- CPU Usage
- Memory Usage
- Elapsed Time
- Test Progress
- Processing Cycles
- Work Processed
- Peak CPU Usage
- Peak Memory Usage
- System Stability

The test can also be stopped manually.

---

### Complete System Test

The Complete System Test combines multiple benchmark modules into a single automated test.

It runs:

1. CPU Performance Test
2. Memory Performance Test
3. Processing Comparison
4. System Stress Test

The final result includes:

- Overall System Score
- Overall Rating
- CPU Score
- Memory Score
- Best Processing Method
- System Stability
- Reference Comparison

The score is calculated using weighted benchmark results.

Current weighting:

- CPU Performance: 35%
- Memory Performance: 30%
- Processing Performance: 20%
- Stress Stability: 15%

---

### Reference Comparison

The Complete System Test also contains a reference-comparison section.

It compares the user's AlgoBench score with a fixed high-end reference score.

Example:

```text
Your AlgoBench Score: 6200
High-End Reference: 8500
Relative Performance: 72.9%
````

This comparison uses the same AlgoBench score scale.

It does not compare AlgoBench scores directly with Cinebench, Geekbench, PassMark, or other external benchmark scores.

The currently used high-end reference value is an internal reference score.

---

### Test History

AlgoBench automatically stores completed benchmark results locally.

The History page displays:

- Test Type
- Workload
- Score
- Result / Rating
- Date and Time

History is stored using SQLite.

The History page also provides:

- Refresh
- Clear History

---

### Settings

The Settings page allows the user to customize the application.

Available options include:

- Dark Mode
- Light Mode
- System Theme
- Dashboard Refresh Rate
- Clear Test History

Available dashboard refresh rates:

- 1 Second
- 2 Seconds
- 5 Seconds

Settings are saved locally and automatically restored when the application is opened again.

---

## About AlgoBench

AlgoBench is an offline system-performance benchmarking application created using Python.

The application combines:

- Real-time system monitoring
- CPU benchmarking
- Memory benchmarking
- Algorithm comparison
- Stress testing
- Complete system benchmarking
- Persistent benchmark history
- User-configurable settings
- Reference-based performance comparison

The project is designed to demonstrate the practical implementation of Python programming, Data Structures and Algorithms, desktop GUI development, system monitoring, databases, multithreading, and performance measurement.

---

## Algorithms Used

AlgoBench currently uses the following algorithms internally:

- Bubble Sort
- Insertion Sort
- Merge Sort
- Quick Sort

These algorithms are used to generate controlled workloads and compare processing performance.

The user interface uses simple user-friendly descriptions while the algorithm implementation remains in the backend.

---

## Tech Stack

| Technology | Purpose |
|---|---|
| Python                   | Core programming language                        |
| CustomTkinter            | Desktop graphical user interface                 |
| psutil                   | System monitoring and hardware statistics        |
| Matplotlib               | Live system-performance graphs                   |
| SQLite                   | Local test-history and settings database         |
| threading                | Background benchmark execution                   |
| queue                    | Safe communication between worker threads and UI |
| tracemalloc              | Memory monitoring                                |
| time / time.perf_counter | Performance measurement                          |
| pathlib                  | File and database paths                          |
| subprocess               | Windows processor information                    |
| PyInstaller              | Building the standalone Windows application      |
| Git                      | Version control                                  |
| GitHub                   | Project repository and source-code hosting       |

---

## Project Structure

```text
AlgoBench/
│
├── algorithms/
│   ├── __init__.py
│   └── sorting.py
│
├── database/
│   ├── __init__.py
│   └── db.py
│
├── system/
│   ├── __init__.py
│   └── monitor.py
│
├── tests/
│   ├── __init__.py
│   ├── cpu_benchmark.py
│   ├── memory_benchmark.py
│   ├── performance_benchmark.py
│   ├── stress_benchmark.py
│   └── all_in_one_benchmark.py
│
├── ui/
│   ├── __init__.py
│   ├── theme.py
│   ├── components.py
│   ├── sidebar.py
│   ├── dashboard.py
│   ├── system_overview.py
│   ├── cpu_test.py
│   ├── memory_test.py
│   ├── performance_test.py
│   ├── stress_test.py
│   ├── all_in_one.py
│   ├── history.py
│   └── settings.py
│
├── main.py
├── run_algobench.bat
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Requirements

Recommended operating system:

```text
Windows 10 / Windows 11
```

Recommended Python version:

```text
Python 3.11+
```

The project was developed and tested using Python 3.14.

---

## Software Required

To run the project from source, install:

- Python
- Git
- Visual Studio Code

A web browser can be used to download these tools and access GitHub.

A browser is not required to run AlgoBench itself.

MySQL Workbench is not required because AlgoBench uses SQLite.

---

## Installing Python

Download Python from:

[https://www.python.org/](https://www.python.org/)

During installation, enable:

```text
Add Python to PATH
```

Verify installation:

```powershell
python --version
```

---

## Installing Git

Download Git from:

[https://git-scm.com/](https://git-scm.com/)

Verify installation:

```powershell
git --version
```

---

## Installing Visual Studio Code

Download Visual Studio Code from:

[https://code.visualstudio.com/](https://code.visualstudio.com/)

Recommended VS Code extension:

```text
Python
```

VS Code is only required for editing and developing the project.

It is not required when running the packaged application.

---

## Clone the Repository

Open PowerShell or Command Prompt:

```powershell
git clone https://github.com/tushar-011/<YOUR-REPOSITORY-NAME>.git
```

Enter the project folder:

```powershell
cd AlgoBench
```

---

## Create a Virtual Environment

Create the virtual environment:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\activate
```

---

## Install Dependencies

If `requirements.txt` is available:

```powershell
python -m pip install -r requirements.txt
```

Or install the main dependencies manually:

```powershell
python -m pip install customtkinter psutil matplotlib pyinstaller
```

SQLite does not require separate installation because Python includes the `sqlite3` module.

---

## Run AlgoBench Using Python

Run:

```powershell
python main.py
```

---

## Run AlgoBench Using the BAT File

AlgoBench includes:

```text
run_algobench.bat
```

Simply double-click the file.

The BAT file automatically:

1. Opens the project directory
2. Checks for the virtual environment
3. Runs AlgoBench using the virtual environment
4. Falls back to the system Python installation if required

Example BAT file:

```bat
@echo off
cd /d "%~dp0"

if exist ".venv\Scripts\python.exe" (
    ".venv\Scripts\python.exe" main.py
) else (
    python main.py
)

if errorlevel 1 (
    echo.
    echo AlgoBench encountered an error.
    pause
)
```

---

## Build the Windows Application

Activate the virtual environment:

```powershell
.venv\Scripts\activate
```

Build the application:

```powershell
python -m PyInstaller --noconfirm --clean --windowed --name AlgoBench main.py
```

The application will be created inside:

```text
dist/AlgoBench/
```

Run:

```text
AlgoBench.exe
```

---

## Build a Single EXE File

You can also build a single executable:

```powershell
python -m PyInstaller --noconfirm --clean --onefile --windowed --name AlgoBench main.py
```

The final executable will be created inside:

```text
dist/
```

Example:

```text
dist/AlgoBench.exe
```

---

## Database

AlgoBench uses SQLite to store:

- Benchmark History
- Application Settings

The database is created automatically.

No external database server is required.

This means you do not need:

- MySQL
- MySQL Workbench
- PostgreSQL
- XAMPP
- phpMyAdmin

---

## Offline Operation

AlgoBench is designed to work completely offline.

An internet connection is not required for:

- CPU Testing
- Memory Testing
- Performance Comparison
- Stress Testing
- Complete Benchmark
- Dashboard Monitoring
- Test History
- Settings

Internet access is only needed when downloading dependencies or cloning the project.

---

## User Interface

AlgoBench includes a modern desktop interface with:

- Sidebar navigation
- Dashboard cards
- Live graphs
- Status badges
- Light and Dark themes
- Responsive panels
- Benchmark result cards
- Progress bars
- Scrollable Settings and About sections

---

## Benchmark Ratings

Different benchmark modules generate internal scores and ratings.

Possible ratings include:

```text
Excellent
Very Good
Good
Average
Basic
```

The scores are designed specifically for AlgoBench workloads.

They should not be directly compared with scores from unrelated benchmarking applications.

---

## Complete Benchmark Score

The final system score is generated using:

```text
CPU Score            35%
Memory Score         30%
Performance Score    20%
Stress Score         15%
```

The maximum displayed score is:

```text
9999
```

---

## Local Data

AlgoBench stores its information locally.

Data is not automatically uploaded to any online server.

The application does not require a user account.

---

## Current Project Status

```text
[✓] Dashboard
[✓] Live CPU Monitoring
[✓] Live Memory Monitoring
[✓] Battery Monitoring
[✓] Storage Monitoring
[✓] System Overview
[✓] CPU Benchmark
[✓] Memory Benchmark
[✓] Performance Comparison
[✓] Stress Test
[✓] Complete System Benchmark
[✓] Reference Comparison
[✓] Test History
[✓] SQLite Integration
[✓] Settings
[✓] Light / Dark Theme
[✓] Adjustable Dashboard Refresh Rate
[✓] BAT Launcher
[✓] Standalone EXE Support
```

---

## Possible Future Improvements

Possible future additions include:

- More benchmark workloads
- Additional algorithm comparisons
- Disk benchmark
- Network benchmark
- Benchmark result export
- CSV export
- PDF report generation
- Historical performance graphs
- Multiple reference systems
- Real measured CPU reference database
- Automatic hardware classification
- More system sensors
- Benchmark presets
- Additional customization options

---

## Important Benchmark Note

AlgoBench uses its own workloads and scoring formulas.

The generated score should be treated as an AlgoBench-specific performance measurement.

The reference comparison currently uses an internal high-end reference score.

It should not be interpreted as a direct comparison against Cinebench, Geekbench, PassMark, or another independent benchmark platform.

---

## Troubleshooting

### Python command is not recognized

Reinstall Python and make sure:

```text
Add Python to PATH
```

is enabled.

---

### Module not found

Activate the virtual environment:

```powershell
.venv\Scripts\activate
```

Then install dependencies:

```powershell
python -m pip install -r requirements.txt
```

---

### Application does not start from BAT file

Try:

```powershell
python main.py
```

Check the terminal for the error message.

---

### PyInstaller command is not recognized

Use:

```powershell
python -m PyInstaller
```

instead of:

```powershell
pyinstaller
```

---

## Git Workflow

Check changes:

```powershell
git status
```

Stage files:

```powershell
git add .
```

Commit:

```powershell
git commit -m "Update AlgoBench"
```

Push:

```powershell
git push
```

---

## Author

**Name:** Tushar Thakur  
**Course / Program:** MCA Data Science  
**University:** Chandigarh University  
**GitHub:** [github.com/tushar-011](https://github.com/tushar-011)  
**LinkedIn:** [linkedin.com/in/tushar-thakur-8848a7396](https://www.linkedin.com/in/tushar-thakur-8848a7396)  
**Email:** [artificial.thakur@gmail.com](mailto:artificial.thakur@gmail.com)

---

## Project Information

**Project Name:** AlgoBench
**Project Type:** Mini Project
**Category:** System Performance Benchmarking
**Platform:** Windows Desktop
**Language:** Python
**Database:** SQLite
**Interface:** CustomTkinter

---

## License

This project was developed for educational and academic purposes.

You may modify and extend the project for learning, experimentation, and academic use.

---


<p align="center">
  <b>AlgoBench</b><br>
  System Performance Benchmarking Made Simple
</p>
