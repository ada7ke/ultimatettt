from loguru import logger
import streamlit as st
import ultimate
import random

# streamlit run src/app.py

def main():
    st.set_page_config(page_title="Ultimate Tic Tac Toe", layout="wide", initial_sidebar_state="collapsed")
    if "board" in st.session_state:
        board = st.session_state["board"]
    else:
        board = ultimate.Board()
        st.session_state["board"] = board

    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]

    st.write(f"Player {board.current_player} turn in board #{board.previous_square}")
    boardMarkdown = f"```\nUltimate Tic Tac Toe\n{board.printBoard()}\n```"
    st.write(boardMarkdown)
    prompt_box = st.empty()

    with prompt_box:
        playerInput = st.text_input("Please choose a square: ", key=f"move{board.move_num}")
    
    st.write("\n")
    st.button("Restart", on_click=board.reset)
    
    if len(playerInput) > 0:
        logger.info(f"Player input: '{playerInput}'")
        if playerInput not in numbers or board.isOccupied(int(playerInput)):
            st.write("Invalid input. Please try again.")
            logger.info(f"Invalid input: '{playerInput}'")
            return
        playerInput = int(playerInput)
        board.move(playerInput)
        st.session_state.board = board

        st.write("\n")
        

        score = board.scoring()
        print(f"Score: '{score}'")
        if score != ultimate.Marker.EMPTY and score != " ":
            st.write(f"Player {score} wins!")
            return
        
        st.write(ultimate.Board())
        st.experimental_rerun()
    else:
        logger.info("Waiting for input...")

              

if __name__ == "__main__":
    main()


