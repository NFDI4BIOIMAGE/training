#!/usr/bin/env python3
import argparse
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Serve this directory over HTTP.")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()

    site_dir = Path(__file__).parent
    handler = lambda *handler_args, **kwargs: SimpleHTTPRequestHandler(
        *handler_args, directory=site_dir, **kwargs
    )

    server = ThreadingHTTPServer((args.host, args.port), handler)
    print(f"Serving {site_dir} at http://{args.host}:{args.port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
