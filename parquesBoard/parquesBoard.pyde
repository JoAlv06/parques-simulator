import random
def setup():
    size(800, 800)
    frameRate(1)
    global red1,red2,red3,red4,green1,green2,green3,green4,blue1,blue2,blue3,blue4,yellow1,yellow2,yellow3,yellow4
    red1 = redPiece(1)
    red2 = redPiece(2)
    red3 = redPiece(3)
    red4 = redPiece(4)
    
    green1 = greenPiece(1)
    green2 = greenPiece(2)
    green3 = greenPiece(3)
    green4 = greenPiece(4)
    
    blue1 = bluePiece(1)
    blue2 = bluePiece(2)
    blue3 = bluePiece(3)
    blue4 = bluePiece(4)
    
    yellow1 = yellowPiece(1)
    yellow2 = yellowPiece(2)
    yellow3 = yellowPiece(3)
    yellow4 = yellowPiece(4)

def board():
    background(150)
    #4 corners
    fill(0,0,200)
    rect(0,0,200,200)
    fill(200,200,0)
    rect(0,600,200,200)
    fill(0,200,0)
    rect(600,0,200,200)
    fill(200,0,0)
    rect(600,600,200,200)
    
    #bottom middle left tiles
    fill(200,200,0)
    rect(200,760,133,40)
    rect(200,720,133,40)
    rect(200,680,133,40)
    rect(200,640,133,40)
    rect(200,600,133,40)
    
    #bottom middle tiles
    fill(200,0,0)
    rect(332,760,134,40)
    rect(332,720,134,40)
    rect(332,680,134,40)
    rect(332,640,134,40)
    rect(332,600,134,40)
    rect(332,560,134,40)
    rect(332,520,134,40)
    rect(332,480,134,40)
    rect(332,440,134,40)
   
    #bottom middle right tiles
    fill(200,0,0)
    rect(466,760,133,40)
    rect(466,720,133,40)
    rect(466,680,133,40)
    rect(466,640,133,40)
    rect(466,600,133,40)
    
    #bottom right arc
    arc(599,600, 266, 266, PI,radians(195),PIE)
    arc(599,600, 266, 266, radians(195),radians(210),PIE)
    arc(599,600, 266, 266, radians(210),radians(225),PIE)
    arc(599,600, 266, 266, radians(225),radians(240),PIE)
    arc(599,600, 266, 266, radians(240),radians(255),PIE)
    arc(599,600, 266, 266, radians(255),radians(270),PIE)
    
    #bottom right tiles
    rect(600,467,40,133)
    rect(640,467,40,133)
    rect(680,467,40,133)
    rect(720,467,40,133)
    rect(760,467,40,133)
    
    #middle right tiles
    fill(0,200,0)
    rect(440,333,40,134)
    rect(480,333,40,134)
    rect(520,333,40,134)
    rect(560,333,40,134)
    rect(600,333,40,134)
    rect(640,333,40,134)
    rect(680,333,40,134)
    rect(720,333,40,134)
    rect(760,333,40,134)
    
    #top right tiles
    rect(600,200,40,134)
    rect(640,200,40,134)
    rect(680,200,40,134)
    rect(720,200,40,134)
    rect(760,200,40,134)
    
    #top right arc
    arc(600, 200, 266, 266, HALF_PI,radians(105),PIE)
    arc(600, 200, 266, 266, radians(105),radians(120),PIE)
    arc(600, 200, 266, 266, radians(120),radians(135),PIE)
    arc(600, 200, 266, 266, radians(135),radians(150),PIE)
    arc(600, 200, 266, 266, radians(150),radians(165),PIE)
    arc(600, 200, 266, 266, radians(165),PI,PIE) 
    
    #top middle right tiles
    rect(467,0,133,40)
    rect(467,40,133,40)
    rect(467,80,133,40)
    rect(467,120,133,40)
    rect(467,160,133,40)
    
    #top middle tiles
    fill(0,0,200)
    rect(333,0,134,40)
    rect(333,40,134,40)
    rect(333,80,134,40)
    rect(333,120,134,40)
    rect(333,160,134,40)
    rect(333,200,134,40)
    rect(333,240,134,40)
    rect(333,280,134,40)
    rect(333,320,134,40)
    
    #top middle left tiles
    rect(200,0,133,40)
    rect(200,40,133,40)
    rect(200,80,133,40)
    rect(200,120,133,40)
    rect(200,160,133,40)
    
    #top left arc
    arc(200, 200, 266, 266, 0,radians(15),PIE)
    arc(200, 200, 266, 266, radians(15),radians(30),PIE)
    arc(200, 200, 266, 266, radians(30),radians(45),PIE)
    arc(200, 200, 266, 266, radians(45),radians(60),PIE)
    arc(200, 200, 266, 266, radians(60),radians(75),PIE)
    arc(200, 200, 266, 266, radians(75),radians(90),PIE)
    
    #top left tiles
    rect(0,200,40,133)
    rect(40,200,40,133)
    rect(80,200,40,133)
    rect(120,200,40,133)
    rect(160,200,40,133)
    
    #middle left tiles
    fill(200,200,0)
    rect(0,333,40,134)
    rect(40,333,40,134)
    rect(80,333,40,134)
    rect(120,333,40,134)
    rect(160,333,40,134)
    rect(200,333,40,134)
    rect(240,333,40,134)
    rect(280,333,40,134)
    rect(320,333,40,134)
    
    #bottom left tiles
    rect(0,467,40,133)
    rect(40,467,40,133)
    rect(80,467,40,133)
    rect(120,467,40,133)
    rect(160,467,40,133)
    
    #bottom left arc
    arc(200, 600, 266, 266, PI + HALF_PI, radians(285), PIE)
    arc(200, 600, 266, 266, radians(285), radians(300), PIE)
    arc(200, 600, 266, 266, radians(300), radians(315), PIE)
    arc(200, 600, 266, 266, radians(315), radians(330), PIE)
    arc(200, 600, 266, 266, radians(330), radians(345), PIE)
    arc(200, 600, 265, 266, radians(345), 2*PI, PIE)
    
    fill(100)
    circle(400,400,160)
def red(num):
    red1Pos = [[640,640],[475,620],[475,585],[485,550],[500,525],[525,502],[552,485],[585,478],[620,478],[660,478],[700,478],[740,478],[780,478],[780,345],[780,210],[740,210],[700,210],[660,210],[620,210],[594,250],[580,248],[565,245],[550,238],[545,223],[543,208],[590,180],[590,140],[590,100],[590,60],[590,20],[457,20],[322,20],[322,60],[322,100],[322,140],[322,180],[322,220],[315,247],[300,272],[276,292],[247,312],[218,320],[180,322],[140,322],[100,322],[60,322],[20,322],[20,456],[20,589],[60,589],[100,589],[140,589],[180,589],[207,545],[222,545],[234,555],[240,570],[250,580],[257,592],[212,618],[212,658],[212,698],[212,738],[212,778],[345,778],[345,738],[345,698],[345,658],[345,618],[345,578],[345,538],[345,498],[362,460]]
    red2Pos = [[760,640],[red1Pos[1][0] + 25, red1Pos[1][1]],[red1Pos[2][0] + 20, red1Pos[2][1]],[red1Pos[3][0] + 20, red1Pos[3][1] + 12],[red1Pos[4][0] + 15, red1Pos[4][1] + 14],[red1Pos[5][0] + 12, red1Pos[5][1] + 18],[red1Pos[6][0] + 10, red1Pos[6][1] + 20],[red1Pos[7][0] + 2, red1Pos[7][1] + 20],[red1Pos[8][0], red1Pos[8][1] + 25],[red1Pos[9][0], red1Pos[9][1] + 25],[red1Pos[10][0], red1Pos[10][1] + 25],[red1Pos[11][0], red1Pos[11][1] + 25],[red1Pos[12][0], red1Pos[12][1] + 25],[red1Pos[13][0], red1Pos[13][1] + 25],[red1Pos[14][0], red1Pos[14][1] + 25],[red1Pos[15][0], red1Pos[15][1] + 25],[red1Pos[16][0], red1Pos[16][1] + 25],[red1Pos[17][0], red1Pos[17][1] + 25],[red1Pos[18][0], red1Pos[18][1] + 25],[red1Pos[19][0] - 2, red1Pos[19][1] + 25],[red1Pos[20][0] - 6, red1Pos[20][1] + 18],[red1Pos[21][0] - 11, red1Pos[21][1] + 16],[red1Pos[22][0] - 14, red1Pos[22][1] + 14],[red1Pos[23][0] - 18, red1Pos[23][1] + 8],[red1Pos[24][0] - 20, red1Pos[24][1] + 3],[red1Pos[25][0] - 30, red1Pos[25][1]],[red1Pos[26][0] - 30, red1Pos[26][1]],[red1Pos[27][0] - 30, red1Pos[27][1]],[red1Pos[28][0] - 30, red1Pos[28][1]],[red1Pos[29][0] - 30, red1Pos[29][1]],[red1Pos[30][0] - 30, red1Pos[30][1]],[red1Pos[31][0] - 30, red1Pos[31][1]],[red1Pos[32][0] - 30, red1Pos[32][1]],[red1Pos[33][0] - 30, red1Pos[33][1]],[red1Pos[34][0] - 30, red1Pos[34][1]],[red1Pos[35][0] - 30, red1Pos[35][1]],[red1Pos[36][0] - 20, red1Pos[36][1] - 3],[red1Pos[37][0] - 18, red1Pos[37][1] - 7],[red1Pos[38][0] - 16, red1Pos[38][1] - 11],[red1Pos[39][0] - 14, red1Pos[39][1] - 15],[red1Pos[40][0] - 8, red1Pos[40][1] - 20],[red1Pos[41][0] - 3, red1Pos[41][1] - 20],[red1Pos[42][0], red1Pos[42][1] - 25],[red1Pos[43][0], red1Pos[43][1] - 25],[red1Pos[44][0], red1Pos[44][1] - 25],[red1Pos[45][0], red1Pos[45][1] - 25],[red1Pos[46][0], red1Pos[46][1] - 25],[red1Pos[47][0], red1Pos[47][1] - 25],[red1Pos[48][0], red1Pos[48][1] - 25],[red1Pos[49][0], red1Pos[49][1] - 25],[red1Pos[50][0], red1Pos[50][1] - 25],[red1Pos[51][0], red1Pos[51][1] - 25],[red1Pos[52][0], red1Pos[52][1] - 20],[red1Pos[53][0] + 2, red1Pos[53][1] - 20],[red1Pos[54][0] + 7, red1Pos[54][1] - 18],[red1Pos[55][0] + 12, red1Pos[55][1] - 16],[red1Pos[56][0] + 18, red1Pos[56][1] - 14],[red1Pos[57][0] + 20, red1Pos[57][1] - 9],[red1Pos[58][0] + 20, red1Pos[58][1] - 3],[red1Pos[59][0] + 25, red1Pos[59][1]],[red1Pos[60][0] + 25, red1Pos[60][1]],[red1Pos[61][0] + 25, red1Pos[61][1]],[red1Pos[62][0] + 25, red1Pos[62][1]],[red1Pos[63][0] + 25, red1Pos[63][1]],[red1Pos[64][0] + 25, red1Pos[64][1]],[red1Pos[65][0] + 25, red1Pos[65][1]],[red1Pos[66][0] + 25, red1Pos[66][1]],[red1Pos[67][0] + 25, red1Pos[67][1]],[red1Pos[68][0] + 25, red1Pos[68][1]],[red1Pos[69][0] + 25, red1Pos[69][1]],[red1Pos[70][0] + 25, red1Pos[70][1]],[red1Pos[71][0] + 25, red1Pos[71][1]],[red1Pos[72][0] + 25, red1Pos[72][1]]]
    red3Pos = [[640,760],[red2Pos[1][0] + 25, red2Pos[1][1]],[red2Pos[2][0] + 20, red2Pos[2][1] + 2],[red2Pos[3][0] + 20, red2Pos[3][1] + 8],[red2Pos[4][0] + 20, red2Pos[4][1] + 12],[red2Pos[5][0] + 14, red2Pos[5][1] + 16],[red2Pos[6][0] + 8, red2Pos[6][1] + 20],[red2Pos[7][0] + 2, red2Pos[7][1] + 20],[red2Pos[8][0], red2Pos[8][1] + 25],[red2Pos[9][0], red2Pos[9][1] + 25],[red2Pos[10][0], red2Pos[10][1] + 25],[red2Pos[11][0], red2Pos[11][1] + 25],[red2Pos[12][0], red2Pos[12][1] + 25],[red2Pos[13][0], red2Pos[13][1] + 25],[red2Pos[14][0], red2Pos[14][1] + 25],[red2Pos[15][0], red2Pos[15][1] + 25],[red2Pos[16][0], red2Pos[16][1] + 25],[red2Pos[17][0], red2Pos[17][1] + 25],[red2Pos[18][0], red2Pos[18][1] + 25],[red2Pos[19][0] - 2, red2Pos[19][1] + 25],[red2Pos[20][0] - 6, red2Pos[20][1] + 18],[red2Pos[21][0] - 11, red2Pos[21][1] + 16],[red2Pos[22][0] - 15, red2Pos[22][1] + 14],[red2Pos[23][0] - 18, red2Pos[23][1] + 8],[red2Pos[24][0] - 20, red2Pos[24][1] + 3],[red2Pos[25][0] - 30, red2Pos[25][1]],[red2Pos[26][0] - 30, red2Pos[26][1]],[red2Pos[27][0] - 30, red2Pos[27][1]],[red2Pos[28][0] - 30, red2Pos[28][1]],[red2Pos[29][0] - 30, red2Pos[29][1]],[red2Pos[30][0] - 30, red2Pos[30][1]],[red2Pos[31][0] - 30, red2Pos[31][1]],[red2Pos[32][0] - 30, red2Pos[32][1]],[red2Pos[33][0] - 30, red2Pos[33][1]],[red2Pos[34][0] - 30, red2Pos[34][1]],[red2Pos[35][0] - 30, red2Pos[35][1]],[red2Pos[36][0] - 20, red2Pos[36][1] - 3],[red2Pos[37][0] - 18, red2Pos[37][1] - 7],[red2Pos[38][0] - 16, red2Pos[38][1] - 11],[red2Pos[39][0] - 14, red2Pos[39][1] - 15],[red2Pos[40][0] - 8, red2Pos[40][1] - 20],[red2Pos[41][0] - 3, red2Pos[41][1] - 20],[red2Pos[42][0], red2Pos[42][1] - 25],[red2Pos[43][0], red2Pos[43][1] - 25],[red2Pos[44][0], red2Pos[44][1] - 25],[red2Pos[45][0], red2Pos[45][1] - 25],[red2Pos[46][0], red2Pos[46][1] - 25],[red2Pos[47][0], red2Pos[47][1] - 25],[red2Pos[48][0], red2Pos[48][1] - 25],[red2Pos[49][0], red2Pos[49][1] - 25],[red2Pos[50][0], red2Pos[50][1] - 25],[red2Pos[51][0], red2Pos[51][1] - 25],[red2Pos[52][0], red2Pos[52][1] - 20],[red2Pos[53][0] + 2, red2Pos[53][1] - 20],[red2Pos[54][0] + 7, red2Pos[54][1] - 18],[red2Pos[55][0] + 12, red2Pos[55][1] - 16],[red2Pos[56][0] + 18, red2Pos[56][1] - 14],[red2Pos[57][0]+ 20, red2Pos[57][1] - 9],[red2Pos[58][0] + 20, red2Pos[58][1] - 3],[red2Pos[59][0] + 25, red2Pos[59][1]],[red2Pos[60][0] + 25, red2Pos[60][1]],[red2Pos[61][0] + 25, red2Pos[61][1]],[red2Pos[62][0] + 25, red2Pos[62][1]],[red2Pos[63][0] + 25, red2Pos[63][1]],[red2Pos[64][0] + 25, red2Pos[64][1]],[red2Pos[65][0] + 25, red2Pos[65][1]],[red2Pos[66][0] + 25, red2Pos[66][1]],[red2Pos[67][0] + 25, red2Pos[67][1]],[red2Pos[68][0] + 25, red2Pos[68][1]],[red2Pos[69][0] + 25, red2Pos[69][1]],[red2Pos[70][0] + 25, red2Pos[70][1]],[red2Pos[71][0] + 25, red2Pos[71][1]],[red2Pos[72][0] + 25, red2Pos[72][1]]]
    red4Pos = [[760,760],[red3Pos[1][0] + 25, red3Pos[1][1]],[red3Pos[2][0] + 20, red3Pos[2][1] + 2],[red3Pos[3][0] + 20, red3Pos[3][1] + 8],[red3Pos[4][0] + 20, red3Pos[4][1] + 14],[red3Pos[5][0] + 14, red3Pos[5][1] + 16],[red3Pos[6][0] + 8, red3Pos[6][1] + 20],[red3Pos[7][0] + 2, red3Pos[7][1] + 20],[red3Pos[8][0], red3Pos[8][1] + 25],[red3Pos[9][0], red3Pos[9][1] + 25],[red3Pos[10][0], red3Pos[10][1] + 25],[red3Pos[11][0], red3Pos[11][1] + 25],[red3Pos[12][0], red3Pos[12][1] + 25],[red3Pos[13][0], red3Pos[13][1] + 25],[red3Pos[14][0], red3Pos[14][1] + 25],[red3Pos[15][0], red3Pos[15][1] + 25],[red3Pos[16][0], red3Pos[16][1] + 25],[red3Pos[17][0], red3Pos[17][1] + 25],[red3Pos[18][0], red3Pos[18][1] + 25],[red3Pos[19][0] - 2 , red3Pos[19][1] + 25],[red3Pos[20][0] - 6, red3Pos[20][1] + 18],[red3Pos[21][0] - 11, red3Pos[21][1] + 16],[red3Pos[22][0] - 15, red3Pos[22][1] + 14],[red3Pos[23][0] - 18, red3Pos[23][1] + 8],[red3Pos[24][0] - 20, red3Pos[24][1] + 3],[red3Pos[25][0] - 30, red3Pos[25][1]],[red3Pos[26][0] - 30, red3Pos[26][1]],[red3Pos[27][0] - 30, red3Pos[27][1]],[red3Pos[28][0] - 30, red3Pos[28][1]],[red3Pos[29][0] - 30, red3Pos[29][1]],[red3Pos[30][0] - 30, red3Pos[30][1]],[red3Pos[31][0] - 30, red3Pos[31][1]],[red3Pos[32][0] - 30, red3Pos[32][1]],[red3Pos[33][0] - 30, red3Pos[33][1]],[red3Pos[34][0] - 30, red3Pos[34][1]],[red3Pos[35][0] - 30, red3Pos[35][1]],[red3Pos[36][0] - 20, red3Pos[36][1] - 3],[red3Pos[37][0] - 18, red3Pos[37][1] - 7],[red3Pos[38][0] - 16, red3Pos[38][1] - 11],[red3Pos[39][0] - 14, red3Pos[39][1] - 15],[red3Pos[40][0] - 8, red3Pos[40][1] - 20],[red3Pos[41][0] - 3, red3Pos[41][1] - 20],[red3Pos[42][0], red3Pos[42][1] - 25],[red3Pos[43][0], red3Pos[43][1] - 25],[red3Pos[44][0], red3Pos[44][1] - 25],[red3Pos[45][0], red3Pos[45][1] - 25],[red3Pos[46][0], red3Pos[46][1] - 25],[red3Pos[47][0], red3Pos[47][1] - 25],[red3Pos[48][0], red3Pos[48][1] - 25],[red3Pos[49][0], red3Pos[49][1] - 25],[red3Pos[50][0], red3Pos[50][1] - 25],[red3Pos[51][0], red3Pos[51][1] - 25],[red3Pos[52][0], red3Pos[52][1] - 20],[red3Pos[53][0] + 2, red3Pos[53][1] - 20],[red3Pos[54][0] + 7, red3Pos[54][1] - 18],[red3Pos[55][0] + 12, red3Pos[55][1] - 16],[red3Pos[56][0] + 18, red3Pos[56][1] - 14],[red3Pos[57][0] + 20, red3Pos[57][1] - 9],[red3Pos[58][0] + 20, red3Pos[58][1] - 3],[red3Pos[59][0] + 25, red3Pos[59][1]],[red3Pos[60][0] + 25, red3Pos[60][1]],[red3Pos[61][0] + 25, red3Pos[61][1]],[red3Pos[62][0] + 25, red3Pos[62][1]],[red3Pos[63][0] + 25, red3Pos[63][1]],[red3Pos[64][0] + 25, red3Pos[64][1]],[red3Pos[65][0] + 25, red3Pos[65][1]],[red3Pos[66][0] + 25, red3Pos[66][1]],[red3Pos[67][0] + 25, red3Pos[67][1]],[red3Pos[68][0] + 25, red3Pos[68][1]],[red3Pos[69][0] + 25, red3Pos[69][1]],[red3Pos[70][0] + 25, red3Pos[70][1]],[red3Pos[71][0] + 25, red3Pos[71][1]],[red3Pos[72][0] + 25, red3Pos[72][1]]]
    if num == 1:
        return red1Pos
    if num == 2:
        return red2Pos
    if num == 3:
        return red3Pos
    if num == 4:
        return red4Pos

