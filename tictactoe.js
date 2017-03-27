var tictactoe = {
	EMPTY: "E",
	X: "X",
	O: "O",

	SIZE: 3,

	O_TURN: 0,
	X_TURN: 1,

	get_piece: function(turn) {
		return (turn === tictactoe.O_TURN ?  tictactoe.O : tictactoe.X);
	}
}

var State = function(prev_state) {

	this.turn = tictactoe.X_TURN;
	this.board = [[],[],[]];

	if (prev_state != undefined) {
		this.turn ^= prev_state.turn;

		//assign the board	
		for (var i = 0; i < tictactoe.SIZE; i++) {
			for (var j = 0; j < tictactoe.SIZE; j++) {
				this.board[i][j] = prev_state.board[i][j];
			}
		}
	}

	this.isGameOver = function() {
		return (this.isRowOver() || this.isColOver() || this.isDiagOver());
	}

	/* Horizontal game over */
	this.isRowOver = function() {
		for (var i = 0; i < tictactoe.SIZE; i++) {
			if (this.board[i][0] != tictactoe.EMPTY && this.board[i][0] === this.board[i][1] && this.board[i][1] == this.board[i][2]) {
				return true;
			}
		}
		return false;
	}

	/* Vertical game over */
	this.isColOver = function() {
		for (var i = 0; i < tictactoe.SIZE; i++) {
			if (this.board[0][i] != tictactoe.EMPTY && this.board[0][i] === this.board[1][i] && this.board[1][i] === this.board[2][i]) {
				return true;
			}
		}
		return false;
	}
	
	/* Diagonal game over */
	this.isDiagOver = function() {
		if (this.board[0][0] != tictactoe.EMPTY && this.board[0][0] === this.board[1][1] && this.board[1][1] === this.board[2][2]) {
			return true;
		}

		if (this.board[0][0] != tictactoe.EMPTY && this.board[0][2] === this.board[1][1] && this.board[1][1] === this.board[2][0]) {
			return true;
		}
		return false;
	}
}



var game = {

	state: undefined,

	init: function() {
		var state = new State();
		state.turn = tictactoe.X_TURN;	

		//initialise the board with empty
		for (var i = 0; i < tictactoe.SIZE; i++) {
			for (var j = 0; j < tictactoe.SIZE; j++) {
				state.board[i][j] = tictactoe.EMPTY;
			}
		}
		
		game.state = state;
	},

	make_move: function(row, col) {
		var state = game.state;

		if (state.board[row][col] === tictactoe.EMPTY) {
			state.board[row][col] = tictactoe.get_piece(state.turn);
			state.turn ^= state.turn;
		}
	},


	play: function() {
		game.init();

	}

}
