
def unauthorized():
    from fastapi import HTTPException
    raise HTTPException(status_code=403, detail="Unauthorized session")
