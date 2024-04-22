from fake_headers import Headers



def create_real_headers(access: str, user_agent: str) -> dict|None:
    """
    :param access: string containing the real access
    :param user_agent: string containing the real user agent
    :return: dict|None containing the real headers or None if "" value(s)
    """
    if access and user_agent:
        real_headers = {"access": access, "user-agent": user_agent}
        return real_headers
    return None


def create_fake_headers() -> dict:
    """
    Create a fake headers using fake_headers library
    :return: dict
    """
    fake_headers = Headers().generate()
    return fake_headers
