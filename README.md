## 🎯 Featured Project: Climate Risk Map for Bank Branches  

**Overview**  
As part of my learning journey, I built a project that combines financial data with environmental risk.  
I connected over 1,750 bank branches in Maryland, DC, and Virginia with FEMA’s climate risk index to see how exposure to climate hazards might impact financial institutions.  
This project helped me strengthen skills in data cleaning, database design, SQL, and visualization, while also exploring a real-world problem I care about: climate risk.  

---

## 🔎 Key Insights  

- **Baltimore, MD** and **Fairfax, VA** have the highest climate risk scores among DMV counties.  
- **Capital One** holds over **$370M** in deposits in high-risk counties — far more than any other bank.  
- Total deposits in high-risk DMV counties exceed **$586M**, showing significant financial exposure concentrated in just a few institutions.  

---

## 📊 Interactive Dashboards  

- [Climate Risk DMV (Map View)](https://public.tableau.com/app/profile/fikreab.mezgebu/viz/climateriskdmv/ClimateRiskDMV)  
- [Climate Risk & Banking Exposure in DMV (Dashboard)](https://public.tableau.com/app/profile/fikreab.mezgebu/viz/ClimateRiskBankingExposureinDMV/ClimateRiskBankingExposureinDMV)  

---

## 💻 What I Did  

- Collected FDIC branch-level banking data (locations, deposits) for Maryland, DC, and Virginia  
- Merged with FEMA climate risk scores at the county level  
- Standardized files into the same format (consistent column names, units, and values)  
- Developed Jupyter notebooks to clean each state’s data and keep the process reproducible  
- Designed a SQLite database with separate state tables and one combined table  
- Wrote SQL queries to answer practical questions (e.g., highest-risk counties, banks in high-risk areas)  
- Exported results to CSV files and built Tableau dashboards for visual exploration  
- Outlined a simple Flask API to make the same data available in JSON format  

---

## 🛠️ Tools I Learned/Used  

Python (Pandas), SQL (SQLite), Jupyter Notebooks, Tableau, Flask (API basics)  

---

## 📂 Project Structure  

- **API/** – Flask app (`app.py`) to demonstrate how SQL results could be served  
- **cleaned_data/** – Final state-level cleaned files (MD, DC, VA)  
- **notebook/** – Step-by-step cleaning notebooks  
- **outputs/** – Combined datasets and SQL query results for Tableau  
- **raw/** – Original datasets before cleaning (FDIC, FEMA, Census)  
- **sql/** – SQLite database (`dmv_banks.db`) and SQL queries  
- **tableau/** – Tableau dashboards (`.twbx`) for interactive visualizations  
- **README.md** – This file  

---

## 🌍 Data Sources & Credits  

- **FEMA National Risk Index** – County-level climate risk scores  
  Source: [FEMA National Risk Index](https://www.fema.gov/flood-maps/products-tools/national-risk-index)  

- **FDIC Bank Branch Data** – Branch locations and deposits  
  Source: [FDIC](https://www.fdic.gov)  

- **U.S. Census Bureau** – City-to-county matching and boundary reference  
  Source: [U.S. Census Bureau](https://www.census.gov)  

(All data is public and credited to the original providers.)  

---

## ✨ Why This Matters to Me  

I wanted this project to be more than just practice with data.  
Climate risk is a growing challenge, and banks are at the front line of economic stability. By combining banking and climate data, I learned how to:  

- Think carefully about data consistency across multiple sources  
- Use SQL to structure and query real-world data  
- Turn raw numbers into insights with Tableau  
- Plan ahead for sharing results through an API  

This project gave me confidence not just in technical tools, but also in tackling complex, messy data with a real-world impact.  
