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

    SnakeInTheSquare(size) {
        //calculate grid size
        var gsize = 0;
        while (true){
            gsize += 1;
            var max = Math.ceil(gsize/2)*gsize + Math.floor(gsize/2);
            if (max >= size) break;
        };
        
        //construct empty grid
        var result = new Array();
        for (var y = 1; y <= gsize; ++y){
            result.push(new Array(gsize).fill(0));
        };
        
        //fill result
        var count = 0;
        for (var y = 0; y < gsize; ++y){
            if ((y+1) % 4 == 1) { //column 1
                for (var x = 0; x < gsize; ++x){ //top to bottom
                    if (count == size) break;
                    result[x][y] = 1;
                    count += 1;
                };
            } else if ((y+1) % 4 == 2) { //column 2
                result[gsize-1][y] = 1; //bottom only
                count += 1;
            } else if ((y+1) % 4 == 3) { //column 3
                for (var x = gsize-1; x >= 0; --x){ //bottom to top
                    if (count == size) break;
                    result[x][y] = 1;
                    count += 1;
                };
            } else if ((y+1) % 4 == 0) { //column 4
                result[0][y] = 1; //top only
                count += 1;
            };
            if (count == size) break;
        };
        
        return result;
    }

    anagrams(word, words) {
        var result = [];
        var letterlist = word.split('');
        letterlist.sort();
        for (var i=0; i<words.length; ++i){
            var comparelist = words[i].split('');
            comparelist.sort();
            if (letterlist.join('') == comparelist.join('')) {
                result.push(words[i]);
            }
        }
        return result;
    }
    getStarStrings(city) {
        var letters = city.toLowerCase().replace(/[^a-z]/gi, '').split("");
        var letterset = Array.from(new Set(letters));
        var result = '';
        for (var i = 0; i < letterset.length; i++){
            let re = new RegExp(letterset[i],'g');
            var count = (city.toLowerCase().match(re) || []).length;
            result += letterset[i]+':'+'*'.repeat(count);
            if (i < letterset.length-1){
                result += ',';
            }
        }
        return result;
    }

    DrivingSchool(mins) {
        return 30 + (mins > 65 ? Math.ceil((mins-60-5)/30) : 0)*10;
    }
}
module.exports = new Kata;
