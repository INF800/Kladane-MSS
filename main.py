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
# setup db
# ----------------------------------------


# ----------------------------------------
# import custom modules
# ----------------------------------------
from MSS.kadane_modified import MaxSubArrSum


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

    print("+"*100)
    print(intervals_val_list)
    print(len(intervals_val_list))
    print("+"*100)

    mss = MaxSubArrSum(in_arr=intervals_val_list, size=len(intervals_val_list))
    max_sum, lcur, rcur = mss.max_subarray_sum_with_indices()

    print(max_sum, lcur, rcur)
    print(intervals_val_list)
    print(intervals_list)

    #(lower, upper) both are inclusive
    return {
        "max value": max_sum,
        "lower interval": intervals_list[lcur],
        "upper interval": intervals_list[rcur-1]}

# ----------------------------------------
# end
# ----------------------------------------