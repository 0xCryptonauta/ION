# ----------------------------------------------------------------------------
# This code takes ion_clawback.csv (from Nostradamus411) 
# and copy address, osmo-total and ion-total at the time of clawback
# ----------------------------------------------------------------------------

import pandas as pd
import json
import os

#os.system('cls||clear')           #<------ uncomment this line to clean terminal each run

ion_genesis_file = "Genesis_data/ion_clawback.csv"

clawback_addr_df = pd.read_csv(ion_genesis_file)

print("\n", "-"*120, sep="")
print("\n\t\t\t\t\tExecuting script #2")
print("\n\tExtracting from", len(clawback_addr_df) ,"addresses the osmos/ion holdings from clawed back snapshot.")

ion_clawback_clean_df = clawback_addr_df[["address", "osmo-total", "ion-total"]]

if not os.path.exists("./Processed_data"):
    os.makedirs("./Processed_data")

ion_clawback_clean_df.to_csv("Processed_data/ion_osmo_clawback.csv", index=False)
ion_clawback_clean_df[["address", "ion-total"]].to_csv("Processed_data/osmo_addr_ion_clawback.csv", index=False)

print("\n\n\t2 files (.csv) were exported to: ./Processed_data \n")
print("\t\t1- ION Clawed back addresses with cosmos and ION holdings.")
print("\t\t\t- ion_osmo_clawback.csv")
print("\t\t2- ION Clawed back addresses with ION holdings.")
print("\t\t\t- osmo_addr_ion_clawback.csv")
print("\n", "-"*120, "\n", sep="")