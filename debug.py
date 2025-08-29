import uvicorn

from evenfasterapi import JSONAPI

if __name__ == "__main__":
    api = JSONAPI()
    uvicorn.run(api)