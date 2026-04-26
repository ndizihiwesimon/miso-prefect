from prefect import flow, task


@task
def hello():
    """Print hello message"""
    print("Hello, World!")


@flow
def main():
    """Main function"""
    print("Here is the hello message:")
    hello()

if __name__ == "__main__":
    main()