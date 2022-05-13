from BlockClass import Block

def block_tester():
    new_chain = Block("Starting Balance Eric = $1000")
    new_chain.add_block("Eric Pays Kimia $10 for providing a great idea")
    new_chain.add_block("Eric Pays the cat $50 for ending the noise")
    new_chain.add_block("The cat pays Pet Food Express $20 for catnip")
    print()
    new_chain.block_checker()
    # new_chain.replay()
    # print()
    #
    # # Cat tried to hack the chain
    # fraud = "Eric Pays the cat $500 for ending the noise"
    # new_chain._next._next._data = fraud
    # new_chain.replay()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    block_tester()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
