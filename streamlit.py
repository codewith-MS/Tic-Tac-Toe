import streamlit as st

#Page Title
st.set_page_config(page_title= "RL Tic Tae Toe" , layout ="centered")
st.title("Tic-Tac-Toe")
st.write("Let's play against a Random AI Player !!!")

#Board session 
if "board" not in st.session_state:
    st.session_state.board =[""] *9
    st.session_state.turn = "X"
    st.session_state.game_over = False
    st.session_state.winner = None

board = st.session_state.board

#to check the winner
def check_winner():
    win_patterns = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for pattern in win_patterns:
        if board[pattern[0]] == board[pattern[1]] == board[pattern[2]] != "":
            return board[pattern[0]]
    return None

#button click logic
def make_move(i):
    if board[i] == "" and not st.session_state.game_over:
        board[i] = st.session_state.turn
        winner = check_winner()

        if winner:
            st.session_state.game_over = True
            st.session_state.winner = winner
        elif "" not in board:
            st.session_state.game_over  = True
            st.session_state.winner = "Draw"
        else:
            st.session_state.turn = "O" if st.session_state.turn == "X" else "X"

#Draw board

for row in range(3):
    cols = st.columns([2,1,1,1,2])  # side padding columns)
    for col in range(3):
        index = row*3 +col 
        cols[col+1].button(
            board[index] if board[index] != "" else " ",
            key=index,
            on_click = make_move,
            args=(index,)
        )

    st.markdown("<br>", unsafe_allow_html=True)


#show result
if st.session_state.game_over:
    if st.session_state.winner == "Draw":
        st.success("It's a Draw!")
    else:
        st.success(f" Winner: {st.session_state.winner}")


# Reset button
if st.button("Restart Game"):
    st.session_state.board = [""] * 9
    st.session_state.turn = "X"
    st.session_state.game_over = False

