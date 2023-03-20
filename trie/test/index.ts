import Trie from "../trie";


const trie: Trie = new Trie()
trie.addWord('abc')
trie.addWord('bce')
trie.addWord('dce')
trie.addWord('dceve')

//console.log(trie.serilaize())

console.log(trie.search('abc'))
console.log(trie.search('a'))
console.log(trie.search('abcde'))
console.log(trie.search('dceve'))