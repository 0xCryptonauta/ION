# ION

### 1- What is this repository?

Curiosity about ION is strong and i just wanted to play with the data given by @sunnya97 (genesis) and @Nostradamus411 (clawback)

### 2- Self interest

A mysterious airdrop was given to cosmos voters and sikka stakers and i found myself with an ION due to voting once. Time passed and interest grew on me (after the clawback was executed) about what happened with all those 16461 addresses that were gifted ION at genesis.

### 3- My approach

The [GENESIS](https://github.com/sunnya97/sunnya97.github.io/blob/master/fsociety.zip) files were given by @sunnya97 but encrypted in a .zip file named fsociety.zip. The password (🧿) was discovered by someone i do not recall but from the ION Governance Working Group Telegram. @Nostradamus411 uploaded the [GENESIS FILES](https://github.com/Nostradamus411/ion-airdrop-code) to github. **This repo is used to get the ions.json file (cosmos genesis addresses)**

6 months after genesis, a clawback was proposed/executed to claim all the ION that were in dust wallets. Once again, @Nostradamus411 uploaded a snapshot of osmosis state after the [CLAWBACK](https://github.com/Nostradamus411/ion-clawback-snapshot). **This repo is needed because of ion_clawback_snapshot.csv**

### 4- Scripts

- **1-Cosmos_Addr2_Osmosis.py**

    Takes the Original_data/ions.json with the genesis cosmos addresses and converts them to osmo addresses and saves 2 new csv files to ./Processed_data named:
    
    - cosmos_addr_ion_genesis.csv --> Genesis with cosmos address
    - osmo_addr_ion_genesis.csv   --> Genesis with osmo address
    
    
- **2-Getting_addr_w_ion_clawback.py**

    Takes the Original_data/ion_clawback_snapshot.csv from the clawback and extracts only the addresses that hodl ION and the osmo/ION holdings and saves 2 new csv files to ./Processed_data named:
    
    - ion_osmo_clawback.csv --> Clawback addresses only with osmo and ION holdings.
    - osmo_addr_ion_clawback.csv --> Clawback addresses only with ION holdings.
    
    
- **3-Genesis_vs_Clawback.py**

    Takes the osmo_addr_ion_clawback.csv and the osmo_addr_ion_genesis.csv files and compares which addresses from the genesis files are found in the clawback file. these addresses are the one hodling ION from genesis and saves 1 new csv file to ./Processed_data named: 
    - ION_true_hodlers.csv --> Osmo addresses hodling ION since genesis.
    
### 5- About the scripts

These scripts are written in python.

    - Create a virtual environment
    - Install requirements.txt
    - Execute scripts in order
    
Inside the .py files you can find lots of print(). 
This is done to get a pretty print in terminal (no more).

- In the addresses that are hodling ION since genesis there are some with a tiny amount (0.000001) that make them appear in the list

### 6- Data Analysis

This will be approach once i get more time to play around this data.

## **At the clawback snapshot time there were 3039 addresses hodling ION but 1207 addresses are hodling since genesis (airdropped addresses)**