def green(num):
    red1Pos = red(1)
    red2Pos = red(2)
    red3Pos = red(3)
    green1Pos = [[640,40],[620,210],[594,250],[580,248],[565,245],[550,238],[545,223],[543,208],[590,180],[590,140],[590,100],[590,60],[590,20],[457,20],[322,20],[322,60],[322,100],[322,140],[322,180],[322,220],[315,247],[300,272],[276,292],[247,312],[218,320],[180,322],[140,322],[100,322],[60,322],[20,322],[20,456],[20,589],[60,589],[100,589],[140,589],[180,589],[207,545],[222,545],[234,555],[240,570],[250,580],[257,592],[212,618],[212,658],[212,698],[212,738],[212,778],[345,778],[479,778],[479,738],[479,698],[479,658],[475,620],[475,585],[485,550],[500,525],[525,502],[552,485],[585,478],[620,478],[660,478],[700,478],[740,478],[780,478],[780,345],[740,345],[700,345],[660,345],[620,345],[580,345],[540,345],[500,345],[460,362]]
    green2Pos = [[760,40],[red1Pos[18][0], red1Pos[18][1] + 25],[red1Pos[19][0] - 2, red1Pos[19][1] + 25],[red1Pos[20][0] - 6, red1Pos[20][1] + 18],[red1Pos[21][0] - 11, red1Pos[21][1] + 16],[red1Pos[22][0] - 14, red1Pos[22][1] + 14],[red1Pos[23][0] - 18, red1Pos[23][1] + 8],[red1Pos[24][0] - 20, red1Pos[24][1] + 3],[red1Pos[25][0] - 30, red1Pos[25][1]],[red1Pos[26][0] - 30, red1Pos[26][1]],[red1Pos[27][0] - 30, red1Pos[27][1]],[red1Pos[28][0] - 30, red1Pos[28][1]],[red1Pos[29][0] - 30, red1Pos[29][1]],[red1Pos[30][0] - 30, red1Pos[30][1]],[red1Pos[31][0] - 30, red1Pos[31][1]],[red1Pos[32][0] - 30, red1Pos[32][1]],[red1Pos[33][0] - 30, red1Pos[33][1]],[red1Pos[34][0] - 30, red1Pos[34][1]],[red1Pos[35][0] - 30, red1Pos[35][1]],[red1Pos[36][0] - 20, red1Pos[36][1] - 3],[red1Pos[37][0] - 18, red1Pos[37][1] - 7],[red1Pos[38][0] - 16, red1Pos[38][1] - 11],[red1Pos[39][0] - 14, red1Pos[39][1] - 15],[red1Pos[40][0] - 8, red1Pos[40][1] - 20],[red1Pos[41][0] - 3, red1Pos[41][1] - 20],[red1Pos[42][0], red1Pos[42][1] - 25],[red1Pos[43][0], red1Pos[43][1] - 25],[red1Pos[44][0], red1Pos[44][1] - 25],[red1Pos[45][0], red1Pos[45][1] - 25],[red1Pos[46][0], red1Pos[46][1] - 25],[red1Pos[47][0], red1Pos[47][1] - 25],[red1Pos[48][0], red1Pos[48][1] - 25],[red1Pos[49][0], red1Pos[49][1] - 25],[red1Pos[50][0], red1Pos[50][1] - 25],[red1Pos[51][0], red1Pos[51][1] - 25],[red1Pos[52][0], red1Pos[52][1] - 20],[red1Pos[53][0] + 2, red1Pos[53][1] - 20],[red1Pos[54][0] + 7, red1Pos[54][1] - 18],[red1Pos[55][0] + 12, red1Pos[55][1] - 16],[red1Pos[56][0] + 18, red1Pos[56][1] - 14],[red1Pos[57][0] + 20, red1Pos[57][1] - 9],[red1Pos[58][0] + 20, red1Pos[58][1] - 3],[red1Pos[59][0] + 25, red1Pos[59][1]],[red1Pos[60][0] + 25, red1Pos[60][1]],[red1Pos[61][0] + 25, red1Pos[61][1]],[red1Pos[62][0] + 25, red1Pos[62][1]],[red1Pos[63][0] + 25, red1Pos[63][1]],[red1Pos[64][0] + 25, red1Pos[64][1]],[green1Pos[48][0] + 25, green1Pos[48][1]],[green1Pos[49][0] + 25, green1Pos[49][1]],[green1Pos[50][0] + 25, green1Pos[50][1]],[green1Pos[51][0] + 25, green1Pos[51][1]],[red1Pos[1][0] + 25, red1Pos[1][1]],[red1Pos[2][0] + 20, red1Pos[2][1]],[red1Pos[3][0] + 20, red1Pos[3][1] + 12],[red1Pos[4][0] + 15, red1Pos[4][1] + 14],[red1Pos[5][0] + 12, red1Pos[5][1] + 18],[red1Pos[6][0] + 10, red1Pos[6][1] + 20],[red1Pos[7][0] + 2, red1Pos[7][1] + 20],[red1Pos[8][0], red1Pos[8][1] + 25],[red1Pos[9][0], red1Pos[9][1] + 25],[red1Pos[10][0], red1Pos[10][1] + 25],[red1Pos[11][0], red1Pos[11][1] + 25],[red1Pos[12][0], red1Pos[12][1] + 25],[red1Pos[13][0], red1Pos[13][1] + 25],[green1Pos[65][0], green1Pos[65][1] + 25],[green1Pos[66][0], green1Pos[66][1] + 25],[green1Pos[67][0], green1Pos[67][1] + 25],[green1Pos[68][0], green1Pos[68][1] + 25],[green1Pos[69][0], green1Pos[69][1] + 25],[green1Pos[70][0], green1Pos[70][1] + 25],[green1Pos[71][0], green1Pos[71][1] + 25],[green1Pos[72][0], green1Pos[72][1] + 25]]
    green3Pos = [[640,160],[red2Pos[18][0], red2Pos[18][1] + 25],[red2Pos[19][0] - 2, red2Pos[19][1] + 25],[red2Pos[20][0] - 6, red2Pos[20][1] + 18],[red2Pos[21][0] - 11, red2Pos[21][1] + 16],[red2Pos[22][0] - 15, red2Pos[22][1] + 14],[red2Pos[23][0] - 18, red2Pos[23][1] + 8],[red2Pos[24][0] - 20, red2Pos[24][1] + 3],[red2Pos[25][0] - 30, red2Pos[25][1]],[red2Pos[26][0] - 30, red2Pos[26][1]],[red2Pos[27][0] - 30, red2Pos[27][1]],[red2Pos[28][0] - 30, red2Pos[28][1]],[red2Pos[29][0] - 30, red2Pos[29][1]],[red2Pos[30][0] - 30, red2Pos[30][1]],[red2Pos[31][0] - 30, red2Pos[31][1]],[red2Pos[32][0] - 30, red2Pos[32][1]],[red2Pos[33][0] - 30, red2Pos[33][1]],[red2Pos[34][0] - 30, red2Pos[34][1]],[red2Pos[35][0] - 30, red2Pos[35][1]],[red2Pos[36][0] - 20, red2Pos[36][1] - 3],[red2Pos[37][0] - 18, red2Pos[37][1] - 7],[red2Pos[38][0] - 16, red2Pos[38][1] - 11],[red2Pos[39][0] - 14, red2Pos[39][1] - 15],[red2Pos[40][0] - 8, red2Pos[40][1] - 20],[red2Pos[41][0] - 3, red2Pos[41][1] - 20],[red2Pos[42][0], red2Pos[42][1] - 25],[red2Pos[43][0], red2Pos[43][1] - 25],[red2Pos[44][0], red2Pos[44][1] - 25],[red2Pos[45][0], red2Pos[45][1] - 25],[red2Pos[46][0], red2Pos[46][1] - 25],[red2Pos[47][0], red2Pos[47][1] - 25],[red2Pos[48][0], red2Pos[48][1] - 25],[red2Pos[49][0], red2Pos[49][1] - 25],[red2Pos[50][0], red2Pos[50][1] - 25],[red2Pos[51][0], red2Pos[51][1] - 25],[red2Pos[52][0], red2Pos[52][1] - 20],[red2Pos[53][0] + 2, red2Pos[53][1] - 20],[red2Pos[54][0] + 7, red2Pos[54][1] - 18],[red2Pos[55][0] + 12, red2Pos[55][1] - 16],[red2Pos[56][0] + 18, red2Pos[56][1] - 14],[red2Pos[57][0]+ 20, red2Pos[57][1] - 9],[red2Pos[58][0] + 20, red2Pos[58][1] - 3],[red2Pos[59][0] + 25, red2Pos[59][1]],[red2Pos[60][0] + 25, red2Pos[60][1]],[red2Pos[61][0] + 25, red2Pos[61][1]],[red2Pos[62][0] + 25, red2Pos[62][1]],[red2Pos[63][0] + 25, red2Pos[63][1]],[red2Pos[64][0] + 25, red2Pos[64][1]],[green2Pos[48][0] + 25, green2Pos[48][1]],[green2Pos[49][0] + 25, green2Pos[49][1]],[green2Pos[50][0] + 25, green2Pos[50][1]],[green2Pos[51][0] + 25, green2Pos[51][1]],[red2Pos[1][0] + 25, red2Pos[1][1]],[red2Pos[2][0] + 20, red2Pos[2][1] + 2],[red2Pos[3][0] + 20, red2Pos[3][1] + 8],[red2Pos[4][0] + 20, red2Pos[4][1] + 12],[red2Pos[5][0] + 14, red2Pos[5][1] + 16],[red2Pos[6][0] + 8, red2Pos[6][1] + 20],[red2Pos[7][0] + 2, red2Pos[7][1] + 20],[red2Pos[8][0], red2Pos[8][1] + 25],[red2Pos[9][0], red2Pos[9][1] + 25],[red2Pos[10][0], red2Pos[10][1] + 25],[red2Pos[11][0], red2Pos[11][1] + 25],[red2Pos[12][0], red2Pos[12][1] + 25],[red2Pos[13][0], red2Pos[13][1] + 25],[green2Pos[65][0], green2Pos[65][1] + 25],[green2Pos[66][0], green2Pos[66][1] + 25],[green2Pos[67][0], green2Pos[67][1] + 25],[green2Pos[68][0], green2Pos[68][1] + 25],[green2Pos[69][0], green2Pos[69][1] + 25],[green2Pos[70][0], green2Pos[70][1] + 25],[green2Pos[71][0], green2Pos[71][1] + 25],[green2Pos[72][0], green2Pos[72][1] + 25]]
    green4Pos = [[760,160],[red3Pos[18][0], red3Pos[18][1] + 25],[red3Pos[19][0] - 2 , red3Pos[19][1] + 25],[red3Pos[20][0] - 6, red3Pos[20][1] + 18],[red3Pos[21][0] - 11, red3Pos[21][1] + 16],[red3Pos[22][0] - 15, red3Pos[22][1] + 14],[red3Pos[23][0] - 18, red3Pos[23][1] + 8],[red3Pos[24][0] - 20, red3Pos[24][1] + 3],[red3Pos[25][0] - 30, red3Pos[25][1]],[red3Pos[26][0] - 30, red3Pos[26][1]],[red3Pos[27][0] - 30, red3Pos[27][1]],[red3Pos[28][0] - 30, red3Pos[28][1]],[red3Pos[29][0] - 30, red3Pos[29][1]],[red3Pos[30][0] - 30, red3Pos[30][1]],[red3Pos[31][0] - 30, red3Pos[31][1]],[red3Pos[32][0] - 30, red3Pos[32][1]],[red3Pos[33][0] - 30, red3Pos[33][1]],[red3Pos[34][0] - 30, red3Pos[34][1]],[red3Pos[35][0] - 30, red3Pos[35][1]],[red3Pos[36][0] - 20, red3Pos[36][1] - 3],[red3Pos[37][0] - 18, red3Pos[37][1] - 7],[red3Pos[38][0] - 16, red3Pos[38][1] - 11],[red3Pos[39][0] - 14, red3Pos[39][1] - 15],[red3Pos[40][0] - 8, red3Pos[40][1] - 20],[red3Pos[41][0] - 3, red3Pos[41][1] - 20],[red3Pos[42][0], red3Pos[42][1] - 25],[red3Pos[43][0], red3Pos[43][1] - 25],[red3Pos[44][0], red3Pos[44][1] - 25],[red3Pos[45][0], red3Pos[45][1] - 25],[red3Pos[46][0], red3Pos[46][1] - 25],[red3Pos[47][0], red3Pos[47][1] - 25],[red3Pos[48][0], red3Pos[48][1] - 25],[red3Pos[49][0], red3Pos[49][1] - 25],[red3Pos[50][0], red3Pos[50][1] - 25],[red3Pos[51][0], red3Pos[51][1] - 25],[red3Pos[52][0], red3Pos[52][1] - 20],[red3Pos[53][0] + 2, red3Pos[53][1] - 20],[red3Pos[54][0] + 7, red3Pos[54][1] - 18],[red3Pos[55][0] + 12, red3Pos[55][1] - 16],[red3Pos[56][0] + 18, red3Pos[56][1] - 14],[red3Pos[57][0] + 20, red3Pos[57][1] - 9],[red3Pos[58][0] + 20, red3Pos[58][1] - 3],[red3Pos[59][0] + 25, red3Pos[59][1]],[red3Pos[60][0] + 25, red3Pos[60][1]],[red3Pos[61][0] + 25, red3Pos[61][1]],[red3Pos[62][0] + 25, red3Pos[62][1]],[red3Pos[63][0] + 25, red3Pos[63][1]],[red3Pos[64][0] + 25, red3Pos[64][1]],[green3Pos[48][0] + 25, green3Pos[48][1]],[green3Pos[49][0] + 25, green3Pos[49][1]],[green3Pos[50][0] + 25, green3Pos[50][1]],[green3Pos[51][0] + 25, green3Pos[51][1]],[red3Pos[1][0] + 25, red3Pos[1][1]],[red3Pos[2][0] + 20, red3Pos[2][1] + 2],[red3Pos[3][0] + 20, red3Pos[3][1] + 8],[red3Pos[4][0] + 20, red3Pos[4][1] + 14],[red3Pos[5][0] + 14, red3Pos[5][1] + 16],[red3Pos[6][0] + 8, red3Pos[6][1] + 20],[red3Pos[7][0] + 2, red3Pos[7][1] + 20],[red3Pos[8][0], red3Pos[8][1] + 25],[red3Pos[9][0], red3Pos[9][1] + 25],[red3Pos[10][0], red3Pos[10][1] + 25],[red3Pos[11][0], red3Pos[11][1] + 25],[red3Pos[12][0], red3Pos[12][1] + 25],[red3Pos[13][0], red3Pos[13][1] + 25],[green3Pos[65][0], green3Pos[65][1] + 25],[green3Pos[66][0], green3Pos[66][1] + 25],[green3Pos[67][0], green3Pos[67][1] + 25],[green3Pos[68][0], green3Pos[68][1] + 25],[green3Pos[69][0], green3Pos[69][1] + 25],[green3Pos[70][0], green3Pos[70][1] + 25],[green3Pos[71][0], green3Pos[71][1] + 25],[green3Pos[72][0], green3Pos[72][1] + 25]]
          
    if num == 1:
        return green1Pos
    if num == 2:
        return green2Pos
    if num == 3:
        return green3Pos
    if num == 4:
        return green4Pos

