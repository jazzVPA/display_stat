import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis, shapiro, t, sem

def calculate_statistics(data):
    stats = {
        "Mean": np.mean(data),
        "Median": np.median(data),
        "Std Dev": np.std(data, ddof=1),
        "Min": np.min(data),
        "Max": np.max(data),
        "Range": np.max(data) - np.min(data),
        "Skewness": skew(data),
        "Kurtosis": kurtosis(data)
    }
    return stats

def calculate_process_capability(data, USL, LSL):
    mean = np.mean(data)
    std_dev = np.std(data, ddof=1)
    cpu = (USL - mean) / (3 * std_dev)
    cpl = (mean - LSL) / (3 * std_dev)
    cp = (USL - LSL) / (6 * std_dev)
    cpk = min(cpu, cpl)
    return {
        "Cp": round(cp, 4),
        "Cpu": round(cpu, 4),
        "Cpl": round(cpl, 4),
        "Cpk": round(cpk, 4)
    }

def calculate_confidence_interval(data, confidence=0.95):
    n = len(data)
    m = np.mean(data)
    s = sem(data)
    interval = t.interval(confidence, n - 1, loc=m, scale=s)
    return interval

def detect_outliers(data):
    Q1 = np.percentile(data, 25)
    Q3 = np.percentile(data, 75)
    IQR = Q3 - Q1
    outliers = data[(data < Q1 - 1.5 * IQR) | (data > Q3 + 1.5 * IQR)]
    return outliers

def print_statistics(label, stats):
    print(f"\n{label} Statistics:")
    for key, value in stats.items():
        print(f"{key}: {value:.4f}")

def print_process_capability(capability, quantity):
    print(f"\nProcess Capability Indices ({quantity}):")
    for key, value in capability.items():
        print(f"{key}: {value}")

def plot_distribution(data, title, xlabel, USL=None, LSL=None, mean=None, annotations=None):
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=30, color='skyblue', edgecolor='black', alpha=0.7, density=True)

    if USL is not None:
        plt.axvline(USL, color='red', linestyle='--', label='USL')
    if LSL is not None:
        plt.axvline(LSL, color='orange', linestyle='--', label='LSL')
    if mean is not None:
        plt.axvline(mean, color='green', linestyle='-', label='Mean')

    if annotations:
        text = "\n".join(annotations)
        plt.text(0.98, 0.98, text, fontsize=9, transform=plt.gca().transAxes,
                 verticalalignment='top', horizontalalignment='right',
                 bbox=dict(facecolor='white', alpha=0.7, edgecolor='gray'))

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel('Density')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    # select the quantity, USL and LSL and run this codes
    # quantities are Luminance_cd/m2 or Chromaticity_x or Chromaticity_y
    quantity = "Luminance_cd/m2"
    USL = 400
    LSL = 200

    df = pd.read_csv("display_Lxy_data.csv")
    data = df[quantity].dropna()
    annotations = []

    # Statistics
    stats = calculate_statistics(data)
    annotations.append("Statistics")
    annotations.append(f"Mean: {stats['Mean']:.4f}")
    annotations.append(f"Median: {stats['Median']:.4f}")
    annotations.append(f"Std Dev: {stats['Std Dev']:.4f}")
    annotations.append(f"Min: {stats['Min']:.4f}")
    annotations.append(f"Max: {stats['Max']:.4f}")
    annotations.append(f"Range: {stats['Range']:.4f}")
    annotations.append(f"Skewness: {stats['Skewness']:.4f}")
    annotations.append(f"Kurtosis: {stats['Kurtosis']:.4f}")

    # Process Capability
    capability = calculate_process_capability(data, USL, LSL)
    annotations.append(f"__________________________")
    annotations.append(f"Process Capability Indices")
    for key, value in capability.items():
        annotations.append(f"{key}: {value:.4f}")

    # Confidence Interval
    annotations.append(f"__________________________")
    ci = calculate_confidence_interval(data)
    annotations.append(f"95% CI: ({ci[0]:.4f}, {ci[1]:.4f})")

    # Normality Test
    stat, p = shapiro(data)
    annotations.append(f"Shapiro-Wilk Test: W = {stat:.4f}, p = {p:.4f}")
    if p > 0.05:
        annotations.append("Data likely normal")
    else:
        annotations.append("Data likely not normal")

    # Outliers
    outliers = detect_outliers(data)
    annotations.append(f"# of Outliers: {len(outliers)}")

    # Plot
    plot_distribution(data, f"{quantity} Distribution with Spec Limits", quantity,
                      USL=USL, LSL=LSL, mean=stats["Mean"], annotations=annotations)

if __name__ == "__main__":
    main()