
#
# Complete the 'counts' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY teamA
#  2. INTEGER_ARRAY teamB
#

def counts(teamA, teamB):
    # Write your code here
    ans = []
    for i in range(len(teamB)):
        tot = 0
        for j in range(len(teamA)):
            if teamB[i] >= teamA[j]:
                tot +=1
        ans.append(tot)
    return ans  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    teamA_count = int(input().strip())

    teamA = []

    for _ in range(teamA_count):
        teamA_item = int(input().strip())
        teamA.append(teamA_item)

    teamB_count = int(input().strip())

    teamB = []

    for _ in range(teamB_count):
        teamB_item = int(input().strip())
        teamB.append(teamB_item)

    result = counts(teamA, teamB)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()