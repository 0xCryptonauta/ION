import pandas as pd
import numpy as np
import os

#os.system('cls||clear')           #<------ uncomment this line to clean terminal each run

def ion_report():
    total_airdrop_addr = genesis_df["Ion Qty"].count()
    total_supply = clawback_df["ion-total"].sum()
    clawed_back_qty = clawback_df["ion-total"].max()
    circ_supply = total_supply - clawed_back_qty
    comm_pool_info = clawback_df.loc[clawback_df["ion-total"] == clawback_df["ion-total"].max()]
    clawed_back_addr = clawback_df["ion-total"].count()
    print("\t"*5, "ION Report:\n", sep="")
    print("\tTotal ION supply: ", np.round(total_supply, 3))
    print("\tTotal of IONs addresses in genesis: ", total_airdrop_addr)
    print("\tTotal of IONs that were clawed back: ", np.round(clawed_back_qty, 3))
    print("\tTotal of IONs in circulation after clawback: ", np.round(circ_supply, 3))
    print("\tNumber of addresses with ION (including comm_pool): ", clawed_back_addr)

    print("\n\tInfo about IONs that were clawed back\n\t", comm_pool_info.to_string(index=False).replace("\n", "\n\t"))


genesis_file = "Processed_data/osmo_addr_ion_genesis.csv"
clawback_file = "Processed_data/osmo_addr_ion_clawback.csv"

genesis_df = pd.read_csv(genesis_file)
clawback_df = pd.read_csv(clawback_file)

print("\n", "-"*120, sep="")
print("\n\t\t\t\t\tExecuting script #3")
print("\n\tComparing ION hodlers in clawback snapshot to genesis.")

ion_hodlers_df = pd.DataFrame(columns=["Address", "Genesis Qty", "Clawback Qty"])

for addr_gen in genesis_df["Osmo Addr"]:
  for addr_claw in clawback_df["address"]:
    if addr_gen == addr_claw:
      gen_qty = genesis_df[genesis_df["Osmo Addr"] == addr_gen]["Ion Qty"].values
      claw_qty = clawback_df[clawback_df["address"] == addr_claw]["ion-total"].values

      ion_hodlers_df = ion_hodlers_df.append({"Address":addr_gen, "Genesis Qty":gen_qty[0], "Clawback Qty":claw_qty[0]}, ignore_index=True)

if not os.path.exists("./Processed_data"):
    os.makedirs("./Processed_data")

ion_hodlers_df.to_csv("Processed_data/ION_true_hodlers.csv", index=False)

print("\n\n\t1 file (.csv) was exported to: ./Processed_data \n")
print("\t\t1- Osmo addresses that HODL ION since genesis")
print("\t\t\t- ION_true_hodlers.csv")
print("\n", "-"*120, "\n", sep="")

#ion_report()

comm_pool_info = clawback_df.loc[clawback_df["ion-total"] == clawback_df["ion-total"].max()]
clawed_back_addr = clawback_df["ion-total"].count()

print("\n\tAt the clawback snapshot time there were", clawed_back_addr, "addresses hodling ION")
print("\tbut", len(ion_hodlers_df), "addresses are hodling since genesis (airdropped addresses)")
print("\n", "-"*120, "\n", sep="")