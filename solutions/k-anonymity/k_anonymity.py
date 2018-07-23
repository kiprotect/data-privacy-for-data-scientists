def is_valid(df, partition, k=3):
    """
    :param        df: The dataframe on which to check the partition.
    :param partition: The partition of the dataframe to check.
    :returns: True if the partition is valid according to our k-anonymity criteria, False otherwise.
    """
    if len(partition) < k:
        # we cannot split this partition further...
        return False
    return True

def partition_dataset(df, scale, is_valid):
    """
    :param       df: The dataframe to be partitioned.
    :param    scale: The column spans as generated before.
    :param is_valid: A function that takes a dataframe and a partition and returns True if the partition is valid.
    :returns: A list of valid partitions that cover the entire dataframe.
    """
    finished_partitions = []
    partitions = [df.index]
    while partitions:
        partition = partitions.pop(0)
        spans = get_spans(df, partition, scale)
        for column, span in sorted(spans.items(), key=lambda x:-x[1]):
            #we try to split this partition along a given column
            lp, rp = split(df, partition, column)
            if not is_valid(df, lp) or not is_valid(df, rp):
                continue
            # the split is valid, we put the new partitions on the list and continue
            partitions.extend((lp, rp))
            break
        else:
            # no split was possible, we add the partition to the finished partitions
            finished_partitions.append(partition)
    return finished_partitions