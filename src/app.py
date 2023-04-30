from loguru import logger
import streamlit as st
import ultimate

def main():
    st.set_page_config(page_title="Ultimate Tic Tac FEET", layout="wide", initial_sidebar_state="collapsed")
    board = ultimate.Board()
    playing = True
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
    keyCounter = 0

    while playing == True:
        st.write(f"Player {board.current_player} turn")
        boardMarkdown = f"```\nUltimate Tic Tac FEET\n{board.printBoard()}\n```"
        st.write(boardMarkdown)
        playerInput = st.text_input("Please choose a square: ", key=f"move{keyCounter}")
        keyCounter += 1  
        if len(playerInput) > 0:
            while playerInput not in numbers or board.isOccupied(int(playerInput)):
                playerInput = st.text_input("Please choose a square: ", key=f"move{keyCounter}")
                keyCounter += 1
            playerInput = int(playerInput)
            board.move(playerInput)
            st.write("\n")
            
            score = board.scoring()
            if score != ultimate.Marker.EMPTY:
                st.write(f"Player {score} wins!")
                return
            

if __name__ == "__main__":
    main()


