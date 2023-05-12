from loguru import logger
import streamlit as st
import ultimate

# streamlit run src/app.py

def main():
    st.set_page_config(page_title="Ultimate Tic Tac Toe", layout="wide", initial_sidebar_state="collapsed")
    if "board" in st.session_state:
        board = st.session_state["board"]
    else:
        board = ultimate.Board()
        st.session_state["board"] = board

    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]

    st.write(f"Player {board.current_player} turn")
    boardMarkdown = f"```\nUltimate Tic Tac Toe\n{board.printBoard()}\n```"
    st.write(boardMarkdown)
    playerInput = st.text_input("Please choose a square: ", key=f"move")
    if len(playerInput) > 0:
        if playerInput not in numbers or board.isOccupied(int(playerInput)):
            st.write("Invalid input. Please try again.")
            return
        playerInput = int(playerInput)
        board.move(playerInput)
        st.session_state.board = board

        st.write("\n")
        

        # score = board.scoring()
        # print(f"Score: '{score}'")
        # if score != ultimate.Marker.EMPTY and score != " ":
        #     st.write(f"Player {score} wins!")
        #     return
        
    st.experimental_rerun()
        
    st.write(ultimate.Board())
              

if __name__ == "__main__":
    main()


