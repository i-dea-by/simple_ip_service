from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import HTMLResponse

import templates


async def not_found_error(request: Request, exc: HTTPException):
    return HTMLResponse(templates.error_404_html, status_code=exc.status_code)


async def internal_error(request: Request, exc: HTTPException):
    return HTMLResponse(templates.error_500_html, status_code=exc.status_code)


exception_handlers = {
    404: not_found_error,
    500: internal_error
}
