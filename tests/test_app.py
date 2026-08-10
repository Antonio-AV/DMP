from pathlib import Path

from streamlit.testing.v1 import AppTest

ENTRYPOINT = Path(__file__).parents[1] / "src" / "dmp" / "ui" / "app.py"


def test_streamlit_entrypoint_initializes() -> None:
    app = AppTest.from_file(str(ENTRYPOINT)).run()

    assert app.title[0].value == "DMP"
