class Node:
    def __init__(self,freq,sym=None,left=None,right=None):
        self.freq = freq
        self.sym = sym
        self.left = left
        self.right = right


def huffman_func(char_list):
    final_codes = {}
    char_freq_list = []

    unique_chars = set(char_list)
    print(f"unique_chars -- {unique_chars}")

    for char in unique_chars:
        char_freq_list.append((char_list.count(char),char))
    print(f"char_freq_list -- {char_freq_list}")

    sorted_char_freq_list = sorted(char_freq_list)
    print(f"sorted_char_freq_list -- {sorted_char_freq_list}")

    #Creating nodes
    nodes = []
    for char in sorted_char_freq_list:
        nodes.append((char,Node(char[0],char[1])))
    print(f"nodes -- {nodes}")
    

    while len(nodes)>1:
        print("Yes")
        nodes.sort()
        left = nodes[0][1]
        right = nodes[1][1]
        
        print(f"Node left -- {left}")
        print(f"Node right -- {right}")

        new_node = Node(left.freq+right.freq,left.sym+right.sym,left,right)
        print(f"Node parent -- {new_node.sym} -- {new_node.freq}")

        nodes.append(((left.freq+right.freq,left.sym+right.sym),new_node))
        nodes.pop(0)
        nodes.pop(0)

    # Final step
    for char in unique_chars:
        temp = new_node
        code = ""
        while char != temp.sym:
            if char in temp.left.sym:
                code = code + "0"
                temp = temp.left
            else:
                code = code + "1"
                temp = temp.right
        final_codes[char] = code
    
    return final_codes




char_data = "aaaacccbbdddddddeeefffff"
char_list = list(char_data)
print(f"Initial char_list -- {char_list}")
print(huffman_func(char_list))