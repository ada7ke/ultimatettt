from loguru import logger
import streamlit as st
import ultimate

def main():
    st.set_page_config(page_title="Ultimate Tic Tac Toe", layout="wide", initial_sidebar_state="collapsed")
    if "board" in st.session_state:
        board: ultimate.Board = st.session_state["board"]
    else:
        board = ultimate.Board()
        st.session_state["board"] = board

    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]

    st.header("Ultimate Tic Tac Toe - Made by Ada Ke")
    boardMarkdown = f"```\nPlayer {board.current_player} turn in board #{board.previous_square}\n{board.printBoard()}\n```"
    st.write(boardMarkdown)

    score = board.scoring()
    print(f"Score: '{score}'")
    if score != ultimate.Marker.EMPTY and score != " ":
        st.write(f"\nPlayer '{score}' wins!")

    prompt_box = st.empty()

    with prompt_box:
        playerInput = st.text_input("Please choose a square (0-8): ", key=f"move{board.move_num}")
    
    instructionCol, buttonCol = st.columns([4,1])

    with instructionCol:
        with st.expander("Instructions"):
            st.write("Welcome to Ultimate Tic Tac Toe made by Ada Ke. The rules are as follows: \n- Just like regular Tic Tac Toe, you enter which square you wish to place your marker in.  \n- On the first turn, the player can only place in the middle board. Then, which ever small square that the player placed in is then reflected on the big board for the next player. For example, if the first player types '0', then the next player must play in the first board on the big board.\n- If a board is already full, the player may choose the board that they wish to play in, then will type in the square that they choose. \n- The winner is who ever wins three small boards in a row, column, or diagonal line.")
    
    with buttonCol:
        st.button("\nRestart\n", on_click=board.reset)

    if len(playerInput) > 0:
        logger.info(f"Player input: '{playerInput}'")
        if playerInput not in numbers:
            st.write("Invalid input. Please try again.")
            logger.info(f"Invalid input: '{playerInput}'")
        else:
            result = board.move(int(playerInput))
            if result == ultimate.MoveState.INVALID:
                st.write("Invalid input. Please try again.")
                logger.info(f"Invalid input: '{playerInput}'")
            
        st.session_state.board = board

        st.write("\n")
        st.experimental_rerun()
    else:
        logger.info("Waiting for input...")


if __name__ == "__main__":
    main()


