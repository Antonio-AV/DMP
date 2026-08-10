from pathlib import Path

from streamlit.testing.v1 import AppTest

from dmp.ui.app import main

ENTRYPOINT = Path(__file__).parents[1] / "src" / "dmp" / "ui" / "app.py"


def test_streamlit_entrypoint_initializes() -> None:
    assert callable(main)

    app = AppTest.from_file(str(ENTRYPOINT)).run()

    assert app.title[0].value == "DMP"
