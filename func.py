from typing import Any

def report(data: Any, attributes: dict):
    # Your function implementation goes here
    print("**GOT EVENT**")
    print(attributes)
    # print(data)
    attributes["type"] = "dev.processed-namespace"
    return (attributes, data)
