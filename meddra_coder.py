import pandas as pd
import os

def code_event_terms(input_path, dict_path, output_path):
    # Load flagged cases and MedDRA dictionary
    cases_df = pd.read_csv(input_path)
    meddra_df = pd.read_csv(dict_path)

    # Merge on Event Term
    coded_df = pd.merge(
        cases_df,
        meddra_df,
        on='Event Term',
        how='left'  # keep unmatched terms for review
    )

    # Create output folder if needed
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save coded cases
    coded_df.to_csv(output_path, index=False)
    print(f"✅ MedDRA coding complete. Saved to {output_path}")

# Run directly
if __name__ == "__main__":
    code_event_terms(
        input_path=r"C:\Users\prave\OneDrive\Desktop\PV DATA\outputs\flagged_cases.csv",
        dict_path=r"C:\Users\prave\OneDrive\Desktop\PV DATA\data\MedDRA_Dictionary.csv",
        output_path=r"C:\Users\prave\OneDrive\Desktop\PV DATA\outputs\meddra_coded_cases.csv"
    )
