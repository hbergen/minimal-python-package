
__all__ = ["speak", "fight", "chatter"]


def speak():
    """ A typical Hodor response
    """

    return ("Hodor")

def fight():
    """ Hodor gets angry
    """

    return ("Hodor!!!!!!!!!@$^&&J##HODOR!!!!!!!!!")

def chatter(nwords):
    """ Hodor gets talkative

         Parameters
         -----------------
         nwords : int
            Number of words Hodor should speak
    """
    return('Hodor ' * nwords)