sample = 'The ADJECTIVE panda walked to the NOUN and then VERB. ' \
                'A nearby NOUN was \nunaffected by these events.'
path = '/Practice Projects\\text_for_madLibs.txt'
textFile = open(path, 'w')
textFile.write(sample)
textFile.close()
