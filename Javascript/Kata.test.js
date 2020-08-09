const Kata = require('./Kata');

test('HelloWorld!', () => {
    expect(Kata.HelloWorld()).toBe('HelloWorld');
});

test('adds 1 + 2 to equal 3', () => {
    expect(Kata.sum(1, 2)).toBe(3);
});

test('Generate 8x8 shape', () => {
	expect(Kata.GenerateShape(8)).toBe('++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++');
});
