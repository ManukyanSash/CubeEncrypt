# CubeEncrypt
## Cube encryption algorithm  
Cube encryption is a specific encryption algorithm that involves the use of a cube structure to transform plaintext into ciphertext. It operates by dividing the plaintext into smaller chunks, typically groups of eight characters, and then performing a series of rotations on each chunk using a cube object.

Here's a simplified explanation of how cube encryption works:

Cube Object: The encryption process involves creating a cube object with a specific matrix structure. Each element in the matrix represents a position that corresponds to a character in the plaintext.

Chunking: The plaintext is divided into chunks, typically eight characters in length, to fit the cube structure. If the last chunk is shorter than eight characters, it may be padded with additional characters to reach the required length.

Encryption: For each chunk of the plaintext, a series of random rotations is applied to the cube object. These rotations involve shifting the elements of the matrix horizontally or vertically. The number of rotations and their direction (left, right, up, down) is determined randomly.

Key Generation: As the rotations are applied, the details of each rotation (e.g., number of rotations and direction) are recorded to create an encryption key. The key represents the specific sequence of rotations applied to each cube.

Ciphertext Formation: After the rotations, the cube object is "collected" to retrieve the encrypted chunk. This involves concatenating the characters from each position in the matrix, row by row, to form the ciphertext.

Reversing the Encryption: To decrypt the ciphertext, the encryption key is used to reverse the rotations applied during encryption. The cube object is initialized with the encrypted chunk, and the recorded rotations are applied in reverse order.

Decryption: The cube object is rotated back to its original state by applying the recorded rotations in reverse. The characters are then collected from the cube to obtain the original plaintext.   
## How to use
Call `encrypt` function in `CubeEncrypt` class to encrypt you letter.
```
enc = CubeEncrypt.encrypt("Hello, world!")
```
if you print `dec` you will get something like this  
```
(' ,owleHl\x00lr\x00\x00do!', 'L1,U3,R2,D3:L3,U3,R3,D2')
```
to `decrypte` use `CubeEncrypt.decrypt` function
```
dec = CubeEncrypt.decrypt(*enc)
```
or
```
dec = CubeEncrypt.decrypt(letter, key)
```
