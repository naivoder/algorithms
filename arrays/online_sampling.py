"""
this file modifies the offline_sampling solution to add new/remove old packet with equal probabilty to maintain a random subset of the n+1 packets

"""
import itertools, random

def online_random_sample(stream, k, debug=False):
    # store first k elements
    running_sample  = list(itertools.islice(stream, k))
    if debug:
        print('Starting sample:', running_sample)
    num_seen = k
    for packet in stream:
        num_seen += 1
        # generate random number in range (0, num_seen - 1)
        to_replace = random.randrange(num_seen)
        # replace if less than k
        if to_replace < k:
            if debug:
                print('Replacing %s with %s' % (running_sample[to_replace], packet))
            running_sample[to_replace] = packet
    return running_sample

if __name__=="__main__":
    stream = [1,2,3,4,5,6,7,8,9]
    print(online_random_sample(stream, 2, debug=True))