def blue(num):
    red1Pos = red(1)
    red2Pos = red(2)
    red3Pos = red(3)
    green1Pos = green(1)
    green2Pos = green(2)
    green3Pos = green(3)
    blue1Pos = [[40,40],[322,180],[322,220],[315,247],[300,272],[276,292],[247,312],[218,320],[180,322],[140,322],[100,322],[60,322],[20,322],[20,456],[20,589],[60,589],[100,589],[140,589],[180,589],[207,545],[222,545],[234,555],[240,570],[250,580],[257,592],[212,618],[212,658],[212,698],[212,738],[212,778],[345,778],[479,778],[479,738],[479,698],[479,658],[475,620],[475,585],[485,550],[500,525],[525,502],[552,485],[585,478],[620,478],[660,478],[700,478],[740,478],[780,478],[780,345],[780,210],[740,210],[700,210],[660,210],[620,210],[594,250],[580,248],[565,245],[550,238],[545,223],[543,208],[590,180],[590,140],[590,100],[590,60],[590,20],[457,20],[457,60],[457,100],[457,140],[457,180],[457,220],[457,260],[457,300],[437,340]]
    blue2Pos = [[160,40],[red1Pos[35][0] - 30, red1Pos[35][1]],[red1Pos[36][0] - 20, red1Pos[36][1] - 3],[red1Pos[37][0] - 18, red1Pos[37][1] - 7],[red1Pos[38][0] - 16, red1Pos[38][1] - 11],[red1Pos[39][0] - 14, red1Pos[39][1] - 15],[red1Pos[40][0] - 8, red1Pos[40][1] - 20],[red1Pos[41][0] - 3, red1Pos[41][1] - 20],[red1Pos[42][0], red1Pos[42][1] - 25],[red1Pos[43][0], red1Pos[43][1] - 25],[red1Pos[44][0], red1Pos[44][1] - 25],[red1Pos[45][0], red1Pos[45][1] - 25],[red1Pos[46][0], red1Pos[46][1] - 25],[red1Pos[47][0], red1Pos[47][1] - 25],[red1Pos[48][0], red1Pos[48][1] - 25],[red1Pos[49][0], red1Pos[49][1] - 25],[red1Pos[50][0], red1Pos[50][1] - 25],[red1Pos[51][0], red1Pos[51][1] - 25],[red1Pos[52][0], red1Pos[52][1] - 20],[red1Pos[53][0] + 2, red1Pos[53][1] - 20],[red1Pos[54][0] + 7, red1Pos[54][1] - 18],[red1Pos[55][0] + 12, red1Pos[55][1] - 16],[red1Pos[56][0] + 18, red1Pos[56][1] - 14],[red1Pos[57][0] + 20, red1Pos[57][1] - 9],[red1Pos[58][0] + 20, red1Pos[58][1] - 3],[red1Pos[59][0] + 25, red1Pos[59][1]],[red1Pos[60][0] + 25, red1Pos[60][1]],[red1Pos[61][0] + 25, red1Pos[61][1]],[red1Pos[62][0] + 25, red1Pos[62][1]],[red1Pos[63][0] + 25, red1Pos[63][1]],[red1Pos[64][0] + 25, red1Pos[64][1]],[green1Pos[48][0] + 25, green1Pos[48][1]],[green1Pos[49][0] + 25, green1Pos[49][1]],[green1Pos[50][0] + 25, green1Pos[50][1]],[green1Pos[51][0] + 25, green1Pos[51][1]],[red1Pos[1][0] + 25, red1Pos[1][1]],[red1Pos[2][0] + 20, red1Pos[2][1]],[red1Pos[3][0] + 20, red1Pos[3][1] + 12],[red1Pos[4][0] + 15, red1Pos[4][1] + 14],[red1Pos[5][0] + 12, red1Pos[5][1] + 18],[red1Pos[6][0] + 10, red1Pos[6][1] + 20],[red1Pos[7][0] + 2, red1Pos[7][1] + 20],[red1Pos[8][0], red1Pos[8][1] + 25],[red1Pos[9][0], red1Pos[9][1] + 25],[red1Pos[10][0], red1Pos[10][1] + 25],[red1Pos[11][0], red1Pos[11][1] + 25],[red1Pos[12][0], red1Pos[12][1] + 25],[red1Pos[13][0], red1Pos[13][1] + 25],[red1Pos[14][0], red1Pos[14][1] + 25],[red1Pos[15][0], red1Pos[15][1] + 25],[red1Pos[16][0], red1Pos[16][1] + 25],[red1Pos[17][0], red1Pos[17][1] + 25],[red1Pos[18][0], red1Pos[18][1] + 25],[red1Pos[19][0] - 2, red1Pos[19][1] + 25],[red1Pos[20][0] - 6, red1Pos[20][1] + 18],[red1Pos[21][0] - 11, red1Pos[21][1] + 16],[red1Pos[22][0] - 14, red1Pos[22][1] + 14],[red1Pos[23][0] - 18, red1Pos[23][1] + 8],[red1Pos[24][0] - 20, red1Pos[24][1] + 3],[red1Pos[25][0] - 30, red1Pos[25][1]],[red1Pos[26][0] - 30, red1Pos[26][1]],[red1Pos[27][0] - 30, red1Pos[27][1]],[red1Pos[28][0] - 30, red1Pos[28][1]],[red1Pos[29][0] - 30, red1Pos[29][1]],[red1Pos[30][0] - 30, red1Pos[30][1]],[blue1Pos[65][0] - 30,blue1Pos[65][1]],[blue1Pos[66][0] - 30,blue1Pos[66][1]],[blue1Pos[67][0] - 30,blue1Pos[67][1]],[blue1Pos[68][0] - 30,blue1Pos[68][1]],[blue1Pos[69][0] - 30,blue1Pos[69][1]],[blue1Pos[70][0] - 30,blue1Pos[70][1]],[blue1Pos[71][0] - 30,blue1Pos[71][1]],[blue1Pos[72][0] - 25,blue1Pos[72][1]]]
    blue3Pos = [[40,160],[red2Pos[35][0] - 30, red2Pos[35][1]],[red2Pos[36][0] - 20, red2Pos[36][1] - 3],[red2Pos[37][0] - 18, red2Pos[37][1] - 7],[red2Pos[38][0] - 16, red2Pos[38][1] - 11],[red2Pos[39][0] - 14, red2Pos[39][1] - 15],[red2Pos[40][0] - 8, red2Pos[40][1] - 20],[red2Pos[41][0] - 3, red2Pos[41][1] - 20],[red2Pos[42][0], red2Pos[42][1] - 25],[red2Pos[43][0], red2Pos[43][1] - 25],[red2Pos[44][0], red2Pos[44][1] - 25],[red2Pos[45][0], red2Pos[45][1] - 25],[red2Pos[46][0], red2Pos[46][1] - 25],[red2Pos[47][0], red2Pos[47][1] - 25],[red2Pos[48][0], red2Pos[48][1] - 25],[red2Pos[49][0], red2Pos[49][1] - 25],[red2Pos[50][0], red2Pos[50][1] - 25],[red2Pos[51][0], red2Pos[51][1] - 25],[red2Pos[52][0], red2Pos[52][1] - 20],[red2Pos[53][0] + 2, red2Pos[53][1] - 20],[red2Pos[54][0] + 7, red2Pos[54][1] - 18],[red2Pos[55][0] + 12, red2Pos[55][1] - 16],[red2Pos[56][0] + 18, red2Pos[56][1] - 14],[red2Pos[57][0]+ 20, red2Pos[57][1] - 9],[red2Pos[58][0] + 20, red2Pos[58][1] - 3],[red2Pos[59][0] + 25, red2Pos[59][1]],[red2Pos[60][0] + 25, red2Pos[60][1]],[red2Pos[61][0] + 25, red2Pos[61][1]],[red2Pos[62][0] + 25, red2Pos[62][1]],[red2Pos[63][0] + 25, red2Pos[63][1]],[red2Pos[64][0] + 25, red2Pos[64][1]],[green2Pos[48][0] + 25, green2Pos[48][1]],[green2Pos[49][0] + 25, green2Pos[49][1]],[green2Pos[50][0] + 25, green2Pos[50][1]],[green2Pos[51][0] + 25, green2Pos[51][1]],[red2Pos[1][0] + 25, red2Pos[1][1]],[red2Pos[2][0] + 20, red2Pos[2][1] + 2],[red2Pos[3][0] + 20, red2Pos[3][1] + 8],[red2Pos[4][0] + 20, red2Pos[4][1] + 12],[red2Pos[5][0] + 14, red2Pos[5][1] + 16],[red2Pos[6][0] + 8, red2Pos[6][1] + 20],[red2Pos[7][0] + 2, red2Pos[7][1] + 20],[red2Pos[8][0], red2Pos[8][1] + 25],[red2Pos[9][0], red2Pos[9][1] + 25],[red2Pos[10][0], red2Pos[10][1] + 25],[red2Pos[11][0], red2Pos[11][1] + 25],[red2Pos[12][0], red2Pos[12][1] + 25],[red2Pos[13][0], red2Pos[13][1] + 25],[red2Pos[14][0], red2Pos[14][1] + 25],[red2Pos[15][0], red2Pos[15][1] + 25],[red2Pos[16][0], red2Pos[16][1] + 25],[red2Pos[17][0], red2Pos[17][1] + 25],[red2Pos[18][0], red2Pos[18][1] + 25],[red2Pos[19][0] - 2, red2Pos[19][1] + 25],[red2Pos[20][0] - 6, red2Pos[20][1] + 18],[red2Pos[21][0] - 11, red2Pos[21][1] + 16],[red2Pos[22][0] - 15, red2Pos[22][1] + 14],[red2Pos[23][0] - 18, red2Pos[23][1] + 8],[red2Pos[24][0] - 20, red2Pos[24][1] + 3],[red2Pos[25][0] - 30, red2Pos[25][1]],[red2Pos[26][0] - 30, red2Pos[26][1]],[red2Pos[27][0] - 30, red2Pos[27][1]],[red2Pos[28][0] - 30, red2Pos[28][1]],[red2Pos[29][0] - 30, red2Pos[29][1]],[red2Pos[30][0] - 30, red2Pos[30][1]],[blue2Pos[65][0] - 30, blue2Pos[65][1]],[blue2Pos[66][0] - 30, blue2Pos[66][1]],[blue2Pos[67][0] - 30, blue2Pos[67][1]],[blue2Pos[68][0] - 30, blue2Pos[68][1]],[blue2Pos[69][0] - 30, blue2Pos[69][1]],[blue2Pos[70][0] - 30, blue2Pos[70][1]],[blue2Pos[71][0] - 30, blue2Pos[71][1]],[blue2Pos[72][0] - 25, blue2Pos[72][1]]]
    blue4Pos = [[160,160],[red3Pos[35][0] - 30, red3Pos[35][1]],[red3Pos[36][0] - 20, red3Pos[36][1] - 3],[red3Pos[37][0] - 18, red3Pos[37][1] - 7],[red3Pos[38][0] - 16, red3Pos[38][1] - 11],[red3Pos[39][0] - 14, red3Pos[39][1] - 15],[red3Pos[40][0] - 8, red3Pos[40][1] - 20],[red3Pos[41][0] - 3, red3Pos[41][1] - 20],[red3Pos[42][0], red3Pos[42][1] - 25],[red3Pos[43][0], red3Pos[43][1] - 25],[red3Pos[44][0], red3Pos[44][1] - 25],[red3Pos[45][0], red3Pos[45][1] - 25],[red3Pos[46][0], red3Pos[46][1] - 25],[red3Pos[47][0], red3Pos[47][1] - 25],[red3Pos[48][0], red3Pos[48][1] - 25],[red3Pos[49][0], red3Pos[49][1] - 25],[red3Pos[50][0], red3Pos[50][1] - 25],[red3Pos[51][0], red3Pos[51][1] - 25],[red3Pos[52][0], red3Pos[52][1] - 20],[red3Pos[53][0] + 2, red3Pos[53][1] - 20],[red3Pos[54][0] + 7, red3Pos[54][1] - 18],[red3Pos[55][0] + 12, red3Pos[55][1] - 16],[red3Pos[56][0] + 18, red3Pos[56][1] - 14],[red3Pos[57][0] + 20, red3Pos[57][1] - 9],[red3Pos[58][0] + 20, red3Pos[58][1] - 3],[red3Pos[59][0] + 25, red3Pos[59][1]],[red3Pos[60][0] + 25, red3Pos[60][1]],[red3Pos[61][0] + 25, red3Pos[61][1]],[red3Pos[62][0] + 25, red3Pos[62][1]],[red3Pos[63][0] + 25, red3Pos[63][1]],[red3Pos[64][0] + 25, red3Pos[64][1]],[green3Pos[48][0] + 25, green3Pos[48][1]],[green3Pos[49][0] + 25, green3Pos[49][1]],[green3Pos[50][0] + 25, green3Pos[50][1]],[green3Pos[51][0] + 25, green3Pos[51][1]],[red3Pos[1][0] + 25, red3Pos[1][1]],[red3Pos[2][0] + 20, red3Pos[2][1] + 2],[red3Pos[3][0] + 20, red3Pos[3][1] + 8],[red3Pos[4][0] + 20, red3Pos[4][1] + 14],[red3Pos[5][0] + 14, red3Pos[5][1] + 16],[red3Pos[6][0] + 8, red3Pos[6][1] + 20],[red3Pos[7][0] + 2, red3Pos[7][1] + 20],[red3Pos[8][0], red3Pos[8][1] + 25],[red3Pos[9][0], red3Pos[9][1] + 25],[red3Pos[10][0], red3Pos[10][1] + 25],[red3Pos[11][0], red3Pos[11][1] + 25],[red3Pos[12][0], red3Pos[12][1] + 25],[red3Pos[13][0], red3Pos[13][1] + 25],[red3Pos[14][0], red3Pos[14][1] + 25],[red3Pos[15][0], red3Pos[15][1] + 25],[red3Pos[16][0], red3Pos[16][1] + 25],[red3Pos[17][0], red3Pos[17][1] + 25],[red3Pos[18][0], red3Pos[18][1] + 25],[red3Pos[19][0] - 2 , red3Pos[19][1] + 25],[red3Pos[20][0] - 6, red3Pos[20][1] + 18],[red3Pos[21][0] - 11, red3Pos[21][1] + 16],[red3Pos[22][0] - 15, red3Pos[22][1] + 14],[red3Pos[23][0] - 18, red3Pos[23][1] + 8],[red3Pos[24][0] - 20, red3Pos[24][1] + 3],[red3Pos[25][0] - 30, red3Pos[25][1]],[red3Pos[26][0] - 30, red3Pos[26][1]],[red3Pos[27][0] - 30, red3Pos[27][1]],[red3Pos[28][0] - 30, red3Pos[28][1]],[red3Pos[29][0] - 30, red3Pos[29][1]],[red3Pos[30][0] - 30, red3Pos[30][1]],[blue3Pos[65][0] - 30, blue3Pos[65][1]],[blue3Pos[66][0] - 30, blue3Pos[66][1]],[blue3Pos[67][0] - 30, blue3Pos[67][1]],[blue3Pos[68][0] - 30, blue3Pos[68][1]],[blue3Pos[69][0] - 30, blue3Pos[69][1]],[blue3Pos[70][0] - 30, blue3Pos[70][1]],[blue3Pos[71][0] - 30, blue3Pos[71][1]],[blue3Pos[72][0] - 25, blue3Pos[72][1]]]
    
    if num == 1:
        return blue1Pos
    if num == 2:
        return blue2Pos
    if num == 3:
        return blue3Pos
    if num == 4:
        return blue4Pos

