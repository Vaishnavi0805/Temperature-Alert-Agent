from uagents import Model


class TEMPRequest(Model):
    """
    Represents an Temperature Request.

    Attributes:
        location (float): The location where temperature is requested.
    """
    location: str
    min_threshold_temperature: float
    max_threshold_temperature: float
