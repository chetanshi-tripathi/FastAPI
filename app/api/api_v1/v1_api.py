from fastapi import APIRouter

from .endpoints import employee

router= APIRouter()
router.include_router(employee.router, prefix="/employee", tags={"Emp[loyee"})