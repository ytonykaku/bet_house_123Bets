import os


def create_operations_dict(operations: list[str], SQL_BASE_PATH: str) -> dict[str, str]:
    queries = dict()

    for op_name in operations:
        with open(os.path.join(SQL_BASE_PATH, f"{op_name}.sql")) as f:
            queries[op_name] = f.read()

    return queries

