import pandas as pd
import os

def detect_serious_cases(input_path, output_path):
    # Load the ICSR dataset
    df = pd.read_csv(input_path)

    # Filter serious cases
    serious_cases = df[df['Seriousness'].str.lower() == 'serious']

    # Create output folder if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save serious cases to output file
    serious_cases.to_csv(output_path, index=False)

    print(f"✅ Flagged {len(serious_cases)} serious cases. Saved to {output_path}")

# Run the module directly
if __name__ == "__main__":
    detect_serious_cases(
        input_path=r"C:\Users\prave\OneDrive\Desktop\PV DATA\data\ICSR_CASES_CSV.csv",
        output_path=r"C:\Users\prave\OneDrive\Desktop\PV DATA\outputs\flagged_cases.csv"
    )
