from prefect import flow, get_run_logger, task


DEFAULT_NAME = "World"


def build_greeting(name: str = DEFAULT_NAME) -> str:
    """Build the greeting message used by the Prefect task."""
    cleaned_name = name.strip() or DEFAULT_NAME
    return f"Hello, {cleaned_name}!"


@task
def hello(name: str = DEFAULT_NAME) -> str:
    """Return a greeting message."""
    return build_greeting(name)


@flow(log_prints=True)
def main(name: str = DEFAULT_NAME) -> str:
    """Run the greeting workflow."""
    logger = get_run_logger()
    logger.info("Preparing hello message.")
    message = hello(name)
    logger.info(message)
    return message


if __name__ == "__main__":
    main()
