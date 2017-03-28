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

	/* 3x3 board as a 2D array */
	this.board = [[],[],[]];
	
	/* Initialise the board with empty */
	for (var i = 0; i < tictactoe.SIZE; i++) {
		for (var j = 0; j < tictactoe.SIZE; j++) {
			this.board[i][j] = tictactoe.EMPTY;
		}
	}

	this.isGameOver = function() {
		return (this.isRowOver() || this.isColOver() || this.isDiagOver());
	}

	this.isBoardFull = function() {
		for (var i = 0, var j = 0; i < tictactoe.SIZE; i++, j++) {
			if (this.board[i][j] === tictactoe.EMPTY) {
				return false;
			}
		}
		return true;
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

		if (this.board[0][2] != tictactoe.EMPTY && this.board[0][2] === this.board[1][1] && this.board[1][1] === this.board[2][0]) {
			return true;
		}
		return false;
	}

	this.draw = function(ctx, width, height) {
		ui.drawGrid(ctx, width, height);

		for (var i = 0; i < tictactoe.SIZE; i++) {
			for (var j = 0; j < tictactoe.SIZE; j++) {
				var piece = this.board[i][j];
				var x = (1 + i*2)*width/6;
				var y = (1 + j*2)*height/6;
				if (piece === tictactoe.X) {
					ui.drawX(ctx, x, y);
				}
				else if (piece === tictactoe.O) {
					ui.drawO(ctx, x, y);
				}	
			}
		}
	}
}



var game = {

	state: undefined,

	init: function() {
		game.state = new State();

		/* Set up HTML canvas with mouseclick event */
		var canvas = document.getElementById("canvas");
		canvas.addEventListener("mousedown", function(event) {
			var x = event.x - canvas.offsetLeft;
			var y = event.y - canvas.offsetTop;
			
			x = Math.floor(x/(canvas.width/3));
			y = Math.floor(y/(canvas.height/3));

			game.make_move(x, y);
	
		}, false);
	},

	make_move: function(row, col) {
		var state = game.state;

		if (state.board[row][col] === tictactoe.EMPTY) {
			state.board[row][col] = tictactoe.get_piece(state.turn);
			game.draw();

			/* Game over check */
			if (game.state.isGameOver()) {
				alert(game.state.turn + " wins!");
				game.play();
				return;
			}
			else if (game.state.isBoardFull()) {
				alert("It's a draw!");
				game.play();
				return();
			}
			state.turn ^= 1;
		}
	},

	draw: function() {
		var canvas = document.getElementById("canvas");
		var ctx = canvas.getContext("2d");

		ctx.clearRect(0,0,canvas.width, canvas.height);
		game.state.draw(ctx, canvas.width, canvas.height);
	},

	play: function() {
		game.init();
		game.draw();
	}

}
