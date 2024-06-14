import pandas as pd
import csv;
import json;

def csv_to_list_of_dicts(file_path):
   df=pd.read_csv(file_path)
   record_dict=json.loads(df.to_json(orient="records"))
   record_json=json.dumps(record_dict)
   return record_json;

def extract_data_from_csv(file_path):
    """Read data from a CSV file and return a DataFrame."""
    try:
        df = pd.read_csv(file_path)
        df=[DataObject(**row) for row in df.to_dict(orient='records')]
        print(f"Successfully read {file_path}")
        return df
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None
def align_columns(master_df, source_df):
    """Align columns of the source DataFrame to match the master DataFrame."""
    missing_cols = set(master_df.columns) - set(source_df.columns)
    for col in missing_cols:
        source_df[col] = None
    return source_df[master_df.columns]

def compare_datasets(master_df, source_df, source_file_name):
    """Compare master dataset with source dataset and identify differences."""
    differences = []
    print(len(type(master_df)));
    # Align columns of source_df to match master_df
    # source_df = align_columns(master_df, source_df)
    return;
    for i in range(0, max(len(master_df))):
        master_row = master_df.iloc[i] if i < len(master_df) else None
        # source_row = source_df.iloc[i] if i < len(source_df) else None
        print(master_row)
        return
        if master_row is None:
            differences.append({
                'row': i + 1,
                'type': 'Missing in master',
                'master_data': None,
                'source_data': source_row.to_dict() if source_row is not None else None,
                'source_file': source_file_name
            })
        elif source_row is None:
            differences.append({
                'row': i + 1,
                'type': 'Missing in source',
                'master_data': master_row.to_dict(),
                'source_data': None,
                'source_file': source_file_name
            })
        else:
            row_diff = {}
            for col in master_df.columns:
                master_value = master_row[col]
                source_value = source_row[col]
                if master_value != source_value:
                    row_diff[col] = {'master': master_value, 'source': source_value}
            if row_diff:
                differences.append({
                    'row': i + 1,
                    'type': 'Mismatch',
                    'differences': row_diff,
                    'source_file': source_file_name
                })

    return differences

def write_differences_to_csv(differences, output_file_path):
    """Write the differences to a new CSV file."""
    differences_df = pd.DataFrame(differences)
    differences_df.to_csv(output_file_path, index=False)
    print(f"Differences written to {output_file_path}")

def compare_multiple_files(master_file, source_files, output_file):
    """Compare a master file with multiple source files and output the differences."""
    Print("My name is ARTI")
    master_df = csv_to_list_of_dicts(master_file)
    master_df = json.loads(master_df)
    source_df=csv_to_list_of_dicts(source_files);
    differences=[];
    source_df=json.loads(source_df);
    for i in range(0,len(master_df)):
        for j in range(0,len(source_df)):
            if master_df[i]["Publication GUID"]==source_df[j]["Publication ID"] and master_df[i]["Object GUID"]==source_df[j]["Activation Topic GUID"]:
                differences.append(
                    {
                    'row': j,
                    "Publication GUID":master_df[i]["Publication GUID"],
                    "Object GUID":master_df[i]["Object GUID"],
                    'type': 'matched',
                    'fileType': 'activation',
                }
                )
    write_differences_to_csv(differences, output_file)
    # for source_file in source_files:
    #     source_df = extract_data_from_csv(source_file)
    #     print(source_df);
    #     if source_df is None:
    #         print(f"Skipping file {source_file} due to read error.")
    #         continue

    #     try:
    #         differences = compare_datasets(master_df, source_df, source_file)
    #         all_differences.extend(differences)
    #     except Exception as e:
    #         print(f"Error comparing {master_file} with {source_file}: {e}")
    #         continue

    # if all_differences:
    #     write_differences_to_csv(all_differences, output_file)
    #     print(f"Differences found and written to {output_file}")
    # else:
    #     print('No differences found.')

# Example usage
master_file_path = 'Hierarchical.csv'
source_file_paths='Activation.csv'
# source_file_paths = [
#     'Activation.csv',

# ]
output_file_path = 'differences.csv'

compare_multiple_files(master_file_path, source_file_paths, output_file_path)
