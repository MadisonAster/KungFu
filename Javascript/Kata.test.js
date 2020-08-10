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

test('SnakeInTheSquare', () => {
    expect(Kata.SnakeInTheSquare(5)).toEqual([[1, 0, 0], [1, 0, 0], [1, 1, 1]]);
    expect(Kata.SnakeInTheSquare(8)).toEqual([[1, 0, 0, 0], [1, 0, 1, 0], [1, 0, 1, 0], [1, 1, 1, 0]]);
    expect(Kata.SnakeInTheSquare(31)).toEqual([[1, 0, 1, 1, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1], [1, 1, 1, 0, 1, 1, 1]]);
});

test('anagrams', () => {
    expect(Kata.anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])).toEqual(['aabb', 'bbaa']);
    expect(Kata.anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])).toEqual(['carer', 'racer']);
    expect(Kata.anagrams('laser', ['lazing', 'lazy',  'lacer'])).toEqual([]);
});

