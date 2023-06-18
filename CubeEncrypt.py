class Cube:
    def __init__(self, str):
        self._matrix = [[0,1,2,3],
                        [4,5,6,7]]
        
        for i in range(len(self._matrix)):
            for j in range(len(self._matrix[i])):
                if self._matrix[i][j] < len(str):
                    self._matrix[i][j] = str[self._matrix[i][j]]
                else:
                    self._matrix[i][j] = "\0"
    
    @property
    def matrix(self):
        return self._matrix

    @matrix.setter
    def matrix(self, obj):
        self._matrix = obj

    def _rot_right(self):
        for i in range(len(self.matrix)):
            tmp = self._matrix[i][-1]
            for j in range(len(self.matrix[i])-1, 0, -1):
                self.matrix[i][j] = self.matrix[i][j-1]
            self.matrix[i][0] = tmp

    def _rot_up(self):
        for i in range(2):
            self.matrix[0][0+i], self.matrix[1][0+i] = self.matrix[1][0+i], self.matrix[0][0+i]
            self.matrix[0][0+i], self.matrix[1][3-i] = self.matrix[1][3-i], self.matrix[0][0+i]
            self.matrix[0][3-i], self.matrix[0][0+i] = self.matrix[0][0+i], self.matrix[0][3-i]  

    def right(self, count):
        count = count % 4
        for _ in range(count):
            self._rot_right() 

    def left(self, count):
        count = count % 4
        if count == 0:
            return
        for _ in range(4 - count):
            self._rot_right() 

    def up(self, count):
        count = count % 4
        for _ in range(count):
            self._rot_up()

    def down(self, count):
        count = count % 4
        if count == 0:
            return
        for _ in range(4 - count):
            self._rot_up()

    def collect(self):
        res = str()
        for line in self.matrix:
            for char in line:
                res += char
        return res


class CubeEncrypt:
    @staticmethod
    def encrypt(letter: str) -> tuple:
        from random import randint
        cubes = list()
        key = str()
        res = str()
        for i in range(len(letter) // 8 + (len(letter) % 8 != 0)):
            cubes.append(Cube(letter[i * 8 : i * 8 + 8]))
        
        for i in range(len(cubes)):
            l = randint(0, 3)
            u = randint(0, 3)
            r = randint(0, 3)
            d = randint(0, 3)
            key += f"L{l},U{u},R{r},D{d}:"
            cubes[i].left(l)
            cubes[i].up(u)
            cubes[i].right(r)
            cubes[i].down(d)
            res += cubes[i].collect()
        key = key[:-1]
        return (res, key)
    
    @staticmethod
    def decrypt(*args) -> str:
        letter = args[0]
        key = args[1]
        res = str()
        cubes = list()
        for i in range(len(letter) // 8 + (len(letter) % 8 != 0)):
            cubes.append(Cube(letter[i * 8 : i * 8 + 8]))

        rotations = key[::-1].split(":")
        for i in range(len(rotations)):
            rotations[i] = rotations[i].split(",")

        rotations.reverse()

        for cube in range(len(cubes)):
            for rotation in rotations[cube]:
                if rotation[1] == "L":
                    cubes[cube].right(int(rotation[0]))
                elif rotation[1] == "U":
                    cubes[cube].down(int(rotation[0]))
                elif rotation[1] == "R":
                    cubes[cube].left(int(rotation[0]))
                else:
                    cubes[cube].up(int(rotation[0]))

        for cube in cubes:
            res += cube.collect()
                   
        return res
    