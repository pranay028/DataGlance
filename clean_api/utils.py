import pandas as pd
from pandas_profiling import ProfileReport
import uuid

def generate_profiling_report(file):
    # Check file extension
    file_extension = file.name.split('.')[-1].lower()

    if file_extension == 'csv':
        df = pd.read_csv(file)
    elif file_extension in ['xlsx', 'xls']:
        df = pd.read_excel(file)
    else:
        raise ValueError('Unsupported file format')

    # Generate profiling report
    profile = ProfileReport(df, title="Profiling Report")
    
    
    report_html = profile.to_html()
    columns_info = columns_with_new_id(df)

    return (report_html,columns_info)


def columns_with_new_id(df):
    
    columns_id = []
    for col in df.columns:
        unique_id = uuid.uuid4()
        print(unique_id)
        type = str(df[col].dtype)
        
        columns_id.append({'name': col, "type":type, "col_id": unique_id})
    return columns_id