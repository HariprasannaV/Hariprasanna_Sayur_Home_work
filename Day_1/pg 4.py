"""
write a program to find if two strings are same.
two string are considered same if both strings have same letters in same order, but from different starting point
eg abcd is same as bcda ('a' is moved to the right)
abcd is same as cdab
abcd is  not same as cdba

123456 = 456123
123456 not = 412356
hint -
there are many simple answers. you can try with slice function

"""

ip_sting1 = str(input("Enter the Word 1 : "))
ip_sting2 = str(input("Enter the Word 2 : "))

if len(ip_sting1) != len(ip_sting2):
    print(f'{ip_sting1} is not same as {ip_sting2}')


else:
    for i in range(len(ip_sting1)):
        new_string = ip_sting1[i:] + ip_sting1[:i]
        print(new_string)


        if new_string == ip_sting2:
            print(f'{ip_sting1} is same as {ip_sting2}')
            break

    else:
        print(f'{ip_sting1} is not same as {ip_sting2}')



# else:
#     new_string = ip_sting1 + ip_sting1  #concatenate
#     print(new_string)
#
#     if ip_sting2 in new_string:
#         print(f'{ip_sting1} is same as {ip_sting2}')
#
#     else:
#         print(f'{ip_sting1} is not same as {ip_sting2}')
"""
Output 1:

Enter the Word 1 : abcdefgh
Enter the Word 2 : ghabcdef
abcdefgh is same as ghabcdef

Output 2:

Enter the Word 1 : abcdef
Enter the Word 2 : fedcba
abcdef is not same as fedcba
"""

"""
ip1 = abcd

new string = abcd because 

ip2 =cdab

cdab in abcdabcd

"""