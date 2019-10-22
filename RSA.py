
print("enter 2 large prime numbers");
a=int(input("Enter prime number 1:"));
b=int(input("Enter prime number 2:"));
n=a*b;e=1;d=1;
encryptedText="";
decryptedText="";
pt =[];
ct =[];
phi_of_n=(a-1)*(b-1);
while phi_of_n%e==0 :
    e+=1;
print(f"public key e:{e}");
inputText = input("Enter the message").lower();
leng = len(inputText);
for i in range(0,leng) :
    pt.append(ord(inputText[i])-96);
    print(f"plain text : {pt[i]}");
    ct.append(pt[i]**e%n );
    print(f"cipher text : {ct[i]}");
    i+=1;
for i in range(1,leng):
    encryptedText+=chr(ct[i]);
print(f"Encrypted Text :{encryptedText}");
while (d*e)%phi_of_n!=1 :
    d+=1;
print(f"private key :{d}");
for i in range(0,leng):
    print(f"cipher text :{ct[i]}");
    pt[i]=ct[i]**d%n;
    print(f"plain text : {pt[i]}");
    decryptedText +=chr(pt[i]+96);
print(f"DecryptedText :{decryptedText}");