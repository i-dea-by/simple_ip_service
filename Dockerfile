FROM python:3.13-slim-bookworm

EXPOSE 8000

ENV USER=user PYTHONUNBUFFERED=1 UV_COMPILE_BYTECODE=1

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

RUN useradd --create-home $USER

WORKDIR /home/$USER/app

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-dev --no-cache

COPY src .

RUN chown -R $USER:$USER /home/$USER/app

USER $USER

CMD ["uv", "run", "main.py"]
