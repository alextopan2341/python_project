from fastapi import FastAPI, Depends, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from . import schemas, utils, crud, db, dependencies

app = FastAPI(title="Calculator with SQLite")

# Inițializare DB
@app.on_event("startup")
def on_startup():
    db.init_db()

# Prometheus counter
REQUEST_COUNT = Counter("request_count", "Total requests", ["operation"])

@app.get("/metrics")
def metrics():
    data = generate_latest()
    return Response(data, media_type=CONTENT_TYPE_LATEST)

@app.post("/pow", response_model=schemas.CalcResponse, dependencies=[Depends(dependencies.api_key_auth)])
def pow_endpoint(req: schemas.CalcRequest, db=Depends(dependencies.get_db)):
    result = utils.compute_pow(req.x, req.y or 0)
    REQUEST_COUNT.labels(operation="pow").inc()
    crud.log_request(db, req, "pow", result)
    return schemas.CalcResponse(operation="pow", x=req.x, y=req.y, result=result)

@app.post("/fibonacci/{n}", response_model=schemas.CalcResponse, dependencies=[Depends(dependencies.api_key_auth)])
def fib_endpoint(n: int, db=Depends(dependencies.get_db)):
    result = utils.compute_fib(n)
    REQUEST_COUNT.labels(operation="fibonacci").inc()
    req = schemas.CalcRequest(x=n, y=None)
    crud.log_request(db, req, "fibonacci", result)
    return schemas.CalcResponse(operation="fibonacci", x=n, y=None, result=result)

@app.post("/factorial/{n}", response_model=schemas.CalcResponse, dependencies=[Depends(dependencies.api_key_auth)])
def fact_endpoint(n: int, db=Depends(dependencies.get_db)):
    result = utils.compute_fact(n)
    REQUEST_COUNT.labels(operation="factorial").inc()
    req = schemas.CalcRequest(x=n, y=None)
    crud.log_request(db, req, "factorial", result)
    return schemas.CalcResponse(operation="factorial", x=n, y=None, result=result)
