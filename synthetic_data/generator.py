import json
import uuid
from datetime import datetime


def make_sample(sample_type='blood'):
sid = str(uuid.uuid4())
return {
'sample_id': sid,
'patient_id': str(uuid.uuid4()),
'sample_type': sample_type,
