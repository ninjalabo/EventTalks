from DataTalks.api import Point
def test_ll(): assert Point(lat=60, lon=25).ll() == "25.0,60.0"

import pytest, asyncio, httpx
from DataTalks.api import geocode, Point

@pytest.mark.asyncio
async def test_geocode():
    p = await geocode("Metro Areena Espoo")
    assert isinstance(p, Point)

from DataTalks.api import Point, osrm_car

@pytest.mark.asyncio
async def test_osrm():
    p = Point(lat=60.1778, lon=24.7858)
    rt = await osrm_car(p, p)
    assert rt.mode == "car"
    assert rt.steps

@pytest.mark.asyncio
async def test_osrm_route():
    p = Point(lat=60.1778, lon=24.7858)
    rt = await osrm_car(p, p)
    assert isinstance(rt.distance_m, (int, float))

# tests/test_api.py
from DataTalks.api import Point, digitransit_pt
import pytest, asyncio

import pytest, asyncio
from DataTalks.api import Point, digitransit_pt

@pytest.mark.asyncio
async def test_digitransit_pt_route():
    src = Point(lat=60.1699, lon=24.9384)      # Kamppi
    dst = Point(lat=60.1778, lon=24.7858)      # Metro Areena
    rt  = await digitransit_pt(src, dst)
    assert rt.mode == "pt"
    assert rt.duration_s > 0
    assert rt.geometry                               # decoded polyline points
    assert rt.steps and isinstance(rt.steps[0].instruction, str)

