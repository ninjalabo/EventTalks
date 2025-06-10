########################
# 1️⃣  Build stage
########################
FROM python:3.11-slim AS builder

ENV PYTHONUNBUFFERED=1
WORKDIR /app

# system deps only needed while building wheels
RUN apt-get update \
 && apt-get install -y --no-install-recommends build-essential \
 && rm -rf /var/lib/apt/lists/*

# ── Python deps ───────────────────────────────────────────────────────────
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
 && if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt ; fi

RUN pip install --upgrade openai

#RUN pip install --no-cache-dir \
#    "git+https://github.com/openai/openai-agents-python.git@main#egg=openai-agents" \
#    "git+https://github.com/lastmile-ai/openai-agents-mcp.git@main#egg=openai-agents-mcp"


# ── project source ────────────────────────────────────────────────────────
COPY . .

# export notebooks → datatalks/*.py  (nbdev)
RUN nbdev_export

# install the repo in editable mode
RUN pip install --no-cache-dir -e .

###########################################################################
# 2️⃣  Runtime stage  (copy venv from builder → no gcc, much smaller)
###########################################################################
FROM python:3.11-slim

RUN apt-get update \
 && apt-get install -y --no-install-recommends curl \
 && rm -rf /var/lib/apt/lists/*

# copy the “built” site-packages from the builder
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /app /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app

WORKDIR /app
EXPOSE 8000 9001

CMD ["bash"]

