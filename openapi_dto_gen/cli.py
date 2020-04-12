import click

@click.command()
@click.argument('openapi_file', envvar='OPENAPI_FILE', type=click.File('rb'))
def main(openapi_file):
    """Simple program to generate DTO Python Classes based on OpenAPI v3 Schema"""
    
    pass

if __name__ == "__main__":
    main()