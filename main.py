# ----------------------------------------
# create fastapi app 
# ----------------------------------------
from fastapi import FastAPI
app = FastAPI()


# ----------------------------------------
# setup templates folder
# ----------------------------------------
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="templates")


# ----------------------------------------
# upload file
# ----------------------------------------
from fastapi import FastAPI, File, UploadFile


# ----------------------------------------
# import custom modules
# ----------------------------------------

# Note: we will be using cython .so istead of .py

# using `.py` module
# from MSS.kadane_modified import MaxSubArrSum

# using `kadaneMSS.so` (CYTHON)
# HAVE to pip install cython and build using `setup.py`
import os
os.system("python setup.py build_ext --inplace")
# we are NOT using MSS.kadane_modified
import kadaneMSS
MaxSubArrSum = kadaneMSS.MaxSubArrSum

# for csv manipulations
import pandas as pd

# ----------------------------------------
# dependency injection
# ----------------------------------------
from fastapi import Depends

def get_db():
	""" returns db session """
	
	try:
		db = SessionLocal()
		yield db
	finally:
		db.close


# ----------------------------------------
# bg tasks
# ----------------------------------------


# ----------------------------------------
# define structure for requests (Pydantic & more)
# ----------------------------------------
from fastapi import Request # for get
from pydantic import BaseModel # for post

class StringRequest(BaseModel):
    intervals       : str
    intervals_vals  : str


# ----------------------------------------
# ----------------------------------------
# routes and related funcs
# ----------------------------------------
# ----------------------------------------
@app.get("/")
def api_home(request: Request):
	"""
	home page
	"""
	
	context = {
		"request": request
	}
	return templates.TemplateResponse("home.html", context)

@app.post("/api/strings/")
def process_string_input(user_req: StringRequest) :
    intervals_list      = user_req.intervals.replace(" ","").split(",")
    intervals_vals_list = user_req.intervals_vals.replace(" ","").split(",")

    intervals_val_list = [float(val) for val in intervals_vals_list]

    mss = MaxSubArrSum(in_arr=intervals_val_list, size=len(intervals_val_list))
    max_sum, lcur, rcur = mss.max_subarray_sum_with_indices()

    #(lower, upper) both are inclusive
    return {
        "max value": max_sum,
        "lower interval": intervals_list[lcur],
        "upper interval": intervals_list[rcur-1]}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    csv_file    = file.file
    df          = pd.read_csv(csv_file)
    #print(df.head())
    intervals_list      = df["time-interval (in any units)"].tolist()
    intervals_val_list  = df["loss/profit (in any units)"].tolist()

    #return {"status": file.filename + " uploaded"}
    mss = MaxSubArrSum(in_arr=intervals_val_list, size=len(intervals_val_list))
    max_sum, lcur, rcur = mss.max_subarray_sum_with_indices()

    #(lower, upper) both are inclusive
    return {
        "max value": max_sum,
        "lower interval": intervals_list[lcur],
        "upper interval": intervals_list[rcur-1]}
# ----------------------------------------
# end
# ----------------------------------------