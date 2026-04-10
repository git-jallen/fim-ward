# Ward

A GUI-based File Integrity Monitoring (FIM) system built with Python and PySide6.  
FIM Sentinel detects unauthorized file changes in real time using cryptographic hashing and provides a clean, modern interface for monitoring and analysis.

## Features

- Real-time file monitoring
- SHA-256 file integrity verification
- Baseline snapshot creation
- Detection of:
  * File modifications
  * New file creation
  * File deletions
- Modern GUI built with PySide6
- Multi-threaded monitoring (non-blocking UI)
- Structured logging (JSONL format)
- Configurable scan settings


## Architecture

This project follows a modular, layered architecture:

### Components:
- **GUI Layer**: User interface (PySide6)
- **Controller Layer**: Application logic and orchestration
- **Core Layer**: File monitoring and change detection
- **Service Layer**: Hashing, logging, baseline, config management
- **Data Layer**: JSON-based persistence and audit logs


## Project Structure
```bash
ward/
│
├── app/
│ ├── gui/
│ ├── controllers/
│ ├── core/
│ ├── services/
│ └── models/
│
├── data/
│ ├── baseline.json
│ ├── config.json
│ └── logs/
│
├── main.py
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/git-jallen/ward.git
cd ward
```

Install dependencies:
```bash
pip install -r requirements.txt
```


## Usage

Run the application:
```bash
python main.py
```

### Steps:
1. Select a directory to monitor
2. Create a baseline (recommended)
3. Start monitoring
4. Modify, create, or delete files to see alerts in real time


## Logging

All events are stored in:
``` bash
data/logs/fim.log
```

Format: JSON Lines (JSONL)

Example:
```json
{"timestamp":"2026-04-10T22:10:01Z","event_type":"MODIFIED","file":"/path/file.txt"}
```


## Configuration

Modify settings in:
```bash
data/config.json
```

Example options:

* Scan interval
* Hash algorithm
* Monitored directories
* Ignore patterns


## Packaging

The application can be packaged into a standalone executable using:
```bash
pyinstaller --onefile --windowed main.py
```


## Skills Demonstrated
* Python application development
* GUI development with PySide6
* Multithreading and event-driven programming
* File system monitoring and security concepts
* Modular software architecture
* Structured logging and data persistence


## Future Improvements
* Threat severity classification (LOW / MED / HIGH)
* Real-time file system event monitoring (watchdog)
* Dashboard analytics and visualizations
* Alert notifications (desktop/email)
* Forensic timeline view
* SIEM integration support


## License

This project is open-source and available under the MIT License.

## Author

**Joshua Allen**
Cybersecurity / Computer Science Student

## Acknowledgments

Inspired by real-world tools such as:

* Tripwire
* OSSEC / Wazuh
* Endpoint Detection & Response (EDR) systems