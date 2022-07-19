def floodFill(self, image: List[List[int]], sr: int, sc: int, Color: int) -> List[List[int]]:
        colorized = [[0]*len(image[0]) for _ in range(len(image))] 
        self.colorize(image, colorized, sr, sc, image[sr][sc], Color)
        return image
    
def colorize(self, image, colorized, sr, sc, sourceColor, Color):
    if sr>=0 and sr<len(image) and sc>=0 and sc<len(image[0]):
        if image[sr][sc] == sourceColor and colorized[sr][sc] == 0:
            image[sr][sc] = Color
            colorized[sr][sc] = 1
            self.colorize(image, colorized, sr-1, sc, sourceColor, Color) 
            self.colorize(image, colorized, sr, sc+1, sourceColor, Color) 
            self.colorize(image, colorized, sr+1, sc, sourceColor, Color) 
            self.colorize(image, colorized, sr, sc-1, sourceColor, Color)