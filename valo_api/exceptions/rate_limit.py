import math
import time


class RateLimit:
    limit: int = -1
    """The number of requests you did in the current period."""
    remaining: int = -1
    """The number of requests you can make in the current period."""
    reset_unix: int = -1
    """The Unix timestamp of when the current period will reset."""

    @property
    def reset(self) -> int:
        """The time until the current period ends."""
        return max(0, self.reset_unix - math.floor(time.time()))

    def __str__(self) -> str:
        return f"Limit: {self.limit}, Remaining: {self.remaining}, Reset: {self.reset}"


def rate_limit() -> RateLimit:
    """Returns the current rate limit for the API.

    Returns:
        RateLimit: A :class:`.RateLimit` object.
    """
    return RateLimit()