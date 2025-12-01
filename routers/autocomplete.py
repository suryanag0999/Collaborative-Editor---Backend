from fastapi import APIRouter
from pydantic import BaseModel
from typing import Literal


router = APIRouter()


class AutocompleteRequest(BaseModel):
    code: str
    cursorPosition: int
    language: Literal['python']



class AutocompleteResponse(BaseModel):
    suggestion: str


@router.post('/autocomplete', response_model=AutocompleteResponse)
def autocomplete(req: AutocompleteRequest):
    token = ''
    s = req.code[:req.cursorPosition]
    for char in reversed(s):
        if char.isalnum() or char == '_':
            token = char + token
        else:
            break
    if token.startswith('pri'):
        return {"suggestion": "print()"}
    if token == 'def':
        return {"suggestion": "def function_name(params):\n pass"}
    return {"suggestion": "# suggestion: consider adding a docstring"}