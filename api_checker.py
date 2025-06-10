from fastmcp import FastMCP
import json, asyncio, httpx, yaml
from openapi_spec_validator import validate_spec, validate

CAT = json.load(open("apis.json"))

async def load(api, client):
    r = await client.get(api["spec_url"]); r.raise_for_status()
    spec = yaml.safe_load(r.text) if api["spec_url"].endswith((".yml",".yaml")) else r.json()
    validate(spec)
    srv = FastMCP.from_openapi(openapi_spec=spec, name=api["id"], client=client)
    tools = await srv.get_tools()
    print(f"✓ {api['id']} mounted with {len(tools)} tools")

async def main():
    async with httpx.AsyncClient() as cx:
        await asyncio.gather(*(load(a, cx) for a in CAT))

asyncio.run(main())

