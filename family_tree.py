'''algourithm d'arbre généalogique avec python  '''
class Member(object):
    def __init__(self, founder):
        """ 
        founder: string
        Initializes a member. 
        Name is the string of name of this node,
        parent is None, and no children
        """        
        self.name = founder
        self.parent = None         
        self.children = []    

    def __str__(self):
        return self.name    

    def add_parent(self, father):
        """
        father: Member
        Sets the parent of this node to the `father` Member node
        """
        self.parent = father   

    def get_parent(self):
        """
        Returns the parent Member node of this Member
        """
        return self.parent 

    def is_parent(self, father):
        """
        father: Member
        Returns: Boolean, whether or not `father` is the 
        parent of this Member
        """
        return self.parent == father  

    def add_child(self, child):
        """
        child: Member
        Adds another child Member node to this Member
        """
        self.children.append(child)   

    def is_child(self, child):
        """
        child: Member
        Returns: Boolean, whether or not `child` is a
        child of this Member
        """
        return child in self.children 


class Family(object):
    def __init__(self, founder):
        """ 
        Initialize with string of name of oldest ancestor

        Keyword arguments:
        founder -- string of name of oldest ancestor
        """

        self.names_to_nodes = {}
        self.root = Member(founder)    
        self.names_to_nodes[founder] = self.root   

    def set_children(self, father, list_of_children):
        """
        Set all children of the father. 

        Keyword arguments: 
        father -- father's name as a string
        list_of_children -- children names as strings
        """
        # convert name to Member node (should check for validity)
        mom_node = self.names_to_nodes[father]   
        # add each child
        for c in list_of_children:           
            # create Member node for a child   
            c_member = Member(c)               
            # remember its name to node mapping
            self.names_to_nodes[c] = c_member    
            # set child's parent
            c_member.add_parent(mom_node)        
            # set the parent's child
            mom_node.add_child(c_member)         
    
    def is_parent(self, father, kid):
        """
        Returns True or False whether father is parent of kid. 
        Keyword arguments: 
        father -- string of father's name
        kid -- string of kid's name
        """
        mom_node = self.names_to_nodes[father]
        child_node = self.names_to_nodes[kid]
        return child_node.is_parent(mom_node)   

    def is_child(self, kid, father):
        """
        Returns True or False whether kid is child of father. 

        Keyword arguments: 
        kid -- string of kid's name
        father -- string of father's name
        """        
        mom_node = self.names_to_nodes[father]   
        child_node = self.names_to_nodes[kid]
        return mom_node.is_child(child_node)

    def cousin(self, a, b):
        """
        Returns a tuple of (the cousin type, degree removed) 

        cousin type is an integer that is -1 if a and b
        are the same node or if one is the direct descendent 
        of the other.  Otherwise, cousin type is 0 or greater,
        representing the shorter distance to their common 
        ancestor as described in the exercises above.

        degree removed is the distance to the common ancestor

        Keyword arguments: 
        a -- string that is the name of a
        b -- string that is the name of b
        """
        
        ## YOUR CODE HERE ####
        a_node = self.names_to_nodes[a]
        b_node = self.names_to_nodes[b]

        def create_branch(node):
            branch = [node]
            parent = node.get_parent()

            while parent:
                branch.append(parent)
                parent = parent.get_parent()
            return branch

        if a_node.name == b_node.name:
            return (-1, 0)
        elif a_node.is_child(b_node) or b_node.is_child(a_node):
            return (-1, 0)

        a_branch = create_branch(a_node)
        b_branch = create_branch(b_node)

        b_parent_index = 0
        for a_parent_index, node in enumerate(a_branch):
            try:
                b_parent_index = b_branch.index(node)
                break
            except ValueError:
                pass

        cousin_type = max(a_parent_index, b_parent_index)
        degree_removed = abs(a_parent_index - b_parent_index)
        return (cousin_type, degree_removed)

if __name__ == '__main__':
    #Test section
    f = Family("ammar")
    f.set_children("ammar", ["islem", "mohammed","ahmed"])
    f.set_children("islem", ["fouad", "younes"])
    f.set_children("ahmed", ["zein", "adem"])

    f.set_children("adem", ["hakim", "ilyes"])
    f.set_children("younes", ["jawed", "khaled"])
    f.set_children("fouad", ["lamia", "mossa"])
    f.set_children("zein", ["nouh", "obayda", "nassim", "chaker"])

    words = ["zeroth", "first", "second", "third", "fourth", "fifth", "non"]

    ## These are your test cases. 

    ## The first test case should print out:
    ## 'islem' is a zeroth cousin 0 removed from 'fouad'
    t, r = f.cousin("zein", "fouad")
    print ("'zein' is a", words[t],"cousin", r, "removed from 'fouad'")

    ## For the remaining test cases, use the graph to figure out what should 
    ## be printed, and make sure that your code prints out the appropriate values.

    t, r = f.cousin("hakim", "khaled")
    print ("'hakim' is a", words[t],"cousin", r, "removed from 'khaled'")
