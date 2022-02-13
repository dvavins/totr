import uuid


def ref_code_generator():
    code = str(uuid.uuid4()).replace('-', '')[:20]
    return code
