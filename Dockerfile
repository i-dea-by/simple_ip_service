FROM python:3.13-slim-bookworm

EXPOSE 8000

ENV USER=user PYTHONUNBUFFERED=1 UV_COMPILE_BYTECODE=1

COPY --from=ghcr.io/astral-sh/uv:0.7.8 /uv /uvx /bin/

RUN useradd --create-home $USER

USER $USER

WORKDIR /home/$USER/app

COPY --chown=$USER pyproject.toml uv.lock ./

RUN uv sync --frozen --no-dev --no-cache

COPY --chown=$USER src .

CMD ["uv", "run",  "--frozen", "main.py"]
