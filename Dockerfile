ARG PYTHON_VERSION=3.12-slim


FROM python:${PYTHON_VERSION} AS build

# RUN apt-get update && \
#     apt-get install -y --no-install-recommends build-essential && \
#     rm -rf /var/cache/apt

RUN python -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
COPY requirements.dev.txt .
COPY pip.conf /etc/pip.conf

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -r requirements.dev.txt

FROM python:${PYTHON_VERSION} AS app

COPY --from=build /opt/venv /opt/venv
COPY --from=build /etc/pip.conf /etc/pip.conf

ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /opt/app

COPY . .

RUN pip install -e .