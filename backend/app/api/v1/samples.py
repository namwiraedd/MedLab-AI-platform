from fastapi import APIRouter, Body
from pydantic import BaseModel
from typing import Optional
from ..models import SampleModel


router = APIRouter()


class SampleIn(BaseModel):
sample_id: str
patient_id: str
sample_type: str
collected_at: Optional[str]
metadata: dict = {}


@router.post("/ingest")
async def ingest_sample(payload: SampleIn):
# AI-driven QC placeholder
qc_ok = True
if not qc_ok:
return {"status": "rejected", "reason": "quality"}
# persist to DB and object store (placeholder)
return {"status": "accepted", "sample_id": payload.sample_id}
