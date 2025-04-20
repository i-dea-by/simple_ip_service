"""
Deploy with uvicorn --proxy-headers
"""

from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import FileResponse, HTMLResponse, PlainTextResponse, Response
from starlette.routing import Route

import templates
from config import BASE_URL, STATIC_DIR
from errors import exception_handlers


def extract_ip(request: Request):
    """Extract real IP from request"""
    ip = request.headers.get("x-forwarded-for")
    if ip is not None:
        return ip.split(", ")[0]
    return request.client.host


async def homepage(request: Request):
    """Home page answer"""
    ip = extract_ip(request)
    return HTMLResponse(content=templates.mainpage_html.substitute(ip=ip, base_url=BASE_URL))


async def ip(request: Request):
    """Returns the IPv4 address of the client as plain text XX.XX.XX.XX"""
    ip = extract_ip(request)
    return PlainTextResponse(content=ip)


async def json(request: Request):
    """Return the IPv4 address of the client as JSON {"ip": XX.XX.XX.XX}"""
    ip = extract_ip(request)
    answer = f'{{"ip": "{ip}"}}'
    return Response(content=answer, media_type="application/json")


async def robots(request: Request):
    """Return robots.txt"""
    return PlainTextResponse(content=templates.robots_txt)


async def sitemap(request: Request):
    """Return sitemap.xml"""
    return Response(content=templates.sitemap_xml, media_type="application/xml")


async def favicon(request: Request):
    """Return favicon.ico"""
    return FileResponse(STATIC_DIR / "favicon.ico")


routes = [
    Route("/", endpoint=homepage, methods=["GET", "HEAD"]),
    Route("/ip", endpoint=ip),
    Route("/json", endpoint=json),
    Route("/favicon.ico", endpoint=favicon),
    Route("/robots.txt", endpoint=robots),
    Route("/sitemap.xml", endpoint=sitemap),
]


app = Starlette(routes=routes, exception_handlers=exception_handlers)
