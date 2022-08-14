 #The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    l = len(s)
    result = ''
    for i in range(l):
        char = s[i]
      # Encrypt uppercase characters in plain text
      
        if (char.isupper()):
            result += chr((ord(char) + k-65) % 26 + 65)
      # Encrypt lowercase characters in plain text
        elif (char.islower()):
            result += chr((ord(char) + k - 97) % 26 + 97)
        else:
            result += char          
    return result
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
