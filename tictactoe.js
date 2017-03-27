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

	this.draw = function(ctx, width, height) {
		this.drawGrid(ctx, width, height);

		for (var i = 0; i < tictactoe.SIZE; i++) {
			for (var j = 0; j < tictactoe.SIZE; j++) {
				var piece = this.board[i][j];
				var x = (1 + i*2)*width/6;
				var y = (1 + j*2)*height/6;
				if (piece === tictactoe.X) {
					this.drawX(ctx, x, y);
				}
				else if (piece === tictactoe.O) {
					this.drawO(ctx, x, y);
				}
			}
		}
	}

	this.drawGrid = function(ctx, width, height) {
		ctx.beginPath();	
		
		/* Draw horizontal lines */
		ctx.moveTo(0, height/3);
		ctx.lineTo(width, height/3);
		ctx.moveTo(0, 2*height/3);
		ctx.lineTo(width, 2*height/3);

		/* Draw vertical lines */
		ctx.moveTo(width/3, 0)
		ctx.lineTo(width/3, height)
		ctx.moveTo(2*width/3, 0)
		ctx.lineTo(2*width/3, height)

		ctx.stroke();
	}

	this.drawX = function(ctx, x, y) {
		var size = 30;	
		ctx.beginPath();

		ctx.moveTo(x - size, y - size);
		ctx.lineTo(x + size, y + size);

		ctx.moveTo(x + size, y - size);
		ctx.lineTo(x - size, y + size);

		ctx.stroke();
	}

	this.drawO = function(ctx, x, y) {
		var size = 30;
		ctx.beginPath();
		ctx.arc(x, y, size, 0, 2*Math.PI);
		ctx.stroke();
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
			state.turn ^= 1;
		}

		game.draw();
	},

	
	draw: function() {
		var canvas = document.getElementById("canvas");
		var ctx = canvas.getContext("2d");
		game.state.draw(ctx, canvas.width, canvas.height);
	},

	play: function() {
		game.init();
		game.draw();
	}

}
