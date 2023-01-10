/**
 * @param {string} pattern
 * @param {string} s
 * @return {boolean}
 */

 //https://leetcode.com/problems/word-pattern/description/
var wordPattern = function(pattern, s) {
    const mapping = {}
    const seen = new Set()
    const tokens = s.split(" ")
    if(tokens.length !== pattern.length) return false
    for(let i=0; i<pattern.length; i++){
        const char = pattern[i]
        const token = tokens[i]
        if(mapping[char]){
            if(mapping[char]!==token)return false
        }else{
            if(seen.has(token)){return false}
            mapping[char]=token
            seen.add(token)
        }
    }
    return true
};