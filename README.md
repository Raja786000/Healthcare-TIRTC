# Healthcare Analytics for Doctor Visits (TIRTC)

**Student:** Raja Babu  
**AICTE Student ID:** STU67790a53c658b1735985747  
**Email:** rafficial807@gmail.com  
**GitHub:** https://github.com/Raja786000/Healthcare-TIRTC

## Project
Exploratory healthcare analytics using Python on the supplied Doctor Visits dataset.

## Dataset
- Records: 5,190
- Columns: 13
- Dataset file: `DoctorVisits.csv`

## Analysis performed
1. Read the dataset.
2. Display complete column information.
3. Calculate descriptive statistics.
4. Count male and female patients.
5. Analyse minimum, maximum and mean income.
6. Analyse reduced-activity days by gender.
7. Find the total number of people by illness count.
8. Visualize missing values with a heatmap.
9. Analyse income versus hospital visits.
10. Count illness by gender.
11. Calculate insurance-indicator percentages.
12. Plot reduced-activity days by gender.

## Main illness-count result
- Illness count 0: **1,554 people**
- Illness count 1: **1,638 people**
- Illness count 2: **946 people**
- Illness count 3: **542 people**
- Illness count 4: **274 people**
- Illness count 5: **236 people**

## Run the project
### Jupyter Notebook
```bash
pip install -r requirements.txt
jupyter notebook Healthcare_Analytics_Doctor_Visits.ipynb
```

Run the notebook cells from top to bottom.

### Python script
```bash
pip install -r requirements.txt
python healthcare_analysis.py
```

## Deliverables
- `DoctorVisits.csv` — dataset
- `Healthcare_Analytics_Doctor_Visits.ipynb` — complete notebook
- `healthcare_analysis.py` — standalone Python analysis
- `requirements.txt` — dependencies
- `analysis_summary.json` — computed summary
