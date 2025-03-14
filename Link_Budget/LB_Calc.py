import math
import tkinter as tk
from tkinter import messagebox

def calculate_link_margin(distance_au, power_w, tx_gain_dbi, rx_gain_dbi, bitrate, system_temp_k):
    # Constants
    c = 3e8  # Speed of light (m/s)
    freq_hz = 8.4e9  # X-band frequency (Hz)
    k = -228.6  # Boltzmann's constant in dBW/Hz/K
    bandwidth = bitrate  # Assuming noise bandwidth ~ bit rate
    
    # Convert distance AU to meters (1 AU = 1.496e11 m)
    distance_m = distance_au * 1.496e11
    
    # Transmitter power in dBW
    power_dbw = 10 * math.log10(power_w)
    
    # Free Space Path Loss (FSPL)
    fspl_db = 20 * math.log10((4 * math.pi * distance_m * freq_hz) / c)
    
    # System Noise Power (N)
    noise_power_dbw = k + 10 * math.log10(system_temp_k) + 10 * math.log10(bandwidth)
    
    # Carrier-to-Noise Ratio (C/N0)
    cn0_dbhz = power_dbw + tx_gain_dbi + rx_gain_dbi - fspl_db - noise_power_dbw
    
    # Energy per bit to noise power spectral density (Eb/N0)
    eb_n0_db = cn0_dbhz - 10 * math.log10(bitrate)
    
    # Required Eb/N0 for reliable BPSK communication (~3 dB)
    required_eb_n0_db = 3
    
    # Link Margin
    link_margin_db = eb_n0_db - required_eb_n0_db
    
    return {
        "FSPL (dB)": round(fspl_db, 2),
        "C/N0 (dB-Hz)": round(cn0_dbhz, 2),
        "Eb/N0 (dB)": round(eb_n0_db, 2),
        "Link Margin (dB)": round(link_margin_db, 2)
    }

def calculate_and_display():
    try:
        distance_au = float(entry_distance.get())
        tx_power_w = float(entry_power.get())
        tx_gain_dbi = float(entry_tx_gain.get())
        rx_gain_dbi = float(entry_rx_gain.get())
        bitrate = float(entry_bitrate.get())
        system_temp_k = float(entry_temp.get())
        
        result = calculate_link_margin(distance_au, tx_power_w, tx_gain_dbi, rx_gain_dbi, bitrate, system_temp_k)
        
        result_text.set(f"FSPL: {result['FSPL (dB)']} dB\n"
                        f"C/N0: {result['C/N0 (dB-Hz)']} dB-Hz\n"
                        f"Eb/N0: {result['Eb/N0 (dB)']} dB\n"
                        f"Link Margin: {result['Link Margin (dB)']} dB")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# Create GUI window
root = tk.Tk()
root.title("Link Budget Calculator")

# Input Fields
tk.Label(root, text="Distance (AU):").grid(row=0, column=0)
entry_distance = tk.Entry(root)
entry_distance.grid(row=0, column=1)

tk.Label(root, text="Tx Power (W):").grid(row=1, column=0)
entry_power = tk.Entry(root)
entry_power.grid(row=1, column=1)

tk.Label(root, text="Tx Antenna Gain (dBi):").grid(row=2, column=0)
entry_tx_gain = tk.Entry(root)
entry_tx_gain.grid(row=2, column=1)

tk.Label(root, text="Rx Antenna Gain (dBi):").grid(row=3, column=0)
entry_rx_gain = tk.Entry(root)
entry_rx_gain.grid(row=3, column=1)

tk.Label(root, text="Bitrate (bps):").grid(row=4, column=0)
entry_bitrate = tk.Entry(root)
entry_bitrate.grid(row=4, column=1)

tk.Label(root, text="System Noise Temp (K):").grid(row=5, column=0)
entry_temp = tk.Entry(root)
entry_temp.grid(row=5, column=1)

# Calculate Button
calculate_button = tk.Button(root, text="Calculate", command=calculate_and_display)
calculate_button.grid(row=6, columnspan=2)

# Output Label
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify=tk.LEFT)
result_label.grid(row=7, columnspan=2)

root.mainloop()