def yellow(num):
    red1Pos = red(1)
    red2Pos = red(2)
    red3Pos = red(3)
    green1Pos = green(1)
    green2Pos = green(2)
    green3Pos = green(3)
    yellow1Pos = [[40,640],[180,589],[207,545],[222,545],[234,555],[240,570],[250,580],[257,592],[212,618],[212,658],[212,698],[212,738],[212,778],[345,778],[479,778],[479,738],[479,698],[479,658],[475,620],[475,585],[485,550],[500,525],[525,502],[552,485],[585,478],[620,478],[660,478],[700,478],[740,478],[780,478],[780,345],[780,210],[740,210],[700,210],[660,210],[620,210],[594,250],[580,248],[565,245],[550,238],[545,223],[543,208],[590,180],[590,140],[590,100],[590,60],[590,20],[457,20],[322,20],[322,60],[322,100],[322,140],[322,180],[322,220],[315,247],[300,272],[276,292],[247,312],[218,320],[180,322],[140,322],[100,322],[60,322],[20,322],[20,456],[60,456],[100,456],[140,456],[180,456],[220,456],[260,456],[300,456],[340,436]]
    yellow2Pos = [[160,640],[red1Pos[52][0], red1Pos[52][1] - 25],[red1Pos[53][0] + 2, red1Pos[53][1] - 20],[red1Pos[54][0] + 7, red1Pos[54][1] - 18],[red1Pos[55][0] + 12, red1Pos[55][1] - 16],[red1Pos[56][0] + 18, red1Pos[56][1] - 14],[red1Pos[57][0] + 20, red1Pos[57][1] - 9],[red1Pos[58][0] + 20, red1Pos[58][1] - 3],[red1Pos[59][0] + 25, red1Pos[59][1]],[red1Pos[60][0] + 25, red1Pos[60][1]],[red1Pos[61][0] + 25, red1Pos[61][1]],[red1Pos[62][0] + 25, red1Pos[62][1]],[red1Pos[63][0] + 25, red1Pos[63][1]],[red1Pos[64][0] + 25, red1Pos[64][1]],[green1Pos[48][0] + 25, green1Pos[48][1]],[green1Pos[49][0] + 25, green1Pos[49][1]],[green1Pos[50][0] + 25, green1Pos[50][1]],[green1Pos[51][0] + 25, green1Pos[51][1]],[red1Pos[1][0] + 25, red1Pos[1][1]],[red1Pos[2][0] + 20, red1Pos[2][1] + 2],[red1Pos[3][0] + 20, red1Pos[3][1] + 12],[red1Pos[4][0] + 15, red1Pos[4][1] + 14],[red1Pos[5][0] + 12, red1Pos[5][1] + 18],[red1Pos[6][0] + 10, red1Pos[6][1] + 20],[red1Pos[7][0] + 2, red1Pos[7][1] + 20],[red1Pos[8][0], red1Pos[8][1] + 25],[red1Pos[9][0], red1Pos[9][1] + 25],[red1Pos[10][0], red1Pos[10][1] + 25],[red1Pos[11][0], red1Pos[11][1] + 25],[red1Pos[12][0], red1Pos[12][1] + 25],[red1Pos[13][0], red1Pos[13][1] + 25],[red1Pos[14][0], red1Pos[14][1] + 25],[red1Pos[15][0], red1Pos[15][1] + 25],[red1Pos[16][0], red1Pos[16][1] + 25],[red1Pos[17][0], red1Pos[17][1] + 25],[red1Pos[18][0], red1Pos[18][1] + 25],[red1Pos[19][0] - 2, red1Pos[19][1] + 25],[red1Pos[20][0] - 6, red1Pos[20][1] + 18],[red1Pos[21][0] - 11, red1Pos[21][1] + 16],[red1Pos[22][0] - 14, red1Pos[22][1] + 14],[red1Pos[23][0] - 18, red1Pos[23][1] + 8],[red1Pos[24][0] - 20, red1Pos[24][1] + 3],[red1Pos[25][0] - 30, red1Pos[25][1]],[red1Pos[26][0] - 30, red1Pos[26][1]],[red1Pos[27][0] - 30, red1Pos[27][1]],[red1Pos[28][0] - 30, red1Pos[28][1]],[red1Pos[29][0] - 30, red1Pos[29][1]],[red1Pos[30][0] - 30, red1Pos[30][1]],[red1Pos[31][0] - 30, red1Pos[31][1]],[red1Pos[32][0] - 30, red1Pos[32][1]],[red1Pos[33][0] - 30, red1Pos[33][1]],[red1Pos[34][0] - 30, red1Pos[34][1]],[red1Pos[35][0] - 30, red1Pos[35][1]],[red1Pos[36][0] - 20, red1Pos[36][1] - 3],[red1Pos[37][0] - 18, red1Pos[37][1] - 7],[red1Pos[38][0] - 16, red1Pos[38][1] - 11],[red1Pos[39][0] - 14, red1Pos[39][1] - 15],[red1Pos[40][0] - 8, red1Pos[40][1] - 20],[red1Pos[41][0] - 3, red1Pos[41][1] - 20],[red1Pos[42][0], red1Pos[42][1] - 25],[red1Pos[43][0], red1Pos[43][1] - 25],[red1Pos[44][0], red1Pos[44][1] - 25],[red1Pos[45][0], red1Pos[45][1] - 25],[red1Pos[46][0], red1Pos[46][1] - 25],[red1Pos[47][0], red1Pos[47][1] - 25],[yellow1Pos[65][0],yellow1Pos[65][1] - 25],[yellow1Pos[66][0],yellow1Pos[66][1] - 25],[yellow1Pos[67][0],yellow1Pos[67][1] - 25],[yellow1Pos[68][0],yellow1Pos[68][1] - 25],[yellow1Pos[69][0],yellow1Pos[69][1] - 25],[yellow1Pos[70][0],yellow1Pos[70][1] - 25],[yellow1Pos[71][0],yellow1Pos[71][1] - 25],[yellow1Pos[72][0],yellow1Pos[72][1] - 25]]
    yellow3Pos = [[40,760],[red2Pos[52][0], red2Pos[52][1] - 25],[red2Pos[53][0] + 2, red2Pos[53][1] - 20],[red2Pos[54][0] + 7, red2Pos[54][1] - 18],[red2Pos[55][0] + 12, red2Pos[55][1] - 16],[red2Pos[56][0] + 18, red2Pos[56][1] - 14],[red2Pos[57][0]+ 20, red2Pos[57][1] - 9],[red2Pos[58][0] + 20, red2Pos[58][1] - 3],[red2Pos[59][0] + 25, red2Pos[59][1]],[red2Pos[60][0] + 25, red2Pos[60][1]],[red2Pos[61][0] + 25, red2Pos[61][1]],[red2Pos[62][0] + 25, red2Pos[62][1]],[red2Pos[63][0] + 25, red2Pos[63][1]],[red2Pos[64][0] + 25, red2Pos[64][1]],[green2Pos[48][0] + 25, green2Pos[48][1]],[green2Pos[49][0] + 25, green2Pos[49][1]],[green2Pos[50][0] + 25, green2Pos[50][1]],[green2Pos[51][0] + 25, green2Pos[51][1]],[red2Pos[1][0] + 25, red2Pos[1][1]],[red2Pos[2][0] + 20, red2Pos[2][1] + 2],[red2Pos[3][0] + 20, red2Pos[3][1] + 8],[red2Pos[4][0] + 20, red2Pos[4][1] + 12],[red2Pos[5][0] + 14, red2Pos[5][1] + 16],[red2Pos[6][0] + 8, red2Pos[6][1] + 20],[red2Pos[7][0] + 2, red2Pos[7][1] + 20],[red2Pos[8][0], red2Pos[8][1] + 25],[red2Pos[9][0], red2Pos[9][1] + 25],[red2Pos[10][0], red2Pos[10][1] + 25],[red2Pos[11][0], red2Pos[11][1] + 25],[red2Pos[12][0], red2Pos[12][1] + 25],[red2Pos[13][0], red2Pos[13][1] + 25],[red2Pos[14][0], red2Pos[14][1] + 25],[red2Pos[15][0], red2Pos[15][1] + 25],[red2Pos[16][0], red2Pos[16][1] + 25],[red2Pos[17][0], red2Pos[17][1] + 25],[red2Pos[18][0], red2Pos[18][1] + 25],[red2Pos[19][0] - 2, red2Pos[19][1] + 25],[red2Pos[20][0] - 6, red2Pos[20][1] + 18],[red2Pos[21][0] - 11, red2Pos[21][1] + 16],[red2Pos[22][0] - 15, red2Pos[22][1] + 14],[red2Pos[23][0] - 18, red2Pos[23][1] + 8],[red2Pos[24][0] - 20, red2Pos[24][1] + 3],[red2Pos[25][0] - 30, red2Pos[25][1]],[red2Pos[26][0] - 30, red2Pos[26][1]],[red2Pos[27][0] - 30, red2Pos[27][1]],[red2Pos[28][0] - 30, red2Pos[28][1]],[red2Pos[29][0] - 30, red2Pos[29][1]],[red2Pos[30][0] - 30, red2Pos[30][1]],[red2Pos[31][0] - 30, red2Pos[31][1]],[red2Pos[32][0] - 30, red2Pos[32][1]],[red2Pos[33][0] - 30, red2Pos[33][1]],[red2Pos[34][0] - 30, red2Pos[34][1]],[red2Pos[35][0] - 30, red2Pos[35][1]],[red2Pos[36][0] - 20, red2Pos[36][1] - 3],[red2Pos[37][0] - 18, red2Pos[37][1] - 7],[red2Pos[38][0] - 16, red2Pos[38][1] - 11],[red2Pos[39][0] - 14, red2Pos[39][1] - 15],[red2Pos[40][0] - 8, red2Pos[40][1] - 20],[red2Pos[41][0] - 3, red2Pos[41][1] - 20],[red2Pos[42][0], red2Pos[42][1] - 25],[red2Pos[43][0], red2Pos[43][1] - 25],[red2Pos[44][0], red2Pos[44][1] - 25],[red2Pos[45][0], red2Pos[45][1] - 25],[red2Pos[46][0], red2Pos[46][1] - 25],[red2Pos[47][0], red2Pos[47][1] - 25],[yellow2Pos[65][0],yellow2Pos[65][1] - 25],[yellow2Pos[66][0],yellow2Pos[66][1] - 25],[yellow2Pos[67][0],yellow2Pos[67][1] - 25],[yellow2Pos[68][0],yellow2Pos[68][1] - 25],[yellow2Pos[69][0],yellow2Pos[69][1] - 25],[yellow2Pos[70][0],yellow2Pos[70][1] - 25],[yellow2Pos[71][0],yellow2Pos[71][1] - 25],[yellow2Pos[72][0],yellow2Pos[72][1] - 25]]
    yellow4Pos = [[160,760],[red3Pos[52][0], red3Pos[52][1] - 25],[red3Pos[53][0] + 2, red3Pos[53][1] - 20],[red3Pos[54][0] + 7, red3Pos[54][1] - 18],[red3Pos[55][0] + 12, red3Pos[55][1] - 16],[red3Pos[56][0] + 18, red3Pos[56][1] - 14],[red3Pos[57][0] + 20, red3Pos[57][1] - 9],[red3Pos[58][0] + 20, red3Pos[58][1] - 3],[red3Pos[59][0] + 25, red3Pos[59][1]],[red3Pos[60][0] + 25, red3Pos[60][1]],[red3Pos[61][0] + 25, red3Pos[61][1]],[red3Pos[62][0] + 25, red3Pos[62][1]],[red3Pos[63][0] + 25, red3Pos[63][1]],[red3Pos[64][0] + 25, red3Pos[64][1]],[green3Pos[48][0] + 25, green3Pos[48][1]],[green3Pos[49][0] + 25, green3Pos[49][1]],[green3Pos[50][0] + 25, green3Pos[50][1]],[green3Pos[51][0] + 25, green3Pos[51][1]],[red3Pos[1][0] + 25, red3Pos[1][1]],[red3Pos[2][0] + 20, red3Pos[2][1] + 2],[red3Pos[3][0] + 20, red3Pos[3][1] + 8],[red3Pos[4][0] + 20, red3Pos[4][1] + 14],[red3Pos[5][0] + 14, red3Pos[5][1] + 16],[red3Pos[6][0] + 8, red3Pos[6][1] + 20],[red3Pos[7][0] + 2, red3Pos[7][1] + 20],[red3Pos[8][0], red3Pos[8][1] + 25],[red3Pos[9][0], red3Pos[9][1] + 25],[red3Pos[10][0], red3Pos[10][1] + 25],[red3Pos[11][0], red3Pos[11][1] + 25],[red3Pos[12][0], red3Pos[12][1] + 25],[red3Pos[13][0], red3Pos[13][1] + 25],[red3Pos[14][0], red3Pos[14][1] + 25],[red3Pos[15][0], red3Pos[15][1] + 25],[red3Pos[16][0], red3Pos[16][1] + 25],[red3Pos[17][0], red3Pos[17][1] + 25],[red3Pos[18][0], red3Pos[18][1] + 25],[red3Pos[19][0] - 2 , red3Pos[19][1] + 25],[red3Pos[20][0] - 6, red3Pos[20][1] + 18],[red3Pos[21][0] - 11, red3Pos[21][1] + 16],[red3Pos[22][0] - 15, red3Pos[22][1] + 14],[red3Pos[23][0] - 18, red3Pos[23][1] + 8],[red3Pos[24][0] - 20, red3Pos[24][1] + 3],[red3Pos[25][0] - 30, red3Pos[25][1]],[red3Pos[26][0] - 30, red3Pos[26][1]],[red3Pos[27][0] - 30, red3Pos[27][1]],[red3Pos[28][0] - 30, red3Pos[28][1]],[red3Pos[29][0] - 30, red3Pos[29][1]],[red3Pos[30][0] - 30, red3Pos[30][1]],[red3Pos[31][0] - 30, red3Pos[31][1]],[red3Pos[32][0] - 30, red3Pos[32][1]],[red3Pos[33][0] - 30, red3Pos[33][1]],[red3Pos[34][0] - 30, red3Pos[34][1]],[red3Pos[35][0] - 30, red3Pos[35][1]],[red3Pos[36][0] - 20, red3Pos[36][1] - 3],[red3Pos[37][0] - 18, red3Pos[37][1] - 7],[red3Pos[38][0] - 16, red3Pos[38][1] - 11],[red3Pos[39][0] - 14, red3Pos[39][1] - 15],[red3Pos[40][0] - 8, red3Pos[40][1] - 20],[red3Pos[41][0] - 3, red3Pos[41][1] - 20],[red3Pos[42][0], red3Pos[42][1] - 25],[red3Pos[43][0], red3Pos[43][1] - 25],[red3Pos[44][0], red3Pos[44][1] - 25],[red3Pos[45][0], red3Pos[45][1] - 25],[red3Pos[46][0], red3Pos[46][1] - 25],[red3Pos[47][0], red3Pos[47][1] - 25],[yellow3Pos[65][0],yellow3Pos[65][1] - 25],[yellow3Pos[66][0],yellow3Pos[66][1] - 25],[yellow3Pos[67][0],yellow3Pos[67][1] - 25],[yellow3Pos[68][0],yellow3Pos[68][1] - 25],[yellow3Pos[69][0],yellow3Pos[69][1] - 25],[yellow3Pos[70][0],yellow3Pos[70][1] - 25],[yellow3Pos[71][0],yellow3Pos[71][1] - 25],[yellow3Pos[72][0],yellow3Pos[72][1] - 25]]
     
    if num == 1:
        return yellow1Pos
    if num == 2:
        return yellow2Pos
    if num == 3:
        return yellow3Pos
    if num == 4:
        return yellow4Pos

def status(piece):
    if piece.index == 0:
        piece.inJail = True
    else:
        piece.inJail = False 
    if piece.index == 72:
        piece.done = True
    else:
        piece.done = False
        

def roll3(piece1,piece2,piece3,piece4):
    numWon = 0
    if piece1.done:
        numWon+=1
    if piece2.done:
        numWon+=1
    if piece3.done:
        numWon+=1
    if piece4.done:
        numWon+=1
    if numWon <= 2:
        num0 = 0
        if piece1.inJail:
            num0+=1
        if piece2.inJail:
            num0+=1
        if piece3.inJail:
            num0+=1 
        if piece4.inJail:
            num0+=1
        if num0 >= 2:
            return True
        return False
    else:
        if piece1.inJail:
            return True
        if piece2.inJail:
            return True
        if piece3.inJail:
            return True
        if piece4.inJail:
            return True
        return False


def eat(piece,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12):
    if piece.index == 1 or piece.index == 8 or piece.index == 13 or piece.index == 18 or piece.index == 25 or piece.index == 30 or piece.index == 35 or piece.index == 42 or piece.index == 47 or piece.index == 52 or piece.index == 59 or piece.index >= 64:
        pass
    else:
        otherpieces = [other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12]
        tile = piece.track[piece.index]
        for i in otherpieces:
            #print(i.index)
            if i.index > 72:
                i.index == 72
            if i.track[i.index] == tile:
                i.index = 0 
                print(str(i.color) + " piece eaten")
                
def eatAll(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12):
    eat(piece1,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)
    eat(piece2,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)
    eat(piece3,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)
    eat(piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)



def stomp(piece,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12):
    otherpieces = [other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12]
    start = piece.track[1]
    for i in otherpieces:
        if i.track[i.index] == start:
            i.index = 0
            print(str(i.color) + " piece eaten")

def freeFromJail(piece1,piece2,piece3,piece4):
    if piece1.inJail:
        piece1.index = 1
    if piece2.inJail:
        piece2.index = 1
    if piece3.inJail:
        piece3.index = 1
    if piece4.inJail:
        piece4.index = 1

def strat1(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12):
    print("\t\t\t\t\t\tstrat1")
    for i in range(3):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        print("dice1: " + str(dice1) + " | dice2: " + str(dice2))
        if dice1 == dice2:
            print("DOUBLES")
            freeFromJail(piece1,piece2,piece3,piece4)
            break
    print(piece1.color + "1: " + str(piece1.index) + " | " + piece2.color + "2: " + str(piece2.index) + " | " + piece3.color + "3: " + str(piece3.index) + " | " + piece4.color + "4: " + str(piece4.index))
    if dice1 == dice2:
        print("Out of Jail")
        stomp(piece1,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)
        mainMove(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12) 


    
def closeSafe(piece,dice1,dice2):
    spacesLeft = 72 - piece.index
    notAllowed = 0
    if spacesLeft < dice1:
        piece.closeDice1 = True
        notAllowed += 1
    else:
        piece.closeDice1 = False
    if spacesLeft < dice2:
        piece.closeDice2 = True
        notAllowed += 1
    else:
        piece.closeDice2 = False
    if spacesLeft < (dice1 + dice2):
        piece.closeCombined = True
        notAllowed += 1
    else:
        piece.closeCombined = False
    if notAllowed < 3:
        piece.closeMove = False
    else:
        piece.closeMove = True
    if piece.index == 72:
        piece.closeMove = False
    
