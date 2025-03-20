from fastapi import FastAPI

"""
"""
CORSMiddleware
origins = [
    "*"
    ]
def lifespan(app: FastAPI):
    pass
    yield
    pass

app = FastAPI(lifespan=lifespan)
app.include_router(router, prefix="/block-chain", tags=["block-chain"])
app.add_middleware(
    CORSMiddleware, 
    allow_origins = origins, 
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)