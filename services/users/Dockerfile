# Cargo Build Stage
FROM rust:1.36-slim as cargo-build

WORKDIR /usr/src/app

COPY Cargo.toml Cargo.toml

RUN mkdir src/
RUN echo "fn main() {println!(\"if you see this, the build broke\")}" > src/main.rs
RUN cargo build --release
RUN cargo rm -f target/release/deps/app*

COPY . .
RUN cargo build --release
RUN cargo install --path .


# Final Stage
FROM alpine:latest

COPY --from=cargo-build /usr/local/cargo/bin/app /usr/local/bin/app

CMD ["app"]
