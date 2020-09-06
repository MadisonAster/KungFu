const Kata = require('./Kata');

test('test_HelloWorld', () => {
    expect(Kata.HelloWorld()).toBe('HelloWorld');
});

test('test_adds', () => {
    expect(Kata.sum(1, 2)).toBe(3);
});

test('test_Generate8x8shape', () => {
    expect(Kata.GenerateShape(8)).toBe('++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++');
});

test('test_SnakeInTheSquare', () => {
    expect(Kata.SnakeInTheSquare(5)).toEqual([[1, 0, 0], [1, 0, 0], [1, 1, 1]]);
    expect(Kata.SnakeInTheSquare(8)).toEqual([[1, 0, 0, 0], [1, 0, 1, 0], [1, 0, 1, 0], [1, 1, 1, 0]]);
    expect(Kata.SnakeInTheSquare(31)).toEqual([[1, 0, 1, 1, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1], [1, 1, 1, 0, 1, 1, 1]]);
    //expect(Kata.SnakeInTheSquare(32)).toEqual([[1, 0, 1, 1, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1], [1, 1, 1, 0, 1, 1, 1]]);
});

test('test_anagrams', () => {
    expect(Kata.anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])).toEqual(['aabb', 'bbaa']);
    expect(Kata.anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])).toEqual(['carer', 'racer']);
    expect(Kata.anagrams('laser', ['lazing', 'lazy',  'lacer'])).toEqual([]);
});

test('test_getStarStrings', () => {
    expect(Kata.getStarStrings('Chicago')).toEqual('c:**,h:*,i:*,a:*,g:*,o:*');
    expect(Kata.getStarStrings('Bangkok')).toEqual('b:*,a:*,n:*,g:*,k:**,o:*');
    expect(Kata.getStarStrings('Las Vegas')).toEqual('l:*,a:**,s:**,v:*,e:*,g:*');
    expect(Kata.getStarStrings('New York City')).toEqual('n:*,e:*,w:*,y:**,o:*,r:*,k:*,c:*,i:*,t:*');
});


test('test_DrivingSchool', () => {
    expect(Kata.DrivingSchool(45)).toEqual(30);
    expect(Kata.DrivingSchool(63)).toEqual(30);
    expect(Kata.DrivingSchool(84)).toEqual(40);
    expect(Kata.DrivingSchool(95)).toEqual(40);
    expect(Kata.DrivingSchool(102)).toEqual(50);
    expect(Kata.DrivingSchool(273)).toEqual(100);
});