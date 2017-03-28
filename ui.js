var ui = {

	drawGrid: function(ctx, width, height) {
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
	},

	drawX: function(ctx, x, y) {
		var size = 30;	
		ctx.beginPath();

		ctx.moveTo(x - size, y - size);
		ctx.lineTo(x + size, y + size);

		ctx.moveTo(x + size, y - size);
		ctx.lineTo(x - size, y + size);

		ctx.stroke();
	},

	drawO: function(ctx, x, y) {
		var size = 30;
		ctx.beginPath();
		ctx.arc(x, y, size, 0, 2*Math.PI);
		ctx.stroke();
	}

};
