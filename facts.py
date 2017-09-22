import redis
import config


def get_random_facts():
    """
    Get a random LFC Fact from the Redis set
    """
    red = redis.Redis(host = 'localhost', db = config.subfeed_db)
    setname = "facts"
    fact = str(red.srandmember(setname))
    fact = fact[2:-1]
    return(fact)
    


