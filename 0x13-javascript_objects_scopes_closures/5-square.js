#!/usr/bin/node
//a class Square that defines a square

module.exports = class Square extends require ('./4-rectangle.js'){
	constructor (size){
		super(size, size);
	}
};
