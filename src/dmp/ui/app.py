"""Local Streamlit entrypoint for DMP."""


def main() -> None:
    """Render the initial local application shell."""
    import streamlit as st

    st.set_page_config(page_title="DMP")
    st.title("DMP")
    st.info("A interface será implementada nas próximas etapas.")


if __name__ == "__main__":
    main()
