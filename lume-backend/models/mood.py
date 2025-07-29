#This file defines the structure of input/output data - means what information is needed and what format must it be

from pydantic import BaseModel

#pydantic is a python library that is used to define and validate date using Python classes 
#BaseModel is the class that we inherit to make our own models

class MoodRequest(BaseModel):
    text : str