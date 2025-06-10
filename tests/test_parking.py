# tests/test_parking.py
import pytest
import httpx
from DataTalks.arena import (
    AREENA,                       # (lat, lon) of Metro Areena
    nearest_parking_ids,
    parking_status,
    facility_prediction,
)


@pytest.mark.asyncio
async def test_nearest_ids():
    """
    We should always find at least one CAR and one BICYCLE facility within
    800 m of Metro Areena.  The ids must be integers and usually differ.
    """
    try:
        ids = await nearest_parking_ids(*AREENA, radius_m=800)
    except httpx.RequestError:
        pytest.skip("Fintraffic Parking API offline")

    assert "CAR" in ids and isinstance(ids["CAR"], int)
    assert "BICYCLE" in ids and isinstance(ids["BICYCLE"], int)
    assert ids["CAR"] != ids["BICYCLE"]


@pytest.mark.asyncio
async def test_live_parking_status():
    """
    Live vacancy numbers must be within the logical range 0 ≤ free ≤ capacity.
    """
    try:
        car_id = (await nearest_parking_ids(*AREENA))["CAR"]
        data   = await parking_status(car_id)
    except httpx.RequestError:
        pytest.skip("Fintraffic Parking API offline")

    assert 0 <= data["spacesAvailable"] <= data["capacity"]
    assert data["timestamp_utc"].endswith("Z") or "T" in data["timestamp_utc"]


@pytest.mark.asyncio
async def test_prediction_optional():
    """
    If Fintraffic has ML predictions, they must be well-formed.  If not yet
    available for this facility the test is skipped.
    """
    try:
        car_id = (await nearest_parking_ids(*AREENA))["CAR"]
        rows   = await facility_prediction(car_id, hours=6)
    except httpx.RequestError:
        pytest.skip("Fintraffic Parking API offline")

    if not rows:                       # some sites don't have predictions yet
        pytest.skip("No prediction data for this facility")

    first = rows[0]
    assert "timestamp" in first and "spacesAvailable" in first
    assert isinstance(first["spacesAvailable"], int)

