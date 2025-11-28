from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import JSONResponse
from .api.v1 import samples, referrals
from .auth import KeycloakAuth


app = FastAPI(title="MedLab AI LIMS")


auth = KeycloakAuth(
server_url="${KEYCLOAK_URL}",
realm="medlab",
)


app.include_router(samples.router, prefix="/api/v1/samples", dependencies=[Depends(auth.require_auth)])
app.include_router(referrals.router, prefix="/api/v1/referrals", dependencies=[Depends(auth.require_auth)])


@app.get("/health")
async def health():
return {"status": "ok"}
