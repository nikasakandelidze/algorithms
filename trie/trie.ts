class TrieNode {
    private nodes: Map<string, TrieNode>
    private wordCounter: number

    constructor(){
        this.nodes = new Map<string, TrieNode>()
        this.wordCounter = 0
    }

    getNode(character: string): TrieNode | undefined {
        return this.nodes.get(character)
    }

    addNodeForCharacter(character: string): TrieNode {
        const resultNode: TrieNode = new TrieNode()
        this.nodes.set(character, resultNode)
        return resultNode
    }
    
    incrementWordCounter(): void {
        this.wordCounter += 1
    }

    getNumberOfWords(): number {
        return this.wordCounter
    }

    isEmpty(): boolean {
        return this.nodes.size === 0
    }

    serialize(depth: number = 1): string {
        let string: string = `${' '.repeat(1)}{\n`
        for(const [key, value] of this.nodes) {
            string += `${' '.repeat(depth+1)}${key}${this.wordCounter ? `(${this.wordCounter} words)` : ''}:${value.serialize(depth+1)}`
        }
        string += `${' '.repeat(depth)}}\n`
        return string
    }
}

class Trie {
    private tree: TrieNode
    private size: number

    constructor(){
        this.tree = new TrieNode()
        this.size = 0
    }
    
    addWord(word: string): void {
        if(word){
            this.size += 1
            let prevNode: TrieNode | undefined = this.tree
            for(const symbol of word){
                let currentNode: TrieNode | undefined = prevNode?.getNode(symbol)
                if(!currentNode){
                    currentNode = prevNode?.addNodeForCharacter(symbol)
                }
                prevNode = currentNode
            }
            prevNode?.incrementWordCounter()
        }else{
            throw new Error(`Word can't be undefined, null or empty`)
        }
    }

    search(word: string): boolean {
        let node: TrieNode = this.tree
        for(let symbol of word) {
            const tempNode: TrieNode | undefined = node.getNode(symbol)
            if(tempNode) {
                node = tempNode
            } else {
                return false
            }
        }
        return true
    }

    numberOfWords(): number {
        return this.size
    }

    serilaize(): string {
        return this.tree.serialize()
    }

}

export default Trie