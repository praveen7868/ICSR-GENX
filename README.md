# ICSR-GENX 🚀  
**GenAI-Powered Drug Safety Intelligence and ICSR Automation**

ICSR-GENX is a simulation project that automates key pharmacovigilance workflows using GenAI and rule-based logic. Inspired by Accenture’s SynOps platform, it showcases how independent innovators can replicate enterprise-grade ICSR processing — including adverse event detection, SLA tracking, causality assessment, and narrative generation — using cost-free tools.

---

## 🔍 Project Scope

- ✅ Case validation and triage
- ✅ Serious adverse event detection
- ✅ SLA compliance tracking (7-day/15-day deadlines)
- ✅ Causality assessment (Naranjo scale)
- ✅ GenAI-powered narrative generation
- ✅ Audit trail logging for inspection readiness

---

## 🔄 ICSR Workflow Simulated

1. **Case Receipt** – Intake of ADR data from structured sources  
2. **Case Validation** – Check for minimum criteria (patient, reporter, drug, event)  
3. **Duplicate Check** – Simulated duplicate detection logic  
4. **Case Triage** – Classify as serious or non-serious  
5. **SLA Compliance** – Track regulatory timelines and flag overdue cases  
6. **Causality Assessment** – Score using Naranjo scale logic  
7. **Narrative Generation** – Auto-generate ICSR text using GenAI or templates  
8. **Audit Logging** – Record actions for inspection simulation  
9. **Final Output** – Summary report per case

---

## 🛠️ Tech Stack

- Python (Jupyter Notebook or CLI)
- Pandas, Matplotlib
- Optional: Hugging Face Transformers, spaCy
- CSV/JSON for input/output
- No paid APIs or cloud dependencies

---

## 📁 Folder Structure

---

## 📣 Why This Project?

Accenture’s SynOps platform reduced PV report timelines from 50+ days to under a minute using GenAI. ICSR-GENX shows how similar intelligence can be simulated independently — without paid APIs or cloud infrastructure.

This project is ideal for:
- Pharmacovigilance and Clinical data management role job seekers
- Recruiters evaluating GenAI readiness
- Academic publishing and portfolio building

---

## 📎 License

MIT – Free to use, adapt, and build upon.

---

## 📂 Data Sources

Data used in this project was derived from publicly accessible pharmacovigilance databases, including:

- [WHO VigiAccess](https://vigiaccess.org/)
- [FDA FAERS](https://www.fda.gov/drugs/questions-and-answers-fdas-adverse-event-reporting-system-faers/fda-adverse-event-reporting-system-faers)
- [EU ADR Reports](https://www.adrreports.eu/)
- [OpenVigil](https://openvigil.sourceforge.net/)
- [Canada Vigilance](https://health-products.canada.ca/adverse-reaction-monitoring/index-eng.jsp)
- [Japan PMDA](https://www.pmda.go.jp/english/safety/info-services/adr-info/0001.html)
- [Australia DAEN](https://www.tga.gov.au/database-adverse-event-notifications-daen)
- [SIDER](http://sideeffects.embl.de/)
- [OpenFDA API](https://open.fda.gov/apis/)

> ⚠️ *Note: This project does not extract or process real patient data. All datasets used are simulated and anonymized for educational and demonstration purposes only. Data structures are inspired by publicly available pharmacovigilance portals.*

---

## 📚 References

- Accenture. (2023). *SynOps for Pharmacovigilance: Transforming Drug Safety with GenAI*. [Accenture PV SynOps Overview](https://www.accenture.com/us-en/services/life-sciences/synops-pharmacovigilance)
- U.S. FDA. *Postmarketing Safety Reporting Requirements for Human Drug and Biological Products*. [FDA Guidance](https://www.fda.gov/media/78504/download)
- WHO. (2002). *Safety Monitoring of Medicinal Products: Guidelines for Setting Up and Running a Pharmacovigilance Centre*. [WHO PV Manual](https://apps.who.int/iris/handle/10665/42493)
- Naranjo CA et al. (1981). *A method for estimating the probability of adverse drug reactions*. Clin Pharmacol Ther. [PubMed Link](https://pubmed.ncbi.nlm.nih.gov/7249508/)
- EMA. *EudraVigilance and ICSR Reporting Requirements*. [EMA Guidance](https://www.ema.europa.eu/en/human-regulatory/research-development/pharmacovigilance/eudravigilance)