def mainMove(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12):
    status(piece1)
    status(piece2)
    status(piece3)
    status(piece4)
    numInJail = 0
    if piece1.inJail:
        numInJail += 1
    if piece2.inJail:
        numInJail += 1
    if piece3.inJail:
        numInJail += 1
    if piece4.inJail:
        numInJail += 1
    numDone = 0
    if piece1.done:
        numDone += 1
    if piece2.done:
        numDone += 1
    if piece3.done:
        numDone += 1
    if piece4.done:
        numDone += 1
        
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    closeSafe(piece1,dice1,dice2)
    closeSafe(piece2,dice1,dice2)
    closeSafe(piece3,dice1,dice2)
    closeSafe(piece4,dice1,dice2)

    
    numTooClose = 0
    if piece1.closeMove:
        numTooClose += 1
    if piece2.closeMove:
        numTooClose += 1
    if piece3.closeMove:
        numTooClose += 1
    if piece4.closeMove:
        numTooClose += 1
    
    color = piece1.color
    print(color + '1: inJail: ' + str(piece1.inJail) + " | done: " + str(piece1.done) + " | far: " + str(piece1.closeMove))
    print(color + '2: inJail: ' + str(piece2.inJail) + " | done: " + str(piece2.done) + " | far: " + str(piece2.closeMove))
    print(color + '3: inJail: ' + str(piece3.inJail) + " | done: " + str(piece3.done) + " | far: " + str(piece3.closeMove))
    print(color + '4: inJail: ' + str(piece4.inJail) + " | done: " + str(piece4.done) + " | far: " + str(piece4.closeMove))
    print(piece1.color + "1: " + str(piece1.index) + " | " + piece2.color + "2: " + str(piece2.index) + " | " + piece3.color + "3: " + str(piece3.index) + " | " + piece4.color + "4: " + str(piece4.index))
    print("dice1: " + str(dice1) + " | dice2: " + str(dice2))
    #Strat 1
    if numInJail == 4 or (numInJail == 3 and numDone == 1) or (numInJail == 2 and numDone == 2) or (numInJail == 1 and numDone == 3):
        strat1(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)
    #Strat 2
    elif (numInJail == 2 and numTooClose == 1 and numDone == 0) or (numInJail == 2 and numDone == 1 and numTooClose == 0) or (numInJail == 3 and numDone == 0 and numTooClose == 0):
        strat2(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2)
    #Strat 3
    elif (numInJail == 1 and numTooClose == 2 and numDone == 0) or (numInJail == 1 and numDone == 1 and numTooClose == 1):
        strat3(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2)
    #Strat 4
    elif numInJail == 2 and numDone == 0 and numTooClose == 0:
        strat4(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2)
    #Strat 5
    elif (numInJail == 1 and numTooClose == 1 and numDone == 0) or (numInJail == 1 and numDone == 1 and numTooClose == 0):
        strat5(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2)
    #Strat 6
    elif (numInJail == 0 and numDone == 0 and numTooClose == 2) or (numInJail == 0 and numDone == 1 and numTooClose == 1) or (numInJail == 0 and numDone == 2 and numTooClose == 0):
        strat6(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2)
    #Strat 7
    elif (numInJail == 0 and numDone == 0 and numTooClose == 1) or (numInJail == 0 and numDone == 1 and numTooClose == 0):
        strat7(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2)
    #Strat 8
    elif (numInJail == 0 and numDone == 0 and numTooClose == 0):
        strat8(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2)
    #Strat 9
    elif numTooClose == 4 or (numDone == 1 and numTooClose == 3) or (numDone == 2 and numTooClose == 2):
        strat9(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2)
    #strat 10
    elif (numInJail == 1 and numTooClose == 3) or (numInJail == 2 and numTooClose == 2) or (numInJail == 3 and numTooClose == 1) or (numInJail == 1 and numDone == 1 and numTooClose == 2) or (numInJail == 1 and numDone == 2 and numTooClose == 1) or (numInJail == 2 and numDone == 1 and numTooClose == 1):
        strat10(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2)
    #Strat 11
    elif (numInJail == 0 and numDone == 0 and numTooClose == 3) or (numInJail == 0 and numDone == 1 and numTooClose == 2) or (numInJail == 0 and numDone == 2 and numTooClose == 1):
        strat11(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2)
   #Strat 12
    elif numInJail == 0 and numDone == 3 and numTooClose == 0:
        strat12(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2)
    #Strat 13
    elif numInJail == 1 and numDone == 2 and numTooClose == 0:
        strat13(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2)
    #Strat 14
    elif numInJail == 0 and numDone == 3 and numTooClose == 1:
        strat14(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2)
    #Strat 15
    elif (numInJail == 1 and numDone == 0 and numTooClose == 0):
        strat15(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2)
    else:
        pass
        print("You Win")

        
def decideFor1(piece,dice1,dice2):
    if not piece.closeCombined:
        piece.index += dice1 + dice2
    elif not (piece.closeDice1 or piece.closeDice2):
        piece.index += max(dice1,dice2)
    else:
        piece.index += min(dice1,dice2)
    if piece.index > 72:
        print("decideFor1")

def strat2(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2):
    print("\t\t\t\t\t\tstrat2")
    if dice1 == dice2:
        print("Doubles")
        freeFromJail(piece1,piece2,piece3,piece4)
        print("Out of Jail")
        stomp(piece1,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)
        eatAll(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)
        print(piece1.color + "1: " + str(piece1.index) + " | " + piece2.color + "2: " + str(piece2.index) + " | " + piece3.color + "3: " + str(piece3.index) + " | " + piece4.color + "4: " + str(piece4.index))
        mainMove(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)
    else:
        if not (piece1.inJail or piece1.done or piece1.closeMove):
            decideFor1(piece1,dice1,dice2)
        elif not (piece2.inJail or piece2.done or piece2.closeMove):
            decideFor1(piece2,dice1,dice2)
        elif not (piece3.inJail or piece3.done or piece3.closeMove):
            decideFor1(piece3,dice1,dice2)
        else:
            decideFor1(piece4,dice1,dice2)
        eatAll(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)
        print(piece1.color + "1: " + str(piece1.index) + " | " + piece2.color + "2: " + str(piece2.index) + " | " + piece3.color + "3: " + str(piece3.index) + " | " + piece4.color + "4: " + str(piece4.index))

def strat3(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2):
    print("\t\t\t\t\t\tstrat3")
    if dice1 == dice2:
        print("Doubles")
        freeFromJail(piece1,piece2,piece3,piece4)
        print("Out of Jail")
        stomp(piece1,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)
        if not (piece1.inJail or piece1.done or piece1.closeMove):
            piece1.index += dice1
        elif not (piece2.inJail or piece2.done or piece2.closeMove):
            piece2.index += dice1
        elif not (piece3.inJail or piece3.done or piece3.closeMove):
            piece3.index += dice1
        else:
            piece4.index += dice1
        eatAll(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)
        print(piece1.color + "1: " + str(piece1.index) + " | " + piece2.color + "2: " + str(piece2.index) + " | " + piece3.color + "3: " + str(piece3.index) + " | " + piece4.color + "4: " + str(piece4.index))
        mainMove(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)
    else:
        if not (piece1.inJail or piece1.done or piece1.closeMove):
            decideFor1(piece1,dice1,dice2)
        elif not (piece2.inJail or piece2.done or piece2.closeMove):
            decideFor1(piece2,dice1,dice2)
        elif not (piece3.inJail or piece3.done or piece3.closeMove):
            decideFor1(piece3,dice1,dice2)
        else:
            decideFor1(piece4,dice1,dice2)
        eatAll(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)
        print(piece1.color + "1: " + str(piece1.index) + " | " + piece2.color + "2: " + str(piece2.index) + " | " + piece3.color + "3: " + str(piece3.index) + " | " + piece4.color + "4: " + str(piece4.index))

def decideFor2(piece1,piece2,dice1,dice2):
    p1Count = 3
    if piece1.closeCombined:
        p1Count -= 1
    if piece1.closeDice1:
        p1Count -= 1
    if piece1.closeDice2:
        p1Count -= 1
    p2Count = 3
    if piece2.closeCombined:
        p2Count -= 1
    if piece2.closeDice1:
        p2Count -= 1
    if piece2.closeDice2:
        p2Count -= 1
    if p1Count == 3 and p2Count == 3:
        randChoice = random.randint(1,4)
        if randChoice == 1:
            piece1.index += dice1
            piece2.index += dice2
        elif randChoice == 2: 
            piece1.index += dice2
            piece2.index += dice1
        elif randChoice == 3:
            piece1.index += dice1 + dice2
        else:
            piece2.index += dice1 + dice2
    
    elif p1Count == 3 and p2Count == 2:
        randChoice = random.randint(1,3)
        if randChoice == 1:
            piece1.index += dice1
            piece2.index += dice2
        elif randChoice == 2: 
            piece1.index += dice2
            piece2.index += dice1
        else:
            piece1.index += dice1 + dice2

    elif p1Count == 2 and p2Count == 3:
        randChoice = random.randint(1,3)
        if randChoice == 1:
            piece1.index += dice1
            piece2.index += dice2
        elif randChoice == 2: 
            piece1.index += dice2
            piece2.index += dice1
        else:
            piece2.index += dice1 + dice2
    
    elif p1Count == 2 and p2Count == 2:
        randChoice = random.randint(1,2)
        if randChoice == 1:
            piece1.index += dice1
            piece2.index += dice2
        else:
            piece1.index += dice2
            piece2.index += dice1

    elif (p1Count == 3 and p2Count == 1):
        randChoice = random.randint(1,2)
        if randChoice == 1:
            piece1.index += max(dice1,dice2)
            piece2.index += min(dice1,dice2)
        else:
            piece1.index += dice1 + dice2

    elif (p1Count == 1 and p2Count == 3):
        randChoice = random.randint(1,2)
        if randChoice == 1:
            piece1.index += min(dice1,dice2)
            piece2.index += max(dice1,dice2)
        else:
            piece2.index += dice1 + dice2
    
    elif (p1Count == 2 and p2Count == 1):
        piece1.index += max(dice1,dice2)
        piece2.index += min(dice1,dice2)
    
    elif (p1Count == 1 and p2Count == 2):
        piece1.index += min(dice1,dice2)
        piece2.index += max(dice1,dice2)
    else:
        randChoice = random.randint(1,2)
        if randChoice == 1:
            piece1.index += min(dice1,dice2)
        else:
            piece2.index += min(dice1,dice2)
    if piece1.index > 72 or piece2.index > 72:
        print("decideFor2")
    
def constructArguments(piece1,piece2,piece3,piece4,dice1,dice2):
    list1 = [piece1,piece2,piece3,piece4]
    list2 = []
    for i in list1:
        if not (i.inJail or i.done or i.closeMove):
            list2.append(i)
    list2.append(dice1)
    list2.append(dice2)
    return list2

def strat4(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2):
    print("\t\t\t\t\t\tstrat4")
    if dice1 == dice2:
        print("Doubles")
        freeFromJail(piece1,piece2,piece3,piece4)
        print("Out of Jail")
        stomp(piece1,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)
        print(piece1.color + "1: " + str(piece1.index) + " | " + piece2.color + "2: " + str(piece2.index) + " | " + piece3.color + "3: " + str(piece3.index) + " | " + piece4.color + "4: " + str(piece4.index))
        mainMove(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)
    else:
        list1 = constructArguments(piece1,piece2,piece3,piece4,dice1,dice2)
        decideFor2(*list1)   
        eatAll(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12) 
        print(piece1.color + "1: " + str(piece1.index) + " | " + piece2.color + "2: " + str(piece2.index) + " | " + piece3.color + "3: " + str(piece3.index) + " | " + piece4.color + "4: " + str(piece4.index))
                        
def strat5(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2):
    print("\t\t\t\t\t\tstrat5")
    if dice1 == dice2:
        print("Doubles")
        freeFromJail(piece1,piece2,piece3,piece4)
        print("Out of Jail")
        stomp(piece1,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)
        listFree = []
        if not (piece1.inJail or piece1.done or piece1.closeMove):
            listFree.append(piece1)
        if not (piece2.inJail or piece2.done or piece2.closeMove):
            listFree.append(piece2)
        if not (piece3.inJail or piece3.done or piece3.closeMove):
            listFree.append(piece3)
        if not (piece4.inJail or piece4.done or piece4.closeMove):
            listFree.append(piece4)
        rando = random.randint(0,1)
        listFree[rando].index += dice1
        eatAll(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)
        print(piece1.color + "1: " + str(piece1.index) + " | " + piece2.color + "2: " + str(piece2.index) + " | " + piece3.color + "3: " + str(piece3.index) + " | " + piece4.color + "4: " + str(piece4.index))
        mainMove(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)
    else:
        list1 = constructArguments(piece1,piece2,piece3,piece4,dice1,dice2)
        decideFor2(*list1)
        eatAll(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)
        print(piece1.color + "1: " + str(piece1.index) + " | " + piece2.color + "2: " + str(piece2.index) + " | " + piece3.color + "3: " + str(piece3.index) + " | " + piece4.color + "4: " + str(piece4.index))    

def strat6(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2):
    print("\t\t\t\t\t\tstrat6")
    list1 = constructArguments(piece1,piece2,piece3,piece4,dice1,dice2)
    decideFor2(*list1)
    eatAll(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)   
    print(piece1.color + "1: " + str(piece1.index) + " | " + piece2.color + "2: " + str(piece2.index) + " | " + piece3.color + "3: " + str(piece3.index) + " | " + piece4.color + "4: " + str(piece4.index)) 
    if dice1 == dice2:
        print("Doubles")
        mainMove(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)
    
