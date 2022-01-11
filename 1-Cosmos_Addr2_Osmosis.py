import pandas as pd
import numpy as np
import bech32
import json
import os


#---- Taken from Nostradamus411 github - https://github.com/Nostradamus411/ion-airdrop-code ---------
#----------------------------------------------------------------------------------------------------


# Function to convert a bech32 address from a Cosmos to Osmosis variant - 

def atom_to_osmo(atom_addr):
    atom_tuple = bech32.bech32_decode(atom_addr)
    #print("atom_tuple: ", atom_tuple)
    data = atom_tuple[1]
    #print("data: ", data)
    osmo_addr = bech32.bech32_encode('osmo',data) 
    #print("osmo_addr: ", osmo_addr)    
    return osmo_addr


genesis_file = 'Genesis_data/ions.json'   #Contains the cosmos address with the quantity of IONs given in genesis

#----------------------------------------------------------------------------------------------------
                                            
g_file = open(genesis_file)
genesis_json = json.load(g_file)
g_file.close()

genesis_cosmos_df = pd.DataFrame(columns=["Cosmos Addr", "Ion Qty"])
genesis_osmo_df = pd.DataFrame(columns=["Osmo Addr", "Ion Qty"])

p100 = len(genesis_json)
p1 = int(np.floor(p100/100))

os.system('cls||clear')

print("-"*120)
print("\n\tConverting", p100, "Cosmos addresses to Osmo addresses.\n")


i = 1
p = 0
for address in genesis_json:
  genesis_cosmos_df = genesis_cosmos_df.append({"Cosmos Addr":address, "Ion Qty":genesis_json[address]}, ignore_index=True)
  genesis_osmo_df = genesis_osmo_df.append({"Osmo Addr":atom_to_osmo(address), "Ion Qty":genesis_json[address]}, ignore_index=True)
  if i % p1 == 0:
    p += 1
    print("\t","*"*p, " "*(100-p), " ", p, "%", sep="", end="\r")

  i += 1

if not os.path.exists("./Processed_data"):
    os.makedirs("./Processed_data")

genesis_cosmos_df.to_csv("Processed_data/cosmos_addr_ion_genesis.csv", index=False)
genesis_osmo_df.to_csv("Processed_data/osmo_addr_ion_genesis.csv", index=False)

print("\n\n\t2 files (.csv) were exported to: ./Processed_data \n")
print("\t\t1- ION Genesis with cosmos addresses.")
print("\t\t2- ION Genesis with osmos addresses.")
print("\n", "-"*120, sep="")