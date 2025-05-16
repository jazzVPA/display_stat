
# Display Metrology Statistical Analysis Tool

This project provides a comprehensive statistical analysis toolkit for display metrology data, with a focus on **luminance** and **chromaticity (x, y)**. It includes process capability indices, distribution characteristics, and graphical representations.

---

## Files

- `display_Lxy_data.csv`: Synthetic dataset of display luminance and chromaticity with large variation.
- `spc_stat.py`: Python script for complete analysis.

- 'SPC_and_stat.pdf': equations and sample output data with graphs

- `README.md`: Project overview and usage instructions.

---

## Features

- Descriptive Statistics: Mean, Median, Std Dev, Min, Max, Range
- Higher-Order Stats: Skewness & Kurtosis
- Process Capability: Cp, Cpu, Cpl, Cpk
- Confidence Interval for Mean (95%)
- Normality Test: Shapiro-Wilk
- Outlier Detection using IQR method
- Histograms with USL, LSL, and Mean
- Separate analysis and visualization for Chromaticity x and y

---

## 🚀 How to Use

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/display-Lxy_stat.git
display-Lxy_stat
```

### 2. Install Dependencies

```bash
pip install pandas numpy matplotlib scipy
```

### 3. Run the Analysis Script

```bash
python spc_stat.py
```

This will output detailed statistical analysis in the terminal and show visual plots for each metric.

---

## Example Output can seen in the pdf document

