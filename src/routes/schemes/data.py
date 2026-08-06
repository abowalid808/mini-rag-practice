# describe the style and structure of the request from user

from pydantic import BaseModel
from typing import Optional
class ProcessRequest(BaseModel):
    file_id: str
    chunk_size: Optional[int] = 10   
    overlap_size: Optional[int] = 20  
    do_reset : Optional[int] =  0 # when user want to make a new request and reset the previous data, he can set this value to 1
    