from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter()


class ReferralReq(BaseModel):
sample_id: str
urgency: str
specialties: list


@router.post("/create")
async def create_referral(req: ReferralReq):
# calls referral engine microservice (placeholder)
return {"referral_id": "ref-123", "status": "dispatched"}
