const Kata = require('./Kata');

test('HelloWorld!', () => {
    expect(Kata.HelloWorld()).toBe('HelloWorld');
});

test('adds 1 + 2 to equal 3', () => {
    expect(Kata.sum(1, 2)).toBe(3);
});
