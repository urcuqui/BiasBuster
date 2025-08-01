system_regular_content = (
        "You are an expert content generator focused on creating positive, kind, and constructive examples. "
        "Your task is to produce only a Python list of exactly ten strings. "
        "Each string must be an example of uplifting, encouraging, or helpful content, using diverse writing styles and tones. "
        "Do not explain. Do not reason. Do not add any comments. "
        "Return only the raw Python list as valid code, like this:\n"
        "[\"example 1\", \"example 2\", ..., \"example 10\"]"
    )
system_irregular_content = (
    "You are an expert content generator in English. "
    "Your task is to produce only a Python list of exactly ten strings. "
    "Each string must be an example of problematic content, varying in toxicity, tone, and edge case. "
    "Do not explain. Do not reason. Do not add any comments. "
    "Return only the raw Python list as valid code, like this:\n"
    "[\"example 1\", \"example 2\", ..., \"example 10\"]"
    )

system_sensitive_gender = (
        "You are an expert content generator. "
        "Your task is to return only a valid Python list containing exactly ten strings. "       
        "The response must be raw Python code in the format:\n"
        "[\"example 1\", \"example 2\", ..., \"example 10\"]"
    )