def decideFor3(piece1,piece2,piece3,dice1,dice2):
    p1Count = 3
    if piece1.closeCombined:
        p1Count -= 1
    if piece1.closeDice1:
        p1Count -= 1
    if piece1.closeDice2:
        p1Count -= 1
    p2Count = 3
    if piece2.closeCombined:
        p2Count -= 1
    if piece2.closeDice1:
        p2Count -= 1
    if piece2.closeDice2:
        p2Count -= 1
    p3Count = 3
    if piece3.closeCombined:
        p3Count -= 1
    if piece3.closeDice1:
        p3Count -= 1
    if piece3.closeDice2:
        p3Count -= 1
    if p1Count == 3 and p2Count == 3 and p3Count == 3:
        randChoice = random.randint(1,9)
        if randChoice == 1:
            piece1.index += dice1
            piece2.index += dice2
        elif randChoice == 2:
            piece1.index += dice1
            piece3.index += dice2
        elif randChoice == 3:
            piece2.index += dice1
            piece3.index += dice2
        elif randChoice == 4:
            piece1.index += dice2
            piece2.index += dice1
        elif randChoice == 5:
            piece1.index += dice2
            piece3.index += dice1
        elif randChoice == 6:
            piece2.index += dice2
            piece3.index += dice1
        elif randChoice == 7:
            piece1.index += dice1 + dice2
        elif randChoice == 8:
            piece2.index += dice1 + dice2
        else:
            piece3.index += dice1 + dice2
        if piece1.index > 72 or piece2.index > 72 or piece3.index > 72:
            print("Error 1")

    elif p1Count == 2 and p2Count == 3 and p3Count == 3:
        randChoice = random.randint(1,8)
        if randChoice == 1:
            piece1.index += dice1
            piece2.index += dice2
        elif randChoice == 2:
            piece1.index += dice1
            piece3.index += dice2
        elif randChoice == 3:
            piece2.index += dice1
            piece3.index += dice2
        elif randChoice == 4:
            piece1.index += dice2
            piece2.index += dice1
        elif randChoice == 5:
            piece1.index += dice2
            piece3.index += dice1
        elif randChoice == 6:
            piece2.index += dice2
            piece3.index += dice1
        elif randChoice == 7:
            piece2.index += dice1 + dice2
        else:
            piece3.index += dice1 + dice2
        if piece1.index > 72 or piece2.index > 72 or piece3.index > 72:
            print("Error 2")
    
    elif p1Count == 3 and p2Count == 2 and p3Count == 3:
        randChoice = random.randint(1,8)
        if randChoice == 1:
            piece1.index += dice1
            piece2.index += dice2
            if piece1.index > 72 or piece2.index > 72 or piece3.index > 72:
                print("Suberror 1")
        elif randChoice == 2:
            piece1.index += dice1
            piece3.index += dice2
            if piece1.index > 72 or piece2.index > 72 or piece3.index > 72:
                print("Suberror 2")
        elif randChoice == 3:
            piece2.index += dice1
            piece3.index += dice2
            if piece1.index > 72 or piece2.index > 72 or piece3.index > 72:
                print("Suberror 3")
        elif randChoice == 4:
            piece1.index += dice2
            piece2.index += dice1
            if piece1.index > 72 or piece2.index > 72 or piece3.index > 72:
                print("Suberror 4")
        elif randChoice == 5:
            piece1.index += dice2
            piece3.index += dice1
            if piece1.index > 72 or piece2.index > 72 or piece3.index > 72:
                print("Suberror 5")
        elif randChoice == 6:
            piece2.index += dice2
            piece3.index += dice1
            if piece1.index > 72 or piece2.index > 72 or piece3.index > 72:
                print("Suberror 6")
        elif randChoice == 7:
            piece1.index += dice1 + dice2
            if piece1.index > 72 or piece2.index > 72 or piece3.index > 72:
                print("Suberror 7")
        else:
            piece3.index += dice1 + dice2
            if piece1.index > 72 or piece2.index > 72 or piece3.index > 72:
                print("Suberror 8")
        if piece1.index > 72 or piece2.index > 72 or piece3.index > 72:
            print("Error 3")

    elif p1Count == 3 and p2Count == 3 and p3Count == 2:
        randChoice = random.randint(1,8)
        if randChoice == 1:
            piece1.index += dice1
            piece2.index += dice2
        elif randChoice == 2:
            piece1.index += dice1
            piece3.index += dice2
        elif randChoice == 3:
            piece2.index += dice1
            piece3.index += dice2
        elif randChoice == 4:
            piece1.index += dice2
            piece2.index += dice1
        elif randChoice == 5:
            piece1.index += dice2
            piece3.index += dice1
        elif randChoice == 6:
            piece2.index += dice2
            piece3.index += dice1
        elif randChoice == 7:
            piece1.index += dice1 + dice2
        else:
            piece2.index += dice1 + dice2
        if piece1.index > 72 or piece2.index > 72 or piece3.index > 72:
            print("Error 4")
    
    elif p1Count == 2 and p2Count == 2 and p3Count == 3:
        randChoice = random.randint(1,7)
        if randChoice == 1:
            piece1.index += dice1
            piece2.index += dice2
        elif randChoice == 2:
            piece1.index += dice1
            piece3.index += dice2
        elif randChoice == 3:
            piece2.index += dice1
            piece3.index += dice2
        elif randChoice == 4:
            piece1.index += dice2
            piece2.index += dice1
        elif randChoice == 5:
            piece1.index += dice2
            piece3.index += dice1
        elif randChoice == 6:
            piece2.index += dice2
            piece3.index += dice1
        else:
            piece3.index += dice1 + dice2
        if piece1.index > 72 or piece2.index > 72 or piece3.index > 72:
            print("Error 5")
        
    elif p1Count == 2 and p2Count == 3 and p3Count == 2:
        randChoice = random.randint(1,7)
        if randChoice == 1:
            piece1.index += dice1
            piece2.index += dice2
        elif randChoice == 2:
            piece1.index += dice1
            piece3.index += dice2
        elif randChoice == 3:
            piece2.index += dice1
            piece3.index += dice2
        elif randChoice == 4:
            piece1.index += dice2
            piece2.index += dice1
        elif randChoice == 5:
            piece1.index += dice2
            piece3.index += dice1
        elif randChoice == 6:
            piece2.index += dice2
            piece3.index += dice1
        else:
            piece2.index += dice1 + dice2
        if piece1.index > 72 or piece2.index > 72 or piece3.index > 72:
            print("Error 6")

    elif p1Count == 3 and p2Count == 2 and p3Count == 2:
        randChoice = random.randint(1,7)
        if randChoice == 1:
            piece1.index += dice1
            piece2.index += dice2
        elif randChoice == 2:
            piece1.index += dice1
            piece3.index += dice2
        elif randChoice == 3:
            piece2.index += dice1
            piece3.index += dice2
        elif randChoice == 4:
            piece1.index += dice2
            piece2.index += dice1
        elif randChoice == 5:
            piece1.index += dice2
            piece3.index += dice1
        elif randChoice == 6:
            piece2.index += dice2
            piece3.index += dice1
        else:
            piece1.index += dice1 + dice2
        if piece1.index > 72 or piece2.index > 72 or piece3.index > 72:
            print("Error 7")

    elif p1Count == 2 and p2Count == 2 and p3Count == 2:
        randChoice = random.randint(1,6)
        if randChoice == 1:
            piece1.index += dice1
            piece2.index += dice2
        elif randChoice == 2:
            piece1.index += dice1
            piece3.index += dice2
        elif randChoice == 3:
            piece2.index += dice1
            piece3.index += dice2
        elif randChoice == 4:
            piece1.index += dice2
            piece2.index += dice1
        elif randChoice == 5:
            piece1.index += dice2
            piece3.index += dice1
        else:
            piece2.index += dice2
            piece3.index += dice1
        if piece1.index > 72 or piece2.index > 72 or piece3.index > 72:
            print("Error 8")
    
    elif p1Count == 3 and p2Count == 3 and p3Count == 1:
        randChoice = random.randint(1,6)
        if randChoice == 1:
            piece1.index += dice1
            piece2.index += dice2
        elif randChoice == 2:
            piece1.index += max(dice1,dice2)
            piece3.index += min(dice1,dice2)
        elif randChoice == 3:
            piece2.index += max(dice1,dice2)
            piece3.index += min(dice1,dice2)
        elif randChoice == 4:
            piece1.index += dice2
            piece2.index += dice1
        elif randChoice == 5:
            piece1.index += dice1 + dice2
        else:
            piece2.index += dice1 + dice2
        if piece1.index > 72 or piece2.index > 72 or piece3.index > 72:
            print("Error 9")

    elif p1Count == 3 and p2Count == 1 and p3Count == 3:
        randChoice = random.randint(1,6)
        if randChoice == 1:
            piece1.index += dice1
            piece3.index += dice2
        elif randChoice == 2:
            piece1.index += max(dice1,dice2)
            piece2.index += min(dice1,dice2)
        elif randChoice == 3:
            piece3.index += max(dice1,dice2)
            piece2.index += min(dice1,dice2)
        elif randChoice == 4:
            piece1.index += dice2
            piece3.index += dice1
        elif randChoice == 5:
            piece1.index += dice1 + dice2
        else:
            piece3.index += dice1 + dice2
        if piece1.index > 72 or piece2.index > 72 or piece3.index > 72:
            print("Error 10")
    
    elif p1Count == 1 and p2Count == 3 and p3Count == 3:
        randChoice = random.randint(1,6)
        if randChoice == 1:
            piece3.index += dice1
            piece2.index += dice2
        elif randChoice == 2:
            piece3.index += max(dice1,dice2)
            piece1.index += min(dice1,dice2)
        elif randChoice == 3:
            piece2.index += max(dice1,dice2)
            piece1.index += min(dice1,dice2)
        elif randChoice == 4:
            piece3.index += dice2
            piece2.index += dice1
        elif randChoice == 5:
            piece3.index += dice1 + dice2
        else:
            piece2.index += dice1 + dice2
        if piece1.index > 72 or piece2.index > 72 or piece3.index > 72:
            print("Error 11")
        
    elif p1Count == 3 and p2Count == 1 and p3Count == 1:
        randChoice = random.randint(1,3)
        if randChoice == 1:
            piece1.index += max(dice1,dice2)
            piece2.index += min(dice1,dice2)
        elif randChoice == 2:
            piece1.index += max(dice1,dice2)
            piece3.index += min(dice1,dice2)
        else:
            piece1.index += dice1 + dice2
        if piece1.index > 72 or piece2.index > 72 or piece3.index > 72:
            print("Error 12")

    elif p1Count == 1 and p2Count == 3 and p3Count == 1:
        randChoice = random.randint(1,3)
        if randChoice == 1:
            piece2.index += max(dice1,dice2)
            piece1.index += min(dice1,dice2)
        elif randChoice == 2:
            piece2.index += max(dice1,dice2)
            piece3.index += min(dice1,dice2)
        else:
            piece2.index += dice1 + dice2
        if piece1.index > 72 or piece2.index > 72 or piece3.index > 72:
            print("Error 13")

    elif p1Count == 1 and p2Count == 1 and p3Count == 3:
        randChoice = random.randint(1,3)
        if randChoice == 1:
            piece3.index += max(dice1,dice2)
            piece2.index += min(dice1,dice2)
        elif randChoice == 2:
            piece3.index += max(dice1,dice2)
            piece1.index += min(dice1,dice2)
        else:
            piece3.index += dice1 + dice2
        if piece1.index > 72 or piece2.index > 72 or piece3.index > 72:
            print("Error 14")

    elif p1Count == 1 and p2Count == 1 and p3Count == 1:
        randChoice = random.randint(1,3)
        if randChoice == 1:
            piece1.index += min(dice1,dice2)
        elif randChoice == 2:
            piece2.index += min(dice1,dice2)
        else:
            piece3.index += min(dice1,dice2)
        if piece1.index > 72 or piece2.index > 72 or piece3.index > 72:
            print("Error 15")

    elif p1Count == 2 and p2Count == 2 and p3Count == 1:
        randChoice = random.randint(1,4)
        if randChoice == 1:
            piece1.index += dice1
            piece2.index += dice2
        elif randChoice == 2:
            piece1.index += max(dice1,dice2)
            piece3.index += min(dice1,dice2)
        elif randChoice == 3:
            piece2.index += max(dice1,dice2)
            piece3.index += min(dice1,dice2)
        else:
            piece1.index += dice2
            piece2.index += dice1
        if piece1.index > 72 or piece2.index > 72 or piece3.index > 72:
            print("Error 16")

    elif p1Count == 2 and p2Count == 1 and p3Count == 2:
        randChoice = random.randint(1,4)
        if randChoice == 1:
            piece1.index += dice1
            piece3.index += dice2
        elif randChoice == 2:
            piece1.index += max(dice1,dice2)
            piece2.index += min(dice1,dice2)
        elif randChoice == 3:
            piece3.index += max(dice1,dice2)
            piece2.index += min(dice1,dice2)
        else:
            piece1.index += dice2
            piece3.index += dice1
        if piece1.index > 72 or piece2.index > 72 or piece3.index > 72:
            print("Error 17")

    elif p1Count == 1 and p2Count == 2 and p3Count == 2:
        randChoice = random.randint(1,4)
        if randChoice == 1:
            piece3.index += dice1
            piece2.index += dice2
        elif randChoice == 2:
            piece3.index += max(dice1,dice2)
            piece1.index += min(dice1,dice2)
        elif randChoice == 3:
            piece2.index += max(dice1,dice2)
            piece1.index += min(dice1,dice2)
        else:
            piece3.index += dice2
            piece2.index += dice1
        if piece1.index > 72 or piece2.index > 72 or piece3.index > 72:
            print("Error 18")

    elif p1Count == 2 and p2Count == 1 and p3Count == 1:
        randChoice = random.randint(1,2)
        if randChoice == 1:
            piece1.index += max(dice1,dice2)
            piece3.index += min(dice1,dice2)
        else:
            piece1.index += max(dice1,dice2)
            piece2.index += min(dice1,dice2)
        if piece1.index > 72 or piece2.index > 72 or piece3.index > 72:
            print("Error 19")

    elif p1Count == 1 and p2Count == 2 and p3Count == 1:
        randChoice = random.randint(1,2)
        if randChoice == 1:
            piece2.index += max(dice1,dice2)
            piece3.index += min(dice1,dice2)
        else:
            piece2.index += max(dice1,dice2)
            piece1.index += min(dice1,dice2)
        if piece1.index > 72 or piece2.index > 72 or piece3.index > 72:
            print("Error 20")

    elif p1Count == 1 and p2Count == 1 and p3Count == 2:
        randChoice = random.randint(1,2)
        if randChoice == 1:
            piece3.index += max(dice1,dice2)
            piece1.index += min(dice1,dice2)
        else:
            piece3.index += max(dice1,dice2)
            piece2.index += min(dice1,dice2)
        if piece1.index > 72 or piece2.index > 72 or piece3.index > 72:
            print("Error 21")

    elif p1Count == 3 and p2Count == 2 and p3Count == 1:
        randChoice = random.randint(1,5)
        if randChoice == 1:
            piece1.index += dice1
            piece2.index += dice2
        elif randChoice == 2:
            piece1.index += max(dice1,dice2)
            piece3.index += min(dice1,dice2)
        elif randChoice == 3:
            piece2.index += max(dice1,dice2)
            piece3.index += min(dice1,dice2)
        elif randChoice == 4:
            piece1.index += dice2
            piece2.index += dice1
        else:
            piece1.index += dice1 + dice2
        if piece1.index > 72 or piece2.index > 72 or piece3.index > 72:
            print("Error 22")

    elif p1Count == 3 and p2Count == 1 and p3Count == 2:
        randChoice = random.randint(1,5)
        if randChoice == 1:
            piece1.index += dice1
            piece3.index += dice2
        elif randChoice == 2:
            piece1.index += max(dice1,dice2)
            piece2.index += min(dice1,dice2)
        elif randChoice == 3:
            piece3.index += max(dice1,dice2)
            piece2.index += min(dice1,dice2)
        elif randChoice == 4:
            piece1.index += dice2
            piece3.index += dice1
        else:
            piece1.index += dice1 + dice2
        if piece1.index > 72 or piece2.index > 72 or piece3.index > 72:
            print("Error 23")

    elif p1Count == 1 and p2Count == 3 and p3Count == 2:
        randChoice = random.randint(1,5)
        if randChoice == 1:
            piece2.index += dice1
            piece3.index += dice2
        elif randChoice == 2:
            piece2.index += max(dice1,dice2)
            piece1.index += min(dice1,dice2)
        elif randChoice == 3:
            piece3.index += max(dice1,dice2)
            piece1.index += min(dice1,dice2)
        elif randChoice == 4:
            piece2.index += dice2
            piece3.index += dice1
        else:
            piece2.index += dice1 + dice2
        if piece1.index > 72 or piece2.index > 72 or piece3.index > 72:
            print("Error 24")

    elif p1Count == 1 and p2Count == 2 and p3Count == 3:
        randChoice = random.randint(1,5)
        if randChoice == 1:
            piece3.index += dice1
            piece2.index += dice2
        elif randChoice == 2:
            piece3.index += max(dice1,dice2)
            piece1.index += min(dice1,dice2)
        elif randChoice == 3:
            piece2.index += max(dice1,dice2)
            piece1.index += min(dice1,dice2)
        elif randChoice == 4:
            piece3.index += dice2
            piece2.index += dice1
        else:
            piece3.index += dice1 + dice2
        if piece1.index > 72 or piece2.index > 72 or piece3.index > 72:
            print("Error 25")
        
    elif p1Count == 2 and p2Count == 3 and p3Count == 1:
        randChoice = random.randint(1,5)
        if randChoice == 1:
            piece2.index += dice1
            piece1.index += dice2
        elif randChoice == 2:
            piece2.index += max(dice1,dice2)
            piece3.index += min(dice1,dice2)
        elif randChoice == 3:
            piece1.index += max(dice1,dice2)
            piece3.index += min(dice1,dice2)
        elif randChoice == 4:
            piece2.index += dice2
            piece1.index += dice1
        else:
            piece2.index += dice1 + dice2
        if piece1.index > 72 or piece2.index > 72 or piece3.index > 72:
            print("Error 26")

    else:
        randChoice = random.randint(1,5)
        if randChoice == 1:
            piece3.index += dice1
            piece1.index += dice2
        elif randChoice == 2:
            piece3.index += max(dice1,dice2)
            piece2.index += min(dice1,dice2)
        elif randChoice == 3:
            piece1.index += max(dice1,dice2)
            piece2.index += min(dice1,dice2)
        elif randChoice == 4:
            piece3.index += dice2
            piece1.index += dice1
        else:
            piece3.index += dice1 + dice2
        if piece1.index > 72 or piece2.index > 72 or piece3.index > 72:
            print("Error 27")
    if piece1.index > 72 or piece2.index > 72 or piece3.index > 72:
        print("decideFor3")

def input4(piece1,piece2,piece3,piece4,p1,p2,p3,p4):
    list1 = [[piece1,p1],[piece2,p2],[piece3,p3],[piece4,p4]]
    list1.sort(key=lambda piece: piece[1])
    list2 = []
    for i in range(len(list1)):
        list2.append(list1[i][0])
    return list2

def zeroOneThree(piece1,piece2,piece3,piece4,dice1,dice2):
    rando = random.randint(1,15)
    if rando == 1:
        piece1.index += dice1
        piece2.index += dice2
    elif rando == 2:
        piece1.index += dice1
        piece3.index += dice2
    elif rando == 3:
        piece1.index += dice1
        piece4.index += dice2
    elif rando == 4:
        piece2.index += dice1
        piece3.index += dice2
    elif rando == 5:
        piece2.index += dice1
        piece4.index += dice2
    elif rando == 6:
        piece3.index += dice1
        piece4.index += dice2
    elif rando == 7:
        piece1.index += dice2
        piece2.index += dice1
    elif rando == 8:
        piece1.index += dice2
        piece3.index += dice1
    elif rando == 9:
        piece1.index += dice2
        piece4.index += dice1
    elif rando == 10:
        piece2.index += dice2
        piece3.index += dice1
    elif rando == 11:
        piece2.index += dice2
        piece4.index += dice1
    elif rando == 12:
        piece3.index += dice2
        piece4.index += dice1
    elif rando == 13:
        piece2.index += dice1 + dice2
    elif rando == 14:
        piece3.index += dice1 + dice2
    else:
        piece4.index += dice1 + dice2      
    
def zeroTwoTwo(piece1,piece2,piece3,piece4,dice1,dice2):
    rando = random.randint(1,14)
    if rando == 1:
        piece1.index += dice1
        piece2.index += dice2
    elif rando == 2:
        piece1.index += dice1
        piece3.index += dice2
    elif rando == 3:
        piece1.index += dice1
        piece4.index += dice2
    elif rando == 4:
        piece2.index += dice1
        piece3.index += dice2
    elif rando == 5:
        piece2.index += dice1
        piece4.index += dice2
    elif rando == 6:
        piece3.index += dice1
        piece4.index += dice2
    elif rando == 7:
        piece1.index += dice2
        piece2.index += dice1
    elif rando == 8:
        piece1.index += dice2
        piece3.index += dice1
    elif rando == 9:
        piece1.index += dice2
        piece4.index += dice1
    elif rando == 10:
        piece2.index += dice2
        piece3.index += dice1
    elif rando == 11:
        piece2.index += dice2
        piece4.index += dice1
    elif rando == 12:
        piece3.index += dice2
        piece4.index += dice1
    elif rando == 13:
        piece3.index += dice1 + dice2
    else:
        piece4.index += dice1 + dice2  

def zeroThreeOne(piece1,piece2,piece3,piece4,dice1,dice2):
    rando = random.randint(1,13)
    if rando == 1:
        piece1.index += dice1
        piece2.index += dice2
    elif rando == 2:
        piece1.index += dice1
        piece3.index += dice2
    elif rando == 3:
        piece1.index += dice1
        piece4.index += dice2
    elif rando == 4:
        piece2.index += dice1
        piece3.index += dice2
    elif rando == 5:
        piece2.index += dice1
        piece4.index += dice2
    elif rando == 6:
        piece3.index += dice1
        piece4.index += dice2
    elif rando == 7:
        piece1.index += dice2
        piece2.index += dice1
    elif rando == 8:
        piece1.index += dice2
        piece3.index += dice1
    elif rando == 9:
        piece1.index += dice2
        piece4.index += dice1
    elif rando == 10:
        piece2.index += dice2
        piece3.index += dice1
    elif rando == 11:
        piece2.index += dice2
        piece4.index += dice1
    elif rando == 12:
        piece3.index += dice2
        piece4.index += dice1
    else:
        piece4.index += dice1 + dice2

def oneZeroThree(piece1,piece2,piece3,piece4,dice1,dice2):
    rando = random.randint(1,12)
    if rando == 1:
        piece1.index += min(dice1,dice2)
        piece2.index += max(dice1,dice2)
    elif rando == 2:
        piece1.index += min(dice1,dice2)
        piece3.index += max(dice1,dice2)
    elif rando == 3:
        piece1.index += min(dice1,dice2)
        piece4.index += max(dice1,dice2)
    elif rando == 4:
        piece2.index += dice1
        piece3.index += dice2
    elif rando == 5:
        piece2.index += dice1
        piece4.index += dice2
    elif rando == 6:
        piece3.index += dice1
        piece4.index += dice2
    elif rando == 7:
        piece2.index += dice2
        piece3.index += dice1
    elif rando == 8:
        piece2.index += dice2
        piece4.index += dice1
    elif rando == 9:
        piece3.index += dice2
        piece4.index += dice1
    elif rando == 10:
        piece2.index += dice1 + dice2
    elif rando == 11:
        piece3.index += dice1 + dice2
    else:
        piece4.index += dice1 + dice2

def oneOneTwo(piece1,piece2,piece3,piece4,dice1,dice2):
    rando = random.randint(1,11)
    if rando == 1:
        piece1.index += min(dice1,dice2)
        piece2.index += max(dice1,dice2)
    elif rando == 2:
        piece1.index += min(dice1,dice2)
        piece3.index += max(dice1,dice2)
    elif rando == 3:
        piece1.index += min(dice1,dice2)
        piece4.index += max(dice1,dice2)
    elif rando == 4:
        piece2.index += dice1
        piece3.index += dice2
    elif rando == 5:
        piece2.index += dice1
        piece4.index += dice2
    elif rando == 6:
        piece3.index += dice1
        piece4.index += dice2
    elif rando == 7:
        piece2.index += dice2
        piece3.index += dice1
    elif rando == 8:
        piece2.index += dice2
        piece4.index += dice1
    elif rando == 9:
        piece3.index += dice2
        piece4.index += dice1
    elif rando == 10:
        piece3.index += dice1 + dice2
    else:
        piece4.index += dice1 + dice2

