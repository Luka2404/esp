from usb_sentinel.webapp import create_app


def main() -> None:
    app = create_app()
    print("USB Sentinel dashboard: http://127.0.0.1:5050")
    app.run(host="127.0.0.1", port=5050, debug=False, use_reloader=False)


if __name__ == "__main__":
    main()
