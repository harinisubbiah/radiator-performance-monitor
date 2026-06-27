import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime

refresh_interval = 30  # in seconds

# Define thresholds for warning status
TEMP_THRESHOLD = 200
RPM_THRESHOLD = 2000

while True:

    # Read the CSV file
    may = pd.read_csv(r"/path/to/sample_data.csv")

    # Convert 'Date&Time' column to datetime if it's not already
    if may['Date&Time'].dtype == 'object':
        may['Date&Time'] = pd.to_datetime(
            may['Date&Time'],
            format='%m/%d/%y %H:%M:%S'
        )

    # Assign columns to variables
    x = may['Date&Time']
    y1 = may['Water Temperature (°C)']
    y2 = may['Oil Temperature (°C)']
    y3 = may['RPM']
    y4 = may['Gear Position']

    # Determine warning status
    warning_status = []

    for i in range(len(y1)):
        if (
            y1[i] > TEMP_THRESHOLD
            or y2[i] > TEMP_THRESHOLD
            or y3[i] > RPM_THRESHOLD
        ):
            warning_status.append("HIGH")
        else:
            warning_status.append("OK")

    interval = 500

    # ================= Figure 1 =================
    plt.figure(1, figsize=(10, 8))

    # Water Temperature
    plt.subplot(2, 1, 1)
    plt.bar(np.arange(len(y1)), y1, color='b', linewidth=1.5)
    plt.ylabel("Temperature (°C)", fontsize=12, fontweight='bold')
    plt.title("Water Temperature vs Time", fontsize=14, fontweight='bold')
    plt.ylim(0, max(y1) + 100)

    plt.xticks(
        np.arange(0, len(x), interval),
        x.dt.strftime('%m/%d/%y %H:%M:%S')[::interval],
        rotation=45,
        fontsize=10
    )

    plt.grid(True)

    for i in range(0, len(y1), interval):
        plt.text(
            i,
            y1[i],
            f"{y1[i]:.1f}",
            ha='center',
            va='bottom',
            fontsize=8
        )

    # Oil Temperature
    plt.subplot(2, 1, 2)
    plt.bar(np.arange(len(y2)), y2, color='r', linewidth=1.5)
    plt.ylabel("Temperature (°C)", fontsize=12, fontweight='bold')
    plt.title("Oil Temperature vs Time", fontsize=14, fontweight='bold')
    plt.ylim(0, max(y2) + 5)

    plt.xticks(
        np.arange(0, len(x), interval),
        x.dt.strftime('%m/%d/%y %H:%M:%S')[::interval],
        rotation=45,
        fontsize=10
    )

    plt.grid(True)

    for i in range(0, len(y2), interval):
        plt.text(
            i,
            y2[i],
            f"{y2[i]:.1f}",
            ha='center',
            va='bottom',
            fontsize=8
        )

    plt.tight_layout()

    # ================= Figure 2 =================
    plt.figure(2, figsize=(10, 8))

    # RPM
    plt.subplot(2, 1, 1)
    plt.bar(np.arange(len(y3)), y3, color='b', linewidth=1.5)
    plt.ylabel("RPM", fontsize=12, fontweight='bold')
    plt.title("RPM vs Time", fontsize=14, fontweight='bold')
    plt.ylim(0, max(y3) + 5)

    plt.xticks(
        np.arange(0, len(x), interval),
        x.dt.strftime('%m/%d/%y %H:%M:%S')[::interval],
        rotation=45,
        fontsize=10
    )

    plt.grid(True)

    for i in range(0, len(y3), interval):
        plt.text(
            i,
            y3[i],
            f"{y3[i]:.1f}",
            ha='center',
            va='bottom',
            fontsize=8
        )

    # Gear Position
    plt.subplot(2, 1, 2)
    plt.bar(np.arange(len(y4)), y4, color='r', linewidth=1.5)
    plt.ylabel("Gear Position", fontsize=12, fontweight='bold')
    plt.title("Gear Position vs Time", fontsize=14, fontweight='bold')
    plt.ylim(0, max(y4) + 5)

    plt.xticks(
        np.arange(0, len(x), interval),
        x.dt.strftime('%m/%d/%y %H:%M:%S')[::interval],
        rotation=45,
        fontsize=10
    )

    plt.grid(True)

    for i in range(0, len(y4), interval):
        plt.text(
            i,
            y4[i],
            f"{y4[i]:.1f}",
            ha='center',
            va='bottom',
            fontsize=8
        )

    plt.tight_layout()

    # ================= Figure 3 =================
    plt.figure(3, figsize=(10, 4))

    plt.bar(
        np.arange(len(warning_status)),
        [1] * len(warning_status),
        color=['r' if status == 'HIGH' else 'g' for status in warning_status],
        linewidth=1.5
    )

    plt.xlabel("Date & Time", fontsize=12, fontweight='bold')
    plt.ylabel("Warning Status", fontsize=12, fontweight='bold')
    plt.title(
        "Warning Status (High = Red, OK = Green)",
        fontsize=14,
        fontweight='bold'
    )

    plt.ylim(0, 1.2)

    plt.xticks(
        np.arange(0, len(x), interval),
        x.dt.strftime('%m/%d/%y %H:%M:%S')[::interval],
        rotation=45,
        fontsize=10
    )

    plt.grid(True)
    plt.tight_layout()

    # Refresh plots every 30 seconds
    plt.pause(refresh_interval)

    # Close all figures before next refresh
    plt.close('all')