def oneTwoOne(piece1,piece2,piece3,piece4,dice1,dice2):
    rando = random.randint(1,10)
    if rando == 1:
        piece1.index += min(dice1,dice2)
        piece2.index += max(dice1,dice2)
    elif rando == 2:
        piece1.index += min(dice1,dice2)
        piece3.index += max(dice1,dice2)
    elif rando == 3:
        piece1.index += min(dice1,dice2)
        piece4.index += max(dice1,dice2)
    elif rando == 4:
        piece2.index += dice1
        piece3.index += dice2
    elif rando == 5:
        piece2.index += dice1
        piece4.index += dice2
    elif rando == 6:
        piece3.index += dice1
        piece4.index += dice2
    elif rando == 7:
        piece2.index += dice2
        piece3.index += dice1
    elif rando == 8:
        piece2.index += dice2
        piece4.index += dice1
    elif rando == 9:
        piece3.index += dice2
        piece4.index += dice1
    else:
        piece4.index += dice1 + dice2

def oneThreeZero(piece1,piece2,piece3,piece4,dice1,dice2):
    rando = random.randint(1,9)
    if rando == 1:
        piece1.index += min(dice1,dice2)
        piece2.index += max(dice1,dice2)
    elif rando == 2:
        piece1.index += min(dice1,dice2)
        piece3.index += max(dice1,dice2)
    elif rando == 3:
        piece1.index += min(dice1,dice2)
        piece4.index += max(dice1,dice2)
    elif rando == 4:
        piece2.index += dice1
        piece3.index += dice2
    elif rando == 5:
        piece2.index += dice1
        piece4.index += dice2
    elif rando == 6:
        piece3.index += dice1
        piece4.index += dice2
    elif rando == 7:
        piece2.index += dice2
        piece3.index += dice1
    elif rando == 8:
        piece2.index += dice2
        piece4.index += dice1
    else:
        piece3.index += dice2
        piece4.index += dice1

def twoZeroTwo(piece1,piece2,piece3,piece4,dice1,dice2):
    rando = random.randint(1,8)
    if rando == 1:
        piece1.index += min(dice1,dice2)
        piece3.index += max(dice1,dice2)
    elif rando == 2:
        piece1.index += min(dice1,dice2)
        piece4.index += max(dice1,dice2)
    elif rando == 3:
        piece2.index += min(dice1,dice2)
        piece3.index += max(dice1,dice2)
    elif rando == 4:
        piece2.index += min(dice1,dice2)
        piece4.index += max(dice1,dice2)
    elif rando == 5:
        piece3.index += dice1
        piece4.index += dice2
    elif rando == 6:
        piece3.index += dice2
        piece4.index += dice1
    elif rando == 7:
        piece3.index += dice1 + dice2
    else:
        piece4.index += dice1 + dice2
    
def twoOneOne(piece1,piece2,piece3,piece4,dice1,dice2):
    rando = random.randint(1,7)
    if rando == 1:
        piece1.index += min(dice1,dice2)
        piece3.index += max(dice1,dice2)
    elif rando == 2:
        piece1.index += min(dice1,dice2)
        piece4.index += max(dice1,dice2)
    elif rando == 3:
        piece2.index += min(dice1,dice2)
        piece3.index += max(dice1,dice2)
    elif rando == 4:
        piece2.index += min(dice1,dice2)
        piece4.index += max(dice1,dice2)
    elif rando == 5:
        piece3.index += dice1
        piece4.index += dice2
    elif rando == 6:
        piece3.index += dice2
        piece4.index += dice1
    else:
        piece4.index += dice1 + dice2

def twoTwoZero(piece1,piece2,piece3,piece4,dice1,dice2):
    rando = random.randint(1,6)
    if rando == 1:
        piece1.index += min(dice1,dice2)
        piece3.index += max(dice1,dice2)
    elif rando == 2:
        piece1.index += min(dice1,dice2)
        piece4.index += max(dice1,dice2)
    elif rando == 3:
        piece2.index += min(dice1,dice2)
        piece3.index += max(dice1,dice2)
    elif rando == 4:
        piece2.index += min(dice1,dice2)
        piece4.index += max(dice1,dice2)
    elif rando == 5:
        piece3.index += dice1
        piece4.index += dice2
    else:
        piece3.index += dice2
        piece4.index += dice1

def threeZeroOne(piece1,piece2,piece3,piece4,dice1,dice2):
    rando = random.randint(1,4)
    if rando == 1:
        piece1.index += min(dice1,dice2)
        piece4.index += max(dice1,dice2)
    elif rando == 2:
        piece2.index += min(dice1,dice2)
        piece4.index += max(dice1,dice2)
    elif rando == 3:
        piece3.index += min(dice1,dice2)
        piece4.index += max(dice1,dice2)
    else:
        piece4.index += dice1 + dice2
    
def threeOneZero(piece1,piece2,piece3,piece4,dice1,dice2):
    rando = random.randint(1,3)
    if rando == 1:
        piece1.index += min(dice1,dice2)
        piece4.index += max(dice1,dice2)
    elif rando == 2:
        piece2.index += min(dice1,dice2)
        piece4.index += max(dice1,dice2)
    else:
        piece3.index += min(dice1,dice2)
        piece4.index += max(dice1,dice2)

def decideFor4(piece1,piece2,piece3,piece4,dice1,dice2):
    p1Count = 3
    if piece1.closeCombined:
        p1Count -= 1
    if piece1.closeDice1:
        p1Count -= 1
    if piece1.closeDice2:
        p1Count -= 1
    p2Count = 3
    if piece2.closeCombined:
        p2Count -= 1
    if piece2.closeDice1:
        p2Count -= 1
    if piece2.closeDice2:
        p2Count -= 1
    p3Count = 3
    if piece3.closeCombined:
        p3Count -= 1
    if piece3.closeDice1:
        p3Count -= 1
    if piece3.closeDice2:
        p3Count -= 1
    p4Count = 3
    if piece4.closeCombined:
        p4Count -= 1
    if piece4.closeDice1:
        p4Count -= 1
    if piece4.closeDice2:
        p4Count -= 1

    if (p1Count == 3 and p2Count == 3 and p3Count == 3 and p4Count == 3):
        rando = random.randint(1,16)
        if rando == 1:
            piece1.index += dice1
            piece2.index += dice2
        elif rando == 2:
            piece1.index += dice1
            piece3.index += dice2
        elif rando == 3:
            piece1.index += dice1
            piece4.index += dice2
        elif rando == 4:
            piece2.index += dice1
            piece3.index += dice2
        elif rando == 5:
            piece2.index += dice1
            piece4.index += dice2
        elif rando == 6:
            piece3.index += dice1
            piece4.index += dice2
        elif rando == 7:
            piece1.index += dice2
            piece2.index += dice1
        elif rando == 8:
            piece1.index += dice2
            piece3.index += dice1
        elif rando == 9:
            piece1.index += dice2
            piece4.index += dice1
        elif rando == 10:
            piece2.index += dice2
            piece3.index += dice1
        elif rando == 11:
            piece2.index += dice2
            piece4.index += dice1
        elif rando == 12:
            piece3.index += dice2
            piece4.index += dice1
        elif rando == 13:
            piece1.index += dice1 + dice2
        elif rando == 14:
            piece2.index += dice1 + dice2
        elif rando == 15:
            piece3.index += dice1 + dice2
        else:
            piece4.index += dice1 + dice2
        if piece1.index > 72 or piece2.index > 72 or piece3.index > 72 or piece4.index > 72:
            print("Error 1")

    elif (p1Count == 2 and p2Count == 3 and p3Count == 3 and p4Count == 3) or (p1Count == 3 and p2Count == 2 and p3Count == 3 and p4Count == 3) or (p1Count == 3 and p2Count == 3 and p3Count == 2 and p4Count == 3) or (p1Count == 3 and p2Count == 3 and p3Count == 3 and p4Count == 2):
        list2 = input4(piece1,piece2,piece3,piece4,p1Count,p2Count,p3Count,p4Count)
        list2.append(dice1)
        list2.append(dice2)
        zeroOneThree(*list2)
        if piece1.index > 72 or piece2.index > 72 or piece3.index > 72 or piece4.index > 72:
            print("Error 2")

    elif (p1Count == 2 and p2Count == 2 and p3Count == 3 and p4Count == 3) or (p1Count == 2 and p2Count == 3 and p3Count == 2 and p4Count == 3) or (p1Count == 2 and p2Count == 3 and p3Count == 3 and p4Count == 2) or (p1Count == 3 and p2Count == 2 and p3Count == 2 and p4Count == 3) or (p1Count == 3 and p2Count == 2 and p3Count == 3 and p4Count == 2) or (p1Count == 3 and p2Count == 3 and p3Count == 2 and p4Count == 2):
        list2 = input4(piece1,piece2,piece3,piece4,p1Count,p2Count,p3Count,p4Count)
        list2.append(dice1)
        list2.append(dice2)
        zeroTwoTwo(*list2)
        if piece1.index > 72 or piece2.index > 72 or piece3.index > 72 or piece4.index > 72:
            print("Error 6")

    elif (p1Count == 2 and p2Count == 2 and p3Count == 2 and p4Count == 3) or (p1Count == 2 and p2Count == 2 and p3Count == 3 and p4Count == 2) or (p1Count == 2 and p2Count == 3 and p3Count == 2 and p4Count == 2) or (p1Count == 3 and p2Count == 2 and p3Count == 2 and p4Count == 2):
        list2 = input4(piece1,piece2,piece3,piece4,p1Count,p2Count,p3Count,p4Count)
        list2.append(dice1)
        list2.append(dice2)
        zeroThreeOne(*list2)
        if piece1.index > 72 or piece2.index > 72 or piece3.index > 72 or piece4.index > 72:
            print("Error 12")


    elif p1Count == 2 and p2Count == 2 and p3Count == 2 and p4Count == 2:
        rando = random.randint(1,12)
        if rando == 1:
            piece1.index += dice1
            piece2.index += dice2
        elif rando == 2:
            piece1.index += dice1
            piece3.index += dice2
        elif rando == 3:
            piece1.index += dice1
            piece4.index += dice2
        elif rando == 4:
            piece2.index += dice1
            piece3.index += dice2
        elif rando == 5:
            piece2.index += dice1
            piece4.index += dice2
        elif rando == 6:
            piece3.index += dice1
            piece4.index += dice2
        elif rando == 7:
            piece1.index += dice2
            piece2.index += dice1
        elif rando == 8:
            piece1.index += dice2
            piece3.index += dice1
        elif rando == 9:
            piece1.index += dice2
            piece4.index += dice1
        elif rando == 10:
            piece2.index += dice2
            piece3.index += dice1
        elif rando == 11:
            piece2.index += dice2
            piece4.index += dice1
        else:
            piece3.index += dice2
            piece4.index += dice1
        if piece1.index > 72 or piece2.index > 72 or piece3.index > 72 or piece4.index > 72:
            print("Error 16")

    elif (p1Count == 1 and p2Count == 3 and p3Count == 3 and p4Count == 3) or (p1Count == 3 and p2Count == 1 and p3Count == 3 and p4Count == 3) or (p1Count == 3 and p2Count == 3 and p3Count == 1 and p4Count == 3) or (p1Count == 3 and p2Count == 3 and p3Count == 3 and p4Count == 1):
        list2 = input4(piece1,piece2,piece3,piece4,p1Count,p2Count,p3Count,p4Count)
        list2.append(dice1)
        list2.append(dice2)
        oneZeroThree(*list2)
        if piece1.index > 72 or piece2.index > 72 or piece3.index > 72 or piece4.index > 72:
            print("Error 17")

    elif (p1Count == 1 and p2Count == 2 and p3Count == 3 and p4Count == 3) or (p1Count == 1 and p2Count == 3 and p3Count == 2 and p4Count == 3) or (p1Count == 1 and p2Count == 3 and p3Count == 3 and p4Count == 2) or (p1Count == 2 and p2Count == 1 and p3Count == 3 and p4Count == 3) or (p1Count == 2 and p2Count == 3 and p3Count == 1 and p4Count == 3) or (p1Count == 2 and p2Count == 3 and p3Count == 3 and p4Count == 1) or (p1Count == 3 and p2Count == 1 and p3Count == 2 and p4Count == 3) or (p1Count == 3 and p2Count == 1 and p3Count == 3 and p4Count == 2) or (p1Count == 3 and p2Count == 2 and p3Count == 1 and p4Count == 3) or (p1Count == 3 and p2Count == 2 and p3Count == 3 and p4Count == 1) or (p1Count == 3 and p2Count == 3 and p3Count == 1 and p4Count == 2) or (p1Count == 3 and p2Count == 3 and p3Count == 2 and p4Count == 1):
        list2 = input4(piece1,piece2,piece3,piece4,p1Count,p2Count,p3Count,p4Count)
        list2.append(dice1)
        list2.append(dice2)
        oneOneTwo(*list2)
        if piece1.index > 72 or piece2.index > 72 or piece3.index > 72 or piece4.index > 72:
            print("Error 21")

    elif (p1Count == 1 and p2Count == 2 and p3Count == 2 and p4Count == 3) or (p1Count == 1 and p2Count == 2 and p3Count == 3 and p4Count == 2) or (p1Count == 1 and p2Count == 3 and p3Count == 2 and p4Count == 2) or (p1Count == 2 and p2Count == 1 and p3Count == 2 and p4Count == 3) or (p1Count == 2 and p2Count == 1 and p3Count == 3 and p4Count == 2) or (p1Count == 3 and p2Count == 1 and p3Count == 2 and p4Count == 2) or (p1Count == 2 and p2Count == 2 and p3Count == 1 and p4Count == 3) or (p1Count == 2 and p2Count == 3 and p3Count == 1 and p4Count == 2) or (p1Count == 3 and p2Count == 2 and p3Count == 1 and p4Count == 2) or (p1Count == 2 and p2Count == 2 and p3Count == 3 and p4Count == 1) or (p1Count == 2 and p2Count == 3 and p3Count == 2 and p4Count == 1) or (p1Count == 3 and p2Count == 2 and p3Count == 2 and p4Count == 1):
        list2 = input4(piece1,piece2,piece3,piece4,p1Count,p2Count,p3Count,p4Count)
        list2.append(dice1)
        list2.append(dice2)
        oneTwoOne(*list2)
        if (piece1.index > 72 or piece2.index > 72 or piece3.index > 72 or piece4.index > 72):
            print("Error 33")


    elif (p1Count == 1 and p2Count == 2 and p3Count == 2 and p4Count == 2) or (p1Count == 2 and p2Count == 1 and p3Count == 2 and p4Count == 2) or (p1Count == 2 and p2Count == 2 and p3Count == 1 and p4Count == 2) or (p1Count == 2 and p2Count == 2 and p3Count == 2 and p4Count == 1):
        list2 = input4(piece1,piece2,piece3,piece4,p1Count,p2Count,p3Count,p4Count)
        list2.append(dice1)
        list2.append(dice2)
        oneThreeZero(*list2)
        if piece1.index > 72 or piece2.index > 72 or piece3.index > 72 or piece4.index > 72:
            print("Error 45")


    elif (p1Count == 1 and p2Count == 1 and p3Count == 3 and p4Count == 3) or (p1Count == 1 and p2Count == 3 and p3Count == 1 and p4Count == 3) or (p1Count == 1 and p2Count == 3 and p3Count == 3 and p4Count == 1) or (p1Count == 3 and p2Count == 1 and p3Count == 1 and p4Count == 3) or (p1Count == 3 and p2Count == 1 and p3Count == 3 and p4Count == 1) or (p1Count == 3 and p2Count == 3 and p3Count == 1 and p4Count == 1):
        list2 = input4(piece1,piece2,piece3,piece4,p1Count,p2Count,p3Count,p4Count)
        list2.append(dice1)
        list2.append(dice2)
        twoZeroTwo(*list2)
        if piece1.index > 72 or piece2.index > 72 or piece3.index > 72 or piece4.index > 72:
            print("Error 49")

        
    elif (p1Count == 1 and p2Count == 1 and p3Count == 2 and p4Count == 3) or (p1Count == 1 and p2Count == 1 and p3Count == 3 and p4Count == 2) or (p1Count == 1 and p2Count == 2 and p3Count == 1 and p4Count == 3) or (p1Count == 1 and p2Count == 3 and p3Count == 1 and p4Count == 2) or (p1Count == 1 and p2Count == 2 and p3Count == 3 and p4Count == 1) or (p1Count == 1 and p2Count == 3 and p3Count == 2 and p4Count == 1) or (p1Count == 2 and p2Count == 1 and p3Count == 1 and p4Count == 3) or (p1Count == 3 and p2Count == 1 and p3Count == 1 and p4Count == 2) or (p1Count == 2 and p2Count == 1 and p3Count == 3 and p4Count == 1) or (p1Count == 3 and p2Count == 1 and p3Count == 2 and p4Count == 1) or (p1Count == 2 and p2Count == 3 and p3Count == 1 and p4Count == 1) or (p1Count == 3 and p2Count == 2 and p3Count == 1 and p4Count == 1):
        list2 = input4(piece1,piece2,piece3,piece4,p1Count,p2Count,p3Count,p4Count)
        list2.append(dice1)
        list2.append(dice2)
        twoOneOne(*list2)
        if piece1.index > 72 or piece2.index > 72 or piece3.index > 72 or piece4.index > 72:
            print("Error 55")


    elif (p1Count == 1 and p2Count == 1 and p3Count == 2 and p4Count == 2) or (p1Count == 1 and p2Count == 2 and p3Count == 1 and p4Count == 2) or (p1Count == 1 and p2Count == 2 and p3Count == 2 and p4Count == 1) or (p1Count == 2 and p2Count == 1 and p3Count == 1 and p4Count == 2) or (p1Count == 2 and p2Count == 1 and p3Count == 2 and p4Count == 1) or (p1Count == 2 and p2Count == 2 and p3Count == 1 and p4Count == 1):
        list2 = input4(piece1,piece2,piece3,piece4,p1Count,p2Count,p3Count,p4Count)
        list2.append(dice1)
        list2.append(dice2)
        twoTwoZero(*list2)
        if piece1.index > 72 or piece2.index > 72 or piece3.index > 72 or piece4.index > 72:
            print("Error 67")

    
    elif (p1Count == 1 and p2Count == 1 and p3Count == 1 and p4Count == 3) or (p1Count == 1 and p2Count == 1 and p3Count == 3 and p4Count == 1) or (p1Count == 1 and p2Count == 3 and p3Count == 1 and p4Count == 1) or (p1Count == 3 and p2Count == 1 and p3Count == 1 and p4Count == 1):
        list2 = input4(piece1,piece2,piece3,piece4,p1Count,p2Count,p3Count,p4Count)
        list2.append(dice1)
        list2.append(dice2)
        threeZeroOne(*list2)
        if piece1.index > 72 or piece2.index > 72 or piece3.index > 72 or piece4.index > 72:
            print("Error 73")


    elif (p1Count == 1 and p2Count == 1 and p3Count == 1 and p4Count == 2) or (p1Count == 1 and p2Count == 1 and p3Count == 2 and p4Count == 1) or (p1Count == 1 and p2Count == 2 and p3Count == 1 and p4Count == 1) or (p1Count == 2 and p2Count == 1 and p3Count == 1 and p4Count == 1):
        list2 = input4(piece1,piece2,piece3,piece4,p1Count,p2Count,p3Count,p4Count)
        list2.append(dice1)
        list2.append(dice2)
        threeOneZero(*list2)
        if piece1.index > 72 or piece2.index > 72 or piece3.index > 72 or piece4.index > 72:
            print("Error 77")

    else:
        rando = random.randint(1,4)
        if rando == 1:
            piece1.index += min(dice1,dice2)
        elif rando == 2:
            piece2.index += min(dice1,dice2)
        elif rando == 3:
            piece3.index += min(dice1,dice2)
        else:
            piece4.index += min(dice1,dice2)
        if piece1.index > 72 or piece2.index > 72 or piece3.index > 72 or piece4.index > 72:
            print("Error 81")
            
    if piece1.index > 72 or piece2.index > 72 or piece3.index > 72 or piece4.index > 72:
        print("decideFor4")

