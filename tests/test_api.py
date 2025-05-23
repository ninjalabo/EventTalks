from DataTalks.api_clients import Point
from DataTalks.api_clients import geocode
from DataTalks.api_clients import digitransit_pt
import pytest
import httpx
from DataTalks.api_clients import osrm_car


def test_ll(): assert Point(lat=60, lon=25).ll() == "25.0,60.0"


@pytest.mark.asyncio
async def test_geocode():
    try:
        p = await geocode("Metro Areena Espoo")
    except httpx.RequestError:
        pytest.skip("Nominatim API offline")
    assert isinstance(p, Point)


@pytest.mark.asyncio
async def test_osrm():
    p = Point(lat=60.1778, lon=24.7858)
    try:
        rt = await osrm_car(p, p)
    except httpx.RequestError:
        pytest.skip("OSRM server offline")
    assert rt.mode == "car"
    assert rt.steps

@pytest.mark.asyncio
async def test_osrm_route():
    p = Point(lat=60.1778, lon=24.7858)
    try:
        rt = await osrm_car(p, p)
    except httpx.RequestError:
        pytest.skip("OSRM server offline")
    assert isinstance(rt.distance_m, (int, float))

@pytest.mark.asyncio
async def test_digitransit_pt_route():
    src = Point(lat=60.1699, lon=24.9384)      # Kamppi
    dst = Point(lat=60.1778, lon=24.7858)      # Metro Areena
    try:
        rt = await digitransit_pt(src, dst)
    except httpx.RequestError:
        pytest.skip("Digitransit API offline")
    assert rt.mode == "pt"
    assert rt.duration_s > 0
    assert rt.geometry                               # decoded polyline points
    assert rt.steps and isinstance(rt.steps[0].instruction, str)

