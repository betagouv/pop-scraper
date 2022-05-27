import pandas as pd
import os, shutil, argparse
from exports.lib import load_export_df

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('path', help='path to the export csv from scrapy with all items')
args = parser.parse_args()
path = args.path

# path = os.path.join(current_path, )

df = load_export_df(path)

current_path = os.path.dirname(os.path.abspath(__file__))
filename_without_ext = os.path.basename(path).replace(".csv", "")
output_dir = os.path.join(current_path, f"{filename_without_ext}")
if os.path.exists(output_dir):
    shutil.rmtree(output_dir)
os.mkdir(output_dir)

dpts = sorted(df.DPT.dropna().unique())
for dpt in dpts:
    df_dpt = df[df.DPT == dpt]
    output_path = os.path.join(output_dir, f"{filename_without_ext}_dpt_{dpt}.csv")
    print(f"exporting {df_dpt.shape[0]} rows into {output_path}")
    df_dpt.to_csv(output_path, index=False)
    


