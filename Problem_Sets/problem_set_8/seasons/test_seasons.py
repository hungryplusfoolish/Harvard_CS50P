import pytest
from seasons import date_delta


def test_invalid():
    with pytest.raises(ValueError):
         date_delta("cat")
    with pytest.raises(ValueError):
         date_delta("100-1000-500")
    with pytest.raises(ValueError):
         date_delta("-100-100-000")




    