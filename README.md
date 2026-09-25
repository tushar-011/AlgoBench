# ⚙️ AlgoBench

> **An Offline System Benchmarking, Monitoring, Stress Testing, and Algorithm Performance Comparison Desktop Application built with Python.**

AlgoBench is a college mini-project designed to demonstrate practical **Data Structures and Algorithms (DAA)** concepts through a real-world system benchmarking application. It combines a modern desktop interface with CPU benchmarking, memory testing, sorting-algorithm comparison, stress testing, live system monitoring, SQLite history, and complete system scoring.

---

## ✨ Highlights

- 🖥️ Live CPU, memory, storage, and battery monitoring
- 📊 Real-time CPU and memory performance graph
- ⚡ CPU benchmarking with Light, Medium, and Heavy workloads
- 🧠 Memory performance benchmarking
- 🔀 Sorting-algorithm performance comparison
- 🔥 Controlled system stress testing
- 🧪 Complete automated system benchmark
- 📈 Overall AlgoBench system score and rating
- 🎯 High-end reference-score comparison
- 🗃️ Local benchmark history using SQLite
- ⚙️ Persistent application settings
- 🌙 Light, Dark, and System themes
- 🖥️ Detailed system and processor information
- ▶️ One-click Windows launcher using a `.bat` file
- 📦 Standalone Windows application support using PyInstaller
- 🔒 Fully offline operation after installation

---

# 📌 Table of Contents

- [About the Project](#-about-the-project)
- [Features](#-features)
- [DAA Concepts Demonstrated](#-daa-concepts-demonstrated)
- [Tech Stack](#%EF%B8%8F-tech-stack)
- [Project Structure](#-project-structure)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Running the Application](#%EF%B8%8F-running-the-application)
- [Using the BAT Launcher](#%EF%B8%8F-using-the-bat-launcher)
- [Building the EXE](#-building-the-exe)
- [Major Application Modules](#-major-application-modules)
- [Benchmark Scoring](#-benchmark-scoring)
- [Local Database](#%EF%B8%8F-local-database)
- [Testing](#-testing)
- [Future Improvements](#-future-improvements)
- [GitHub Setup](#-github-setup)
- [Project Status](#-project-status)
- [Author](#%EF%B8%8F-author)

---

# 📖 About the Project

**AlgoBench** is an offline desktop application developed as a **Data Structures and Algorithms mini-project**.

The application allows users to:

- Monitor live system performance
- View processor and hardware information
- Benchmark CPU performance
- Benchmark memory performance
- Compare multiple sorting algorithms
- Run a controlled stress test
- Execute a complete system benchmark
- Generate an overall AlgoBench score
- Compare the score with a high-end internal reference
- Save benchmark history locally
- Customize the application appearance

The application is designed so that normal users see simple and understandable performance terminology while the actual algorithm implementations remain in the backend.

---

# 🚀 Features

## 🏠 Dashboard

The Dashboard provides a live overview of the computer.

### Live information

- CPU usage
- Memory usage
- Battery percentage
- Charging status
- Storage usage
- CPU activity graph
- Memory activity graph
- System health indicator

The graph refresh rate can be changed from the Settings page.

---

## 🖥️ System Overview

The System Overview page displays detailed hardware and operating-system information.

### Information displayed

- Device name
- Operating system
- System architecture
- Processor name
- Physical CPU cores
- Logical CPU threads
- CPU utilization
- Memory usage
- Storage usage
- Battery information
- System uptime

AlgoBench uses Windows system information together with `psutil` to provide accurate processor and hardware details.

---

## ⚡ CPU Performance Test

The CPU Performance Test measures processor performance using controlled workloads.

### Workload modes

- Light
- Medium
- Heavy

### Results

- CPU score
- Performance rating
- Execution time
- Total work processed
- Processing rate
- Peak CPU usage
- Average CPU usage

The benchmark internally uses **Merge Sort** to generate measurable processor workloads.

---

## 🧠 Memory Performance Test

The Memory Performance Test evaluates processing and memory behavior during controlled workloads.

### Workload modes

- Light
- Medium
- Heavy

### Results

- Memory score
- Performance rating
- Execution time
- Work completed
- Peak memory usage
- Memory increase

Python's `tracemalloc` and `psutil` are used to monitor memory behavior.

---

## 🔀 Performance Comparison

The Performance Comparison module compares multiple sorting algorithms using the same generated dataset.

### Processing methods

| User-facing Name | Algorithm |
|---|---|
| Basic Data Processing | Bubble Sort |
| Sequential Data Processing | Insertion Sort |
| Balanced Data Processing | Merge Sort |
| Fast Partition Processing | Quick Sort |

### Workload modes

- Light
- Medium
- Heavy

The module measures execution time for each algorithm and displays visual comparison bars.

The fastest result shown is the fastest **for that specific benchmark run and workload**, not a universal algorithm ranking.

---

## 🔥 System Stress Test

The System Stress Test applies a controlled workload for a selected amount of time.

### Stress levels

- Light
- Medium
- Heavy

### Available durations

- 10 seconds
- 20 seconds
- 30 seconds

### Live monitoring

- CPU usage
- Memory usage
- Elapsed time
- Test progress
- Processing cycles
- Work processed
- Peak CPU usage
- Peak memory usage
- Stability result

The test can be manually stopped at any time.

Manually stopped tests are not stored as completed benchmark results.

---

## 🧪 Complete System Test

The Complete System Test automatically runs the main benchmark modules in sequence.

### Benchmark sequence

1. CPU Performance Test
2. Memory Performance Test
3. Processing Comparison
4. System Stress Test
5. Final score calculation

### Final results

- Overall system score
- Overall rating
- CPU score
- Memory score
- Best processing method
- System stability
- Reference comparison

This provides a single summary of the system's performance inside AlgoBench.

---

## 🎯 Reference Comparison

AlgoBench compares the final Complete System Test score with an internal high-end reference score.

Example:

```text
Your AlgoBench Score: 6200
High-End Reference: 8500
Relative Performance: 72.9%
```

The comparison is calculated using:

```text
Relative Performance = User Score / Reference Score × 100
```

> The current reference value is an internal AlgoBench reference target. It is not a Cinebench, Geekbench, PassMark, or manufacturer benchmark result.

---

## 🗃️ Test History

Completed benchmark results are stored locally using SQLite.

### History information

- Test type
- Workload / mode
- Score
- Rating / result
- Date and time
- Benchmark details

### Available actions

- Refresh history
- Clear history

No external database server is required.

---

## ⚙️ Settings

The Settings page allows users to customize AlgoBench.

### Available settings

- Dark theme
- Light theme
- System theme
- Dashboard refresh rate
- Clear benchmark history

### Refresh-rate options

- 1 second
- 2 seconds
- 5 seconds

Settings are stored locally and automatically restored when the application starts again.

---

# 🧠 DAA Concepts Demonstrated

AlgoBench demonstrates multiple Data Structures and Algorithms concepts through practical benchmarking.

## Sorting Algorithms

### Bubble Sort

Used as the basic comparison algorithm.

Typical time complexity:

```text
O(n²)
```

---

### Insertion Sort

Used for sequential data-processing comparison.

Typical time complexity:

```text
O(n²)
```

---

### Merge Sort

Used in CPU, memory, and stress workloads.

Typical time complexity:

```text
O(n log n)
```

---

### Quick Sort

Used as a partition-based performance comparison algorithm.

Typical average time complexity:

```text
O(n log n)
```

---

## Algorithm Comparison

AlgoBench runs algorithms against comparable datasets and measures their actual execution time.

This demonstrates:

- Runtime measurement
- Algorithm comparison
- Input-size effects
- Workload scaling
- Practical performance differences

---

## Workload Scaling

Different benchmark modes use different input sizes.

```text
Light < Medium < Heavy
```

This helps demonstrate how algorithms and system resources behave as workload size increases.

---

# 🛠️ Tech Stack

| Layer / Technology | Purpose |
|---|---|
| Python | Core programming language |
| CustomTkinter | Desktop graphical user interface |
| psutil | CPU, memory, disk, battery, and system monitoring |
| Matplotlib | Live CPU and memory graphs |
| SQLite | Local benchmark history and settings |
| threading | Background benchmark execution |
| queue | Thread-safe UI result communication |
| tracemalloc | Python memory allocation tracking |
| time / perf_counter | Benchmark timing |
| pathlib | File and database path handling |
| subprocess | Windows processor information |
| platform | Operating-system and architecture information |
| socket | Device-name information |
| PyInstaller | Building the standalone Windows application |
| Visual Studio Code | Development environment |
| Git | Version control |
| GitHub | Repository hosting |
| Batch File | One-click Windows launcher |

---

# 📁 Project Structure

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

> The exact structure may change slightly as the project evolves.

---

# ✅ Requirements

Before running AlgoBench from source, install the following.

## 1. Python

Recommended:

```text
Python 3.11+
```

The project was developed and tested using **Python 3.14**.

Download Python from:

https://www.python.org/

During installation, enable:

```text
Add Python to PATH
```

Check installation:

```powershell
python --version
```

---

## 2. Visual Studio Code

VS Code is recommended for development.

Download:

https://code.visualstudio.com/

Recommended extension:

```text
Python
```

VS Code is not required every time AlgoBench is launched.

Once configured, the application can be started using:

```text
run_algobench.bat
```

---

## 3. Git

Git is required to clone or manage the repository.

Download:

https://git-scm.com/

Check installation:

```powershell
git --version
```

---

## 4. Browser

A browser is only required for downloading tools or accessing GitHub.

Examples:

- Google Chrome
- Microsoft Edge
- Mozilla Firefox

AlgoBench itself is a desktop application and does **not** run inside a browser.

---

## 5. Database Software

No external database software is required.

AlgoBench uses Python's built-in SQLite support.

You do **not** need:

- MySQL Server
- MySQL Workbench
- PostgreSQL
- XAMPP
- phpMyAdmin

---

# 📥 Installation

## Step 1 — Clone the Repository

```powershell
git clone https://github.com/tushar-011/AlgoBench.git
```

Open the project folder:

```powershell
cd AlgoBench
```

---

## Step 2 — Create a Virtual Environment

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\activate
```

---

## Step 3 — Install Dependencies

```powershell
python -m pip install -r requirements.txt
```

If required, the main dependencies can also be installed manually:

```powershell
python -m pip install customtkinter psutil matplotlib pyinstaller
```

SQLite does not require a separate installation because Python includes the `sqlite3` module.

---

# ▶️ Running the Application

AlgoBench can be started in two ways.

---

## Method 1 — BAT Launcher

Recommended for demonstrations.

Double-click:

```text
run_algobench.bat
```

The launcher automatically:

1. Moves to the AlgoBench project directory
2. Checks for the local virtual environment
3. Starts AlgoBench using the virtual environment
4. Falls back to the system Python installation if required

You do **not** need to open VS Code every time.

---

# ▶️ Using the BAT Launcher

Expected project structure:

```text
AlgoBench/
├── main.py
├── run_algobench.bat
└── .venv/
```

Example launcher:

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

To start the application, simply double-click:

```text
run_algobench.bat
```

---

## Method 2 — Manual Run

Activate the virtual environment:

```powershell
.venv\Scripts\activate
```

Then run:

```powershell
python main.py
```

---

# 📦 Building the EXE

AlgoBench can also be converted into a Windows executable using PyInstaller.

## Folder-based build

```powershell
python -m PyInstaller --noconfirm --clean --windowed --name AlgoBench main.py
```

The application will be created inside:

```text
dist/AlgoBench/
```

---

## Single-file build

```powershell
python -m PyInstaller --noconfirm --clean --onefile --windowed --name AlgoBench main.py
```

The executable will be created as:

```text
dist/AlgoBench.exe
```

> The folder-based build is recommended first because it is easier to test and troubleshoot.

---

# 🧩 Major Application Modules

```text
Dashboard
├── CPU usage
├── Memory usage
├── Battery status
├── Storage usage
├── Live performance graph
└── System health

System Overview
├── Device information
├── Operating system
├── Processor information
├── CPU cores
├── CPU threads
├── Memory
├── Storage
├── Battery
└── Uptime

CPU Test
├── Light workload
├── Medium workload
├── Heavy workload
├── CPU score
├── Processing rate
└── CPU utilization

Memory Test
├── Light workload
├── Medium workload
├── Heavy workload
├── Memory score
├── Peak memory
└── Execution time

Performance Comparison
├── Bubble Sort
├── Insertion Sort
├── Merge Sort
├── Quick Sort
├── Execution-time comparison
└── Fastest result

Stress Test
├── Light intensity
├── Medium intensity
├── Heavy intensity
├── Live CPU monitoring
├── Live memory monitoring
├── Stability analysis
└── Manual stop

Complete System Test
├── CPU benchmark
├── Memory benchmark
├── Processing comparison
├── Stress benchmark
├── Overall score
├── Overall rating
└── Reference comparison

History
├── Previous benchmark results
├── Scores
├── Ratings
├── Date and time
├── Refresh
└── Clear history

Settings
├── Appearance
├── Dashboard refresh rate
├── History management
└── Application information
```

---

# 📊 Benchmark Scoring

AlgoBench uses its own internal scoring system.

## CPU Score

The CPU test uses processing throughput to generate the score.

The displayed score is limited to:

```text
0 - 9999
```

---

## Complete System Score

The Complete System Test combines multiple benchmark results.

| Benchmark | Weight |
|---|---:|
| CPU Performance | 35% |
| Memory Performance | 30% |
| Processing Performance | 20% |
| Stress Stability | 15% |

Calculation:

```text
Overall Score =
CPU Score × 0.35
+ Memory Score × 0.30
+ Performance Score × 0.20
+ Stress Score × 0.15
```

The final score is limited to:

```text
9999
```

---

## Overall Ratings

| Score | Rating |
|---:|---|
| 8000+ | Excellent |
| 6500+ | Very Good |
| 5000+ | Good |
| 3500+ | Average |
| Below 3500 | Basic |

> AlgoBench scores are specific to AlgoBench workloads and should not be directly compared with scores from unrelated benchmark applications.

---

# 🗃️ Local Database

AlgoBench uses SQLite for local application data.

The database stores:

- Benchmark history
- Benchmark details
- Application settings
- Appearance preference
- Dashboard refresh rate

SQLite is embedded directly into Python through the `sqlite3` module.

No database server needs to run in the background.

---

# 📴 Offline Operation

AlgoBench is designed to work completely offline after the required Python dependencies are installed.

Internet access is not required for:

- Dashboard monitoring
- System Overview
- CPU Benchmark
- Memory Benchmark
- Performance Comparison
- Stress Test
- Complete System Test
- History
- Settings

Internet access is only needed for tasks such as:

- Downloading Python
- Installing packages
- Cloning the repository
- Accessing GitHub

---

# 🧪 Testing

Before submitting or demonstrating AlgoBench, test:

- Application startup
- BAT launcher
- Dashboard live monitoring
- CPU graph
- Memory graph
- System Overview
- Processor detection
- Light CPU test
- Medium CPU test
- Heavy CPU test
- Memory benchmark
- Performance comparison
- Bubble Sort
- Insertion Sort
- Merge Sort
- Quick Sort
- Stress test
- Manual stress-test stop
- Complete System Test
- Reference comparison
- History saving
- History refresh
- Clear history
- Light theme
- Dark theme
- System theme
- Dashboard refresh-rate setting
- Application restart
- Settings persistence
- PyInstaller build

---

# 🔮 Future Improvements

Possible future additions include:

- Disk read/write benchmark
- Network benchmark
- GPU benchmark
- Historical performance charts
- Export benchmark results to CSV
- Export benchmark reports to PDF
- Multiple reference systems
- Real measured processor reference database
- Additional algorithms
- Search and filtering in benchmark history
- Benchmark presets
- Hardware classification
- More system sensors
- Application update checker
- Installer / setup package
- Benchmark result sharing

These features are intentionally outside the current mini-project scope.

---

# 🌐 GitHub Setup

Useful Git commands:

```powershell
git status
git add .
git commit -m "Your commit message"
git push
```

For a final project commit:

```powershell
git add .
git commit -m "Finalize AlgoBench mini project"
git push
```

---

# 🏁 Project Status

### ✅ Mini-project feature development complete

AlgoBench currently includes the major features required to demonstrate:

- Data Structures and Algorithms
- Sorting algorithms
- Runtime comparison
- Workload scaling
- System monitoring
- CPU benchmarking
- Memory benchmarking
- Stress testing
- Desktop GUI development
- Multithreading
- Local database storage
- Persistent settings
- Benchmark scoring
- Windows application packaging

The project is now primarily in its **testing, documentation, demonstration, and submission stage**.

---

# 👨‍💻 Development Notes

AlgoBench was created as an academic mini-project with emphasis on **Data Structures and Algorithms** and practical desktop application development.

The application is intended for learning, experimentation, demonstration, and academic submission rather than professional hardware certification.

Benchmark results can vary depending on:

- Background applications
- Power mode
- CPU temperature
- Available memory
- Operating-system activity
- Laptop charging state
- Hardware configuration

For more consistent results, close unnecessary applications before running benchmarks.

---

# ⚙️ AlgoBench

**Benchmarking • Monitoring • Algorithms • Stress Testing • System Analysis**

Built with **Python + CustomTkinter + psutil + Matplotlib + SQLite**

---

# 👨‍💻 Author

### Tushar Thakur

**MCA Data Science**  
**Chandigarh University**

[![GitHub](https://img.shields.io/badge/GitHub-tushar--011-181717?logo=github)](https://github.com/tushar-011)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Tushar%20Thakur-0A66C2?logo=linkedin)](https://www.linkedin.com/in/tushar-thakur-8848a7396)
[![Email](https://img.shields.io/badge/Email-artificial.thakur%40gmail.com-EA4335?logo=gmail)](mailto:artificial.thakur@gmail.com)

---

## 📜 Disclaimer

AlgoBench uses custom workloads and custom scoring formulas created specifically for this project.

The generated scores are intended for educational comparison inside AlgoBench and should not be treated as official hardware certification or as directly equivalent to third-party benchmark scores.

---

<p align="center">
  <b>⚙️ AlgoBench</b><br>
  System Performance Benchmarking Made Simple
</p>
