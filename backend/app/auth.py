from fastapi import Request, HTTPException, Depends
from fastapi.security import HTTPBearer
from jose import jwt
import os


class KeycloakAuth:
def __init__(self, server_url: str, realm: str):
self.server_url = server_url
self.realm = realm
self.jwk_uri = f"{server_url}/realms/{realm}/protocol/openid-connect/certs"


async def require_auth(self, request: Request):
auth_header = request.headers.get("authorization")
if not auth_header:
raise HTTPException(status_code=401, detail="Missing token")
token = auth_header.split(" ")[1]
try:
# For demo: we will not verify key rotation here. Use python-keycloak in prod.
payload = jwt.get_unverified_claims(token)
return payload
except Exception as e:
raise HTTPException(status_code=401, detail=str(e))
