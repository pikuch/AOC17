
def run_day(n):
    module_name = f"Day{n:02d}"
    try:
        module = __import__(module_name)
        module.run()
    except ModuleNotFoundError:
        print(f"Can't find {module_name}")
        exit(404)


if __name__ == '__main__':
    run_day(1)
