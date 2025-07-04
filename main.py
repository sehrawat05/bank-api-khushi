import pandas as pd
from fastapi import FastAPI,HTTPException

app=FastAPI()
df=pd.read_csv("banks.csv")

banks_list=df["bank_name"].unique().tolist()
branches_by_bank=df.groupby("bank_name").apply(lambda x: x.to_dict(orient="records")).to_dict()
branch_lookup=df.set_index("ifsc").T.to_dict()

#endpoints
@app.get("/banks")
def get_banks():
    return {"banks": banks_list}

@app.get("/banks/{bank_name}/branches")
def get_branches(bank_name: str):
    if bank_name not in branches_by_bank:
        raise HTTPException(status_code=404, detail="Bank not found.")
    return branches_by_bank[bank_name]

@app.get("/branches/{ifsc}")
def get_branch_by_ifsc(ifsc: str):
    if ifsc not in branch_lookup:
        raise HTTPException(status_code=404, detail="IFSC not found.")
    return branch_lookup[ifsc]
