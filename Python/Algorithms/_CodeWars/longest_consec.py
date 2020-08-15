import unittest, datetime, time

from pprint import pprint
def longest_consec(strarr, k):
    result = ''
    if len(strarr) == 0 or k > len(strarr) or k<= 0:
        return result
    
    for i in range(len(strarr)-(k-1)):
        c = ''.join(strarr[i:i+k])
        if len(c) > len(result):
            result = c
    return result
    
class longest_consec_test(unittest.TestCase):
    def setUp(self):
        self.starttime = datetime.datetime.now()
    def tearDown(self):
        t = datetime.datetime.now() - self.starttime
        #print('test time:', self.id(), t) 
        print(str(t.seconds)+'.'+str(t.microseconds).zfill(6)+' seconds '+self.id())
        
    def test_1(self):
        time.sleep(1.432)
        self.assertEqual(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2), 'abigailtheta')
    def test_2(self):
        self.assertEqual(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1), 'oocccffuucccjjjkkkjyyyeehh')
    def test_3(self):
        self.assertEqual(longest_consec([],3), '')
    def test_4(self):
        self.assertEqual(longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2), 'wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck')
    def test_5(self):
        self.assertEqual(longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2), 'wlwsasphmxxowiaxujylentrklctozmymu')
    def test_6(self):
        self.assertEqual(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2), '')
    def test_7(self):
        self.assertEqual(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3), 'ixoyx3452zzzzzzzzzzzz')
    def test_8(self):
        self.assertEqual(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15), '')
    def test_9(self):
        self.assertEqual(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0), '')
    def test_10(self):
        self.assertEqual(longest_consec(
        ['dtttppooqtn', 'lllaaadddyy', 'vvgggoooa', 'lllqqo', 'ppxxssy', 'xgssshmm', 'bpppwhhh',
         'sssmmmddbb', 'fcccwqqq', 'dddmqqzzppiin', 'aapppiii', 'mmggxx', 'afqaa', 'vvggyyyhip',
         'tttnnneeebcp', 'ffbjjja', 'ggbbii', 'lnntttyyrzppkk', 'ssrrvvvgggg',
         'fffnnns', 'nsssvpppjjjf', 'pqqny', 'qgggbbbsstttjj', 'edddsssmmmssr', 'naaqqqrggg',
         'vvwkkfffqqzd', 'mnzwwe', 'ssiiwwpoiisssreee', 'upccciiiyy', 'ttissshhyyy', 'cvvvvdduuu',
         'gkkkfcccuuyyy', 'zssdnntthhhj', 'qqxyykkk', 'jjjjqqtttwwooob', 'kkkjvvsss', 'xllggghhoxxxzzz',
         'llhhxt', 'kkssstlqqypppaaa', 'iiiaaatttlf', 'ssmmmhhhxnnnkkkk', 'hhjjjbh', 'xhhhhhffxxxs', 'aaaiiyykkknnwww',
         'ddfnnp', 'lllpxxewvv', 'iiiyyygggnnnhdddkkkp', 'ssbbppputtccc', 'ooovnnmmm', 'zfffeennkkuuunnz', 'dddfuuuccfff',
         'iaqqqqqq', 'cgggzzz', 'rrrvxxxapppuutghhh', 'axxkkke', 'tttfmm', 'eeevvvsr', 'ghhhbbbmmpp', 'llwweec',
         'cccxagghyyy', 'uuaammiiddazzuuv', 'iiihhhyyyccvbbb', 'jjvvtttccppp', 'pggguutg', 'llaacpp',
         'rqqqmreevu', 'rrrrrraajjjetyy', 'qqqoouukp', 'llloookkll', 'mqqooommjjjcc', 'rrrezzzwwiiiw',
         'aaaennn', 'uuuwwxynn', 'tttvvvzvvv', 'djiuuu', 'iiivvttt', 'hfssq', 'zzkkko', 'rrdddzzzppaw',
         'oovuqldqq', 'yymmmuuvrsssddd', 'kpgggcccbyyggfff', 'rrrjwwwrrr', 'qqejmmm', 'ccffccc',
         'klllipp', 'doeeettzpmi', 'oookkkooovvvmwgggfff', 'zzzzdppzzzzz', 'ppjjjxxee', 'rrmmmooo',
         'zzcccddbf', 'fffgggccsss', 'cddnnnccrruuhwjj', 'olcccllndqqql', 'vlmmmj', 'aaazzoooqqqdd',
         'xxaaasfqeevvwwuu', 'jjeeeaanniiiy', 'bbbxxooo', 'sbbpppp', 'ffaagg', 'fffrrccveeeyyy', 'xpccwwb',
         'tfffbbbhhhxx', 'lltttrrrxxxxx', 'byyyaazzz', 'mwwddiiiaxxxbbb', 'wgfffggfff', 'bugoo', 'ccvvvpbb',
         'sskkmmmggghh', 'hhhmfybb', 'qqquubbbwwuvvk', 'dduiizzxxe', 'vvzzzuuupppw', 'mmmccrrlllcc', 'uuuvvuuuujjjzz',
         'fffyyymmmxxf', 'jgggannjjjqqooyy', 'hmmlrrrzz', 'ucfkkjggfffcc', 'bbgggddzzggg', 'kkkccdwwwnnbbbw',
         'iidddczzdddee', 'qqhhhdddpppb', 'eeekdddwwwkfsooo', 'mmuf', 'oyyyqqquuiijkkuuu', 'wwwxpppytii']
         , 1), 'iiiyyygggnnnhdddkkkp')
    def test_11(self):
        self.assertEqual(longest_consec(
        ['dtttppooqtn', 'lllaaadddyy', 'vvgggoooa', 'lllqqo', 'ppxxssy', 'xgssshmm', 'bpppwhhh',
         'sssmmmddbb', 'fcccwqqq', 'dddmqqzzppiin', 'aapppiii', 'mmggxx', 'afqaa', 'vvggyyyhip',
         'tttnnneeebcp', 'ffbjjja', 'ggbbii', 'lnntttyyrzppkk', 'ssrrvvvgggg',
         'fffnnns', 'nsssvpppjjjf', 'pqqny', 'qgggbbbsstttjj', 'edddsssmmmssr', 'naaqqqrggg',
         'vvwkkfffqqzd', 'mnzwwe', 'ssiiwwpoiisssreee', 'upccciiiyy', 'ttissshhyyy', 'cvvvvdduuu',
         'gkkkfcccuuyyy', 'zssdnntthhhj', 'qqxyykkk', 'jjjjqqtttwwooob', 'kkkjvvsss', 'xllggghhoxxxzzz',
         'llhhxt', 'kkssstlqqypppaaa', 'iiiaaatttlf', 'ssmmmhhhxnnnkkkk', 'hhjjjbh', 'xhhhhhffxxxs', 'aaaiiyykkknnwww',
         'ddfnnp', 'lllpxxewvv', 'iiiyyygggnnnhdddkkkp', 'ssbbppputtccc', 'ooovnnmmm', 'zfffeennkkuuunnz', 'dddfuuuccfff',
         'iaqqqqqq', 'cgggzzz', 'rrrvxxxapppuutghhh', 'axxkkke', 'tttfmm', 'eeevvvsr', 'ghhhbbbmmpp', 'llwweec',
         'cccxagghyyy', 'uuaammiiddazzuuv', 'iiihhhyyyccvbbb', 'jjvvtttccppp', 'pggguutg', 'llaacpp',
         'rqqqmreevu', 'rrrrrraajjjetyy', 'qqqoouukp', 'llloookkll', 'mqqooommjjjcc', 'rrrezzzwwiiiw',
         'aaaennn', 'uuuwwxynn', 'tttvvvzvvv', 'djiuuu', 'iiivvttt', 'hfssq', 'zzkkko', 'rrdddzzzppaw',
         'oovuqldqq', 'yymmmuuvrsssddd', 'kpgggcccbyyggfff', 'rrrjwwwrrr', 'qqejmmm', 'ccffccc',
         'klllipp', 'doeeettzpmi', 'oookkkooovvvmwgggfff', 'zzzzdppzzzzz', 'ppjjjxxee', 'rrmmmooo',
         'zzcccddbf', 'fffgggccsss', 'cddnnnccrruuhwjj', 'olcccllndqqql', 'vlmmmj', 'aaazzoooqqqdd',
         'xxaaasfqeevvwwuu', 'jjeeeaanniiiy', 'bbbxxooo', 'sbbpppp', 'ffaagg', 'fffrrccveeeyyy', 'xpccwwb',
         'tfffbbbhhhxx', 'lltttrrrxxxxx', 'byyyaazzz', 'mwwddiiiaxxxbbb', 'wgfffggfff', 'bugoo', 'ccvvvpbb',
         'sskkmmmggghh', 'hhhmfybb', 'qqquubbbwwuvvk', 'dduiizzxxe', 'vvzzzuuupppw', 'mmmccrrlllcc', 'uuuvvuuuujjjzz',
         'fffyyymmmxxf', 'jgggannjjjqqooyy', 'hmmlrrrzz', 'ucfkkjggfffcc', 'bbgggddzzggg', 'kkkccdwwwnnbbbw',
         'iidddczzdddee', 'qqhhhdddpppb', 'eeekdddwwwkfsooo', 'mmuf', 'oyyyqqquuiijkkuuu', 'wwwxpppytii']
         , 1), 'iiiyyygggnnnhdddkkkp')
    def test_12(self):
        self.assertEqual(longest_consec(
        ['dtttppooqtn', 'lllaaadddyy', 'vvgggoooa', 'lllqqo', 'ppxxssy', 'xgssshmm', 'bpppwhhh',
         'sssmmmddbb', 'fcccwqqq', 'dddmqqzzppiin', 'aapppiii', 'mmggxx', 'afqaa', 'vvggyyyhip',
         'tttnnneeebcp', 'ffbjjja', 'ggbbii', 'lnntttyyrzppkk', 'ssrrvvvgggg',
         'fffnnns', 'nsssvpppjjjf', 'pqqny', 'qgggbbbsstttjj', 'edddsssmmmssr', 'naaqqqrggg',
         'vvwkkfffqqzd', 'mnzwwe', 'ssiiwwpoiisssreee', 'upccciiiyy', 'ttissshhyyy', 'cvvvvdduuu',
         'gkkkfcccuuyyy', 'zssdnntthhhj', 'qqxyykkk', 'jjjjqqtttwwooob', 'kkkjvvsss', 'xllggghhoxxxzzz',
         'llhhxt', 'kkssstlqqypppaaa', 'iiiaaatttlf', 'ssmmmhhhxnnnkkkk', 'hhjjjbh', 'xhhhhhffxxxs', 'aaaiiyykkknnwww',
         'ddfnnp', 'lllpxxewvv', 'iiiyyygggnnnhdddkkkp', 'ssbbppputtccc', 'ooovnnmmm', 'zfffeennkkuuunnz', 'dddfuuuccfff',
         'iaqqqqqq', 'cgggzzz', 'rrrvxxxapppuutghhh', 'axxkkke', 'tttfmm', 'eeevvvsr', 'ghhhbbbmmpp', 'llwweec',
         'cccxagghyyy', 'uuaammiiddazzuuv', 'iiihhhyyyccvbbb', 'jjvvtttccppp', 'pggguutg', 'llaacpp',
         'rqqqmreevu', 'rrrrrraajjjetyy', 'qqqoouukp', 'llloookkll', 'mqqooommjjjcc', 'rrrezzzwwiiiw',
         'aaaennn', 'uuuwwxynn', 'tttvvvzvvv', 'djiuuu', 'iiivvttt', 'hfssq', 'zzkkko', 'rrdddzzzppaw',
         'oovuqldqq', 'yymmmuuvrsssddd', 'kpgggcccbyyggfff', 'rrrjwwwrrr', 'qqejmmm', 'ccffccc',
         'klllipp', 'doeeettzpmi', 'oookkkooovvvmwgggfff', 'zzzzdppzzzzz', 'ppjjjxxee', 'rrmmmooo',
         'zzcccddbf', 'fffgggccsss', 'cddnnnccrruuhwjj', 'olcccllndqqql', 'vlmmmj', 'aaazzoooqqqdd',
         'xxaaasfqeevvwwuu', 'jjeeeaanniiiy', 'bbbxxooo', 'sbbpppp', 'ffaagg', 'fffrrccveeeyyy', 'xpccwwb',
         'tfffbbbhhhxx', 'lltttrrrxxxxx', 'byyyaazzz', 'mwwddiiiaxxxbbb', 'wgfffggfff', 'bugoo', 'ccvvvpbb',
         'sskkmmmggghh', 'hhhmfybb', 'qqquubbbwwuvvk', 'dduiizzxxe', 'vvzzzuuupppw', 'mmmccrrlllcc', 'uuuvvuuuujjjzz',
         'fffyyymmmxxf', 'jgggannjjjqqooyy', 'hmmlrrrzz', 'ucfkkjggfffcc', 'bbgggddzzggg', 'kkkccdwwwnnbbbw',
         'iidddczzdddee', 'qqhhhdddpppb', 'eeekdddwwwkfsooo', 'mmuf', 'oyyyqqquuiijkkuuu', 'wwwxpppytii']
         , 1), 'iiiyyygggnnnhdddkkkp')
if __name__ == '__main__':
    unittest.main()
