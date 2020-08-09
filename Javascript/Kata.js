class Kata{
	HelloWorld(){
		return "HelloWorld";
	}
	
	sum(a, b) {
	  return a + b;
	}

	GenerateShape(int){
  		return new Array(int).fill('+'.repeat(int)).join('\n');
	}
}
module.exports = new Kata;
