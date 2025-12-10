# 📊 Vacancy Tech Trends

## 📋 Project Description

**Vacancy Tech Trends** is a Python-based analytics project that collects, processes, and visualizes data from Python-related job postings.

The project includes a Jupyter Notebook, processed CSV data, plots, and insights.

The analysis covers: job title word frequency, experience level distribution (Jr/Mid/Sr), heatmaps, salary analysis and more.

## 👥 Target Users

*   🧑‍💻 **Analysts** – explore job market trends
*   🧪 **Students & Juniors** – understand real expectations in Python roles
*   📈 **HR & Recruiters** – view job title frequency and demand trends

## 📂 Files in Repository

*   `analysis.ipynb` – Jupyter Notebook with full analysis 🧠
*   `jobs_analysis.csv` – cleaned and processed dataset 📄
*   `plots/` – directory with generated graphs 📊
*   `requirements.txt` – list of dependencies 🐍

## 📊 Analysis Sections

*   **🔤 Job Titles Analysis** – most frequent words in job titles
*   **🎚️ Experience Levels** – distribution of Junior / Mid / Senior / Unknown
*   **🔥 Heatmap (Titles vs Experience)** – comparison of job titles and levels
*   **💰 Salary Analysis** – salary distribution and averages (if available)

## ⚠️ Notes

*   🤖 Scraping uses only public data — no login required.
*   🛡️ The script uses a minimal number of requests to avoid overloading servers.
*   📦 Analysis is performed using Pandas, NumPy, Matplotlib, and Seaborn.
*   🏷️ Experience levels are normalized to: Jr, Mid, Sr, Unk.
*   🗂️ The CSV contains processed titles, experience levels, and salaries (if available).

## 🚀 How to Run Locally

### 🌿 1. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows
```

### 📥 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 📘 3. Open the Jupyter Notebook

```bash
jupyter notebook analysis.ipynb
```

### ▶️ 4. Run all cells

#### Run all notebook cells to perform data cleaning, analysis, and chart generation.