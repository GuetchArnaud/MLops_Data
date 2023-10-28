
from fastapi import APIRouter, HTTPException
from typing import Any
from datetime import timedelta

router = APIRouter(
    title="MLops_Data",
    description="Cette API est destinée à gerer des informations sur les données mise à disposition.",
    version="1.0.1"
)

@router.post("/logging/")
async def get_post():
    """_summary_
    """