FROM pypy:3
WORKDIR /app
COPY . .
RUN apt-get update

RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1
ENV PATH="/root/.cargo/bin:${PATH}"
RUN rustc --version
RUN pip install -U pip
RUN pip install -r requirements.txt

ENTRYPOINT ["pypy3", "-m","uvicorn", "main:app" , "--reload", "--host=0.0.0.0", "--port=3000", "--log-level=debug", "--workers=3"]