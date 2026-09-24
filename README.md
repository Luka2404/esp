# USB Sentinel

Defensive coursework project: a local USB device monitor with a dashboard, event log, and a **test mode that uses generated devices only**.

It does **not** read game memory, attach to other processes, talk to Counter-Strike, use DMA hardware, or hide software from security tools.

## What it demonstrates

- Enumerate USB devices from the operating system (`system_profiler` on macOS, Plug and Play on Windows, `lsusb` on Linux).
- Collect standard fields: name, vendor, VID/PID, class, serial (when the OS reports one), location.
- Detect connect and disconnect by polling the live device list.
- Compare devices against a saved **baseline** (allowlist of previously seen hardware).
- Flag unknown or incomplete identities (missing serial, vendor ID not on a small public demo allowlist, simulated fixtures).
- Append arrival, removal, and flag events to `logs/usb-sentinel.jsonl`.
- Dashboard at `http://127.0.0.1:5050`.

## Run (development)

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

Open `http://127.0.0.1:5050`.

- **Save baseline** — mark currently connected *live* devices as trusted.
- **Start test mode** — inject three synthetic devices (HID, serial/CDC, mass storage). The monitor should flag them. This does not require plugging anything in.

## Windows executable

On a Windows PC with Python 3 installed:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
.\scripts\build-windows.ps1
```

The demo binary is `dist\USBSentinel.exe`. It opens a console and serves the same local dashboard. Logs for the packaged app are written under `%USERPROFILE%\USBSentinel\`.

This project is developed on macOS as well; run `python run.py` there for the same dashboard using macOS USB inventory.

## Tests

```bash
python -m pytest
```

## Scope limits

- Standard OS USB inventory only — no kernel drivers, no DMA, no process injection.
- Test fixtures are hardcoded sample records, not traffic from games or anti-cheat software.
- Baseline data stays on disk in this project (or the user profile for the `.exe`).
