import pandas as pd
import os

def generate_narratives(input_path, output_path):
    df = pd.read_csv(input_path)

    def create_summary(row):
        age = row.get('Patient_Age', 'unknown')
        gender = row.get('Gender', 'unknown').lower()
        country = row.get('Country', 'unspecified')
        drug = row.get('Drug_Name', 'unspecified')
        event = row.get('Preferred Term') or row.get('Event_Term', 'unspecified')
        seriousness = row.get('Seriousness', 'unspecified').lower()
        outcome = row.get('Outcome', 'unspecified').lower()

        return (
            f"A {age}-year-old {gender} patient from {country} reported {event.lower()} "
            f"following administration of {drug}. The case was classified as {seriousness} "
            f"and the outcome was {outcome}."
        )

    df['Narrative Summary'] = df.apply(create_summary, axis=1)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"✅ Narratives generated and saved to {output_path}")

# Run directly
if __name__ == "__main__":
    generate_narratives(
        input_path=r"C:\Users\prave\OneDrive\Desktop\PV DATA\outputs\meddra_coded_cases.csv",
        output_path=r"C:\Users\prave\OneDrive\Desktop\PV DATA\outputs\narrative_cases.csv"
    )