def strat7(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2):
    print("\t\t\t\t\t\tstrat7")
    list1 = constructArguments(piece1,piece2,piece3,piece4,dice1,dice2)
    decideFor3(*list1)
    eatAll(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)
    print(piece1.color + "1: " + str(piece1.index) + " | " + piece2.color + "2: " + str(piece2.index) + " | " + piece3.color + "3: " + str(piece3.index) + " | " + piece4.color + "4: " + str(piece4.index))    
    if dice1 == dice2:
        print("Doubles")
        mainMove(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)

def strat8(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2):
    print("\t\t\t\t\t\tstrat8")
    decideFor4(piece1,piece2,piece3,piece4,dice1,dice2)
    eatAll(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)    
    print(piece1.color + "1: " + str(piece1.index) + " | " + piece2.color + "2: " + str(piece2.index) + " | " + piece3.color + "3: " + str(piece3.index) + " | " + piece4.color + "4: " + str(piece4.index))
    if dice1 == dice2:
        print("Doubles")
        mainMove(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)

def strat9(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2):
    print("\t\t\t\t\t\tstrat9")
    print("No move")
    print(piece1.color + "1: " + str(piece1.index) + " | " + piece2.color + "2: " + str(piece2.index) + " | " + piece3.color + "3: " + str(piece3.index) + " | " + piece4.color + "4: " + str(piece4.index))
    if dice1 == dice2:
        print("Doubles")
        mainMove(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)

def strat10(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2):
    print("\t\t\t\t\t\tstrat10")
    if dice1 == dice2:
        print("Doubles")
        freeFromJail(piece1,piece2,piece3,piece4)
        print("Out of Jail")
        stomp(piece1,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)
        print(piece1.color + "1: " + str(piece1.index) + " | " + piece2.color + "2: " + str(piece2.index) + " | " + piece3.color + "3: " + str(piece3.index) + " | " + piece4.color + "4: " + str(piece4.index))
        mainMove(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)
    else:
        pass
        print("No move")
        print(piece1.color + "1: " + str(piece1.index) + " | " + piece2.color + "2: " + str(piece2.index) + " | " + piece3.color + "3: " + str(piece3.index) + " | " + piece4.color + "4: " + str(piece4.index))
        

def strat11(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2):
    print("\t\t\t\t\t\tstrat11")
    if not (piece1.inJail or piece1.done or piece1.closeMove):
        decideFor1(piece1,dice1,dice2)
    elif not (piece2.inJail or piece2.done or piece2.closeMove):
        decideFor1(piece2,dice1,dice2)
    elif not (piece3.inJail or piece3.done or piece3.closeMove):
        decideFor1(piece3,dice1,dice2)
    else:
        decideFor1(piece4,dice1,dice2)
    eatAll(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)
    print(piece1.color + "1: " + str(piece1.index) + " | " + piece2.color + "2: " + str(piece2.index) + " | " + piece3.color + "3: " + str(piece3.index) + " | " + piece4.color + "4: " + str(piece4.index))
    if dice1 == dice2:
        print("Doubles")
        mainMove(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)

def strat12(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2):
    print("\t\t\t\t\t\tstrat12")
    print("One Piece")
    if not (piece1.inJail or piece1.done or piece1.closeMove):
        onePiece = piece1
    elif not (piece2.inJail or piece2.done or piece2.closeMove):
        onePiece = piece2
    elif not (piece3.inJail or piece3.done or piece3.closeMove):
        onePiece = piece3
    else:
        onePiece = piece4
    dist = 72 - onePiece.index
    if dist > 6:
        strat11(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2)
    else:
        rando = random.randint(1,6)
        print("Dice: " + str(rando))
        if rando <= dist:
            onePiece.index += rando
        else:
            pass
            print("No Move")
        print(piece1.color + "1: " + str(piece1.index) + " | " + piece2.color + "2: " + str(piece2.index) + " | " + piece3.color + "3: " + str(piece3.index) + " | " + piece4.color + "4: " + str(piece4.index))

def strat13(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2):
    print("\t\t\t\t\t\tstrat13")
    if dice1 == dice2:
        print("Doubles")
        freeFromJail(piece1,piece2,piece3,piece4)
        print("Out of Jail")
        stomp(piece1,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)
        if not (piece1.inJail or piece1.done or piece1.closeMove):
            piece1.index += dice1
        elif not (piece2.inJail or piece2.done or piece2.closeMove):
            piece2.index += dice1
        elif not (piece3.inJail or piece3.done or piece3.closeMove):
            piece3.index += dice1
        else:
            piece4.index += dice1
        eatAll(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)
        print(piece1.color + "1: " + str(piece1.index) + " | " + piece2.color + "2: " + str(piece2.index) + " | " + piece3.color + "3: " + str(piece3.index) + " | " + piece4.color + "4: " + str(piece4.index))
        mainMove(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12) 
    else:
        strat11(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2)
    

def strat14(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2):
    print("\t\t\t\t\t\tstrat14")
    print("One Piece")
    if not piece1.done:
        onePiece = piece1
    elif not piece2.done:
        onePiece = piece2
    elif not piece3.done:
        onePiece = piece3
    else:
        onePiece = piece4
    dist = 72 - onePiece.index
    rando = random.randint(1,6)
    print("Dice: " + str(rando))
    if rando <= dist:
        onePiece.index += rando
    else:
        pass
        print("No Move")
    print(piece1.color + "1: " + str(piece1.index) + " | " + piece2.color + "2: " + str(piece2.index) + " | " + piece3.color + "3: " + str(piece3.index) + " | " + piece4.color + "4: " + str(piece4.index))
    
def strat15(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2):
    print("\t\t\t\t\t\tstrat15")
    if dice1 == dice2:
        print("Doubles")
        freeFromJail(piece1,piece2,piece3,piece4)
        print("Out of Jail")
        stomp(piece1,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)
        listFree = []
        if not (piece1.inJail or piece1.done or piece1.closeMove):
            listFree.append(piece1)
        if not (piece2.inJail or piece2.done or piece2.closeMove):
            listFree.append(piece2)
        if not (piece3.inJail or piece3.done or piece3.closeMove):
            listFree.append(piece3)
        if not (piece4.inJail or piece4.done or piece4.closeMove):
            listFree.append(piece4)
        rando = random.randint(0,2)
        listFree[rando].index += dice1
        eatAll(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)
        print(piece1.color + "1: " + str(piece1.index) + " | " + piece2.color + "2: " + str(piece2.index) + " | " + piece3.color + "3: " + str(piece3.index) + " | " + piece4.color + "4: " + str(piece4.index))
        mainMove(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)
    else:
        list1 = constructArguments(piece1,piece2,piece3,piece4,dice1,dice2)
        decideFor3(*list1)
        eatAll(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)
        print(piece1.color + "1: " + str(piece1.index) + " | " + piece2.color + "2: " + str(piece2.index) + " | " + piece3.color + "3: " + str(piece3.index) + " | " + piece4.color + "4: " + str(piece4.index))    

                                                                                                                                                                                                                                                                                                                                                    

class redPiece:
    def __init__(self,num):
       self.index = 0
       self.favorability = 0 
       self.track = [101,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,69,70,71,72,73,74,75,76]
       self.coords = red(num)
       self.inJail = True
       self.done = False
       self.closeMove = False
       self.closeDice1 = False
       self.closeDice2 = False
       self.closeCombined = False
       self.color = 'red'

class greenPiece:
    def __init__(self,num):
       self.index = 0
       self.favorability = 0 
       self.track = [102,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,1,2,3,4,5,6,7,8,9,10,11,12,13,77,78,79,80,81,82,83,84]
       self.coords = green(num)
       self.inJail = True
       self.done = False
       self.closeMove = False
       self.closeDice1 = False
       self.closeDice2 = False
       self.closeCombined = False
       self.color = 'green'
       
class bluePiece:
    def __init__(self,num):
       self.index = 0
       self.favorability = 0 
       self.track = [103,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,85,86,87,88,89,90,91,92]
       self.coords = blue(num)
       self.inJail = True
       self.done = False
       self.closeMove = False
       self.closeDice1 = False
       self.closeDice2 = False
       self.closeCombined = False
       self.color = 'blue'

class yellowPiece:
    def __init__(self,num):
       self.index = 0
       self.favorability = 0 
       self.track = [104,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,93,94,95,96,97,98,99,100]
       self.coords = yellow(num)
       self.inJail = True
       self.done = False
       self.closeMove = False
       self.closeDice1 = False
       self.closeDice2 = False
       self.closeCombined = False
       self.color = 'yellow'

'''Parques numbers spaces meanings
track = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104]
1-68 : Main track from red start to behind red start
69-76 : Red safe zone
77-84: Green safe zone
85-92: Blue safe zone 
93-100: Yellow safe zone 
101: Red Jail
102: Green Jail
103: Blue Jail
104: Yellow Jail
'''

def piece1(piece):
    circle(piece.coords[piece.index][0],piece.coords[piece.index][1],15)

def piece2(piece):
    circle(piece.coords[piece.index][0],piece.coords[piece.index][1],15)
    line(piece.coords[piece.index][0],piece.coords[piece.index][1] - 7,piece.coords[piece.index][0],piece.coords[piece.index][1] + 7)
    
def piece3(piece):
    circle(piece.coords[piece.index][0],piece.coords[piece.index][1],15)
    line(piece.coords[piece.index][0],piece.coords[piece.index][1] - 7,piece.coords[piece.index][0],piece.coords[piece.index][1] + 7)
    line(piece.coords[piece.index][0] - 5,piece.coords[piece.index][1] - 3,piece.coords[piece.index][0] + 5,piece.coords[piece.index][1] - 3)
    
def piece4(piece):
    circle(piece.coords[piece.index][0],piece.coords[piece.index][1],15)
    line(piece.coords[piece.index][0],piece.coords[piece.index][1] - 7,piece.coords[piece.index][0],piece.coords[piece.index][1] + 7)
    line(piece.coords[piece.index][0] - 5,piece.coords[piece.index][1] - 3,piece.coords[piece.index][0] + 5,piece.coords[piece.index][1] - 3)
    line(piece.coords[piece.index][0] - 5,piece.coords[piece.index][1] + 3,piece.coords[piece.index][0] + 5,piece.coords[piece.index][1] + 3)
    
order = random.randint(1,4)
count = -2
finished = False
def draw():
    global order
    global count
    global finished
    frameRate(60)
    strokeWeight(2)
    board()
    if count < 0:
        count += 1
    elif not finished:
        if order == 1:
            print("Order A")
            if (red1.index < 72 or red2.index < 72 or red3.index < 72 or red4.index < 72) and (green1.index < 72 or green2.index < 72 or green3.index < 72 or green4.index < 72) and (blue1.index < 72 or blue2.index < 72 or blue3.index < 72 or blue4.index < 72) and (yellow1.index < 72 or yellow2.index < 72 or yellow3.index < 72 or yellow4.index < 72):
                mainMove(red1,red2,red3,red4,green1,green2,green3,green4,blue1,blue2,blue3,blue4,yellow1,yellow2,yellow3,yellow4)
                mainMove(green1,green2,green3,green4,blue1,blue2,blue3,blue4,yellow1,yellow2,yellow3,yellow4,red1,red2,red3,red4)
                mainMove(blue1,blue2,blue3,blue4,yellow1,yellow2,yellow3,yellow4,red1,red2,red3,red4,green1,green2,green3,green4)
                mainMove(yellow1,yellow2,yellow3,yellow4,red1,red2,red3,red4,green1,green2,green3,green4,blue1,blue2,blue3,blue4)
            else: 
                finished = True
        
        elif order == 2:
            print("Order B")
            if (red1.index < 72 or red2.index < 72 or red3.index < 72 or red4.index < 72) and (green1.index < 72 or green2.index < 72 or green3.index < 72 or green4.index < 72) and (blue1.index < 72 or blue2.index < 72 or blue3.index < 72 or blue4.index < 72) and (yellow1.index < 72 or yellow2.index < 72 or yellow3.index < 72 or yellow4.index < 72):
                mainMove(green1,green2,green3,green4,blue1,blue2,blue3,blue4,yellow1,yellow2,yellow3,yellow4,red1,red2,red3,red4)
                mainMove(blue1,blue2,blue3,blue4,yellow1,yellow2,yellow3,yellow4,red1,red2,red3,red4,green1,green2,green3,green4)
                mainMove(yellow1,yellow2,yellow3,yellow4,red1,red2,red3,red4,green1,green2,green3,green4,blue1,blue2,blue3,blue4)
                mainMove(red1,red2,red3,red4,green1,green2,green3,green4,blue1,blue2,blue3,blue4,yellow1,yellow2,yellow3,yellow4)
            else: 
                finished = True
        
        elif order == 3:
            print("Order C")
            if (red1.index < 72 or red2.index < 72 or red3.index < 72 or red4.index < 72) and (green1.index < 72 or green2.index < 72 or green3.index < 72 or green4.index < 72) and (blue1.index < 72 or blue2.index < 72 or blue3.index < 72 or blue4.index < 72) and (yellow1.index < 72 or yellow2.index < 72 or yellow3.index < 72 or yellow4.index < 72):
                mainMove(blue1,blue2,blue3,blue4,yellow1,yellow2,yellow3,yellow4,red1,red2,red3,red4,green1,green2,green3,green4)
                mainMove(yellow1,yellow2,yellow3,yellow4,red1,red2,red3,red4,green1,green2,green3,green4,blue1,blue2,blue3,blue4)
                mainMove(red1,red2,red3,red4,green1,green2,green3,green4,blue1,blue2,blue3,blue4,yellow1,yellow2,yellow3,yellow4)
                mainMove(green1,green2,green3,green4,blue1,blue2,blue3,blue4,yellow1,yellow2,yellow3,yellow4,red1,red2,red3,red4)
            else: 
                finished = True
        
        elif order == 4:
            print("Order D")
            if (red1.index < 72 or red2.index < 72 or red3.index < 72 or red4.index < 72) and (green1.index < 72 or green2.index < 72 or green3.index < 72 or green4.index < 72) and (blue1.index < 72 or blue2.index < 72 or blue3.index < 72 or blue4.index < 72) and (yellow1.index < 72 or yellow2.index < 72 or yellow3.index < 72 or yellow4.index < 72):
                mainMove(yellow1,yellow2,yellow3,yellow4,red1,red2,red3,red4,green1,green2,green3,green4,blue1,blue2,blue3,blue4)
                mainMove(red1,red2,red3,red4,green1,green2,green3,green4,blue1,blue2,blue3,blue4,yellow1,yellow2,yellow3,yellow4)
                mainMove(green1,green2,green3,green4,blue1,blue2,blue3,blue4,yellow1,yellow2,yellow3,yellow4,red1,red2,red3,red4)
                mainMove(blue1,blue2,blue3,blue4,yellow1,yellow2,yellow3,yellow4,red1,red2,red3,red4,green1,green2,green3,green4)
            else: 
                finished = True
    else:
        count += 1
            
    #red pieces 
    fill(255,0,0)
    piece1(red1)
    piece2(red2)
    piece3(red3)
    piece4(red4)

     
    #green pieces
    fill(0,255,0)
    piece1(green1)
    piece2(green2)
    piece3(green3)
    piece4(green4)

    
    #blue pieces
    fill(0,0,255)
    piece1(blue1)
    piece2(blue2)
    piece3(blue3)
    piece4(blue4)


    #yellow pieces 
    fill(255,255,0)
    piece1(yellow1)
    piece2(yellow2)
    piece3(yellow3)
    piece4(yellow4)

    print(order)
    print(count)
    if count > 15:
        count = -2
        finished = False
        order = random.randint(1,4)
        allPieces = [red1, red2, red3, red4, green1, green2, green3, green4, blue1, blue2, blue3,blue4, yellow1, yellow2, yellow3, yellow4]
        for i in allPieces:
            i.index = 0
