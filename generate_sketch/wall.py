from PIL import Image,ImageDraw, ImageFont
#import 

scale=2
brick={ 'width': 18*scale,'height':8*scale,'x_gap':2, 'y_gap':2}    
cap={ 'width': 18*scale,'height':4*scale,'x_gap':2, 'y_gap':2}    
margin_x=brick['width']*2
margin_y=brick['height']*2+300
offset_x=margin_x/2
offset_y=margin_y/2

class wall:
    def __init__(self,levels,grade):
        # reverse the array
        self.levels=levels[::-1] 

        self.grade=[]
        for item in grade:
            coord=self.grade_coordinate(item[0],item[1],item[2])
            self.grade.append(coord)
        print(self.grade)
        

        self.draw_wall()

    def get_brick_position(self,x,y):
        pos=None
        if y<len(self.levels):
            level=self.levels[y]
        else: 
            return pos
        if x>level[0]:
            return pos
        alignment = level[1] * (brick['width'] + brick['x_gap']) 
        y_position = y * (brick['height'] + brick['y_gap']) + offset_y
        x_position = x * (brick['width']  + brick['x_gap']) + alignment + offset_x

        pos=[int(x_position),
            int(y_position),
            int(x_position+brick['width']),
            int(y_position+brick['height'])]
        return pos

    def get_cap_position(self,x,y):
        pos=None
        if y<len(self.levels):
            level=self.levels[y]
        else: 
            return pos
        if x>level[0]:
            return pos
        alignment = level[1] * (brick['width'] + brick['x_gap']) 
        y_position = y * (brick['height'] + brick['y_gap']) + offset_y - cap['height'] - cap['y_gap']
        x_position = x * (cap['width']  + cap['x_gap']) + alignment + offset_x

        pos=[int(x_position),
            int(y_position),
            int(x_position+cap['width']),
            int(y_position+cap['height'])]
        return pos



    def draw_wall(self):
        self.levels_height=len(self.levels)

        
        # Calculate the wall width and height
        max_width= max(int(item[0]+item[1]) for item in self.levels)
        wall_width = max_width * (brick['width'] + brick['x_gap']) +margin_x
        wall_height = self.levels_height * (brick['height'] + brick['y_gap']) +margin_y

        # Create an image
        img = Image.new("RGBA", (wall_width, wall_height), "white")
        img2 = Image.new("RGBA", (wall_width, wall_height))
        draw = ImageDraw.Draw(img)
        draw2 = ImageDraw.Draw(img2)

        # Iterate through levels and draw bricks
        row=0
        blocks=0
        
        for level_idx in range(len(self.levels)):
            row=row+1
            for brick_idx in range(self.levels[level_idx][0]):
                blocks=blocks+1
                brick_pos=self.get_brick_position(brick_idx,level_idx)
                occluded=self.occluded_brick(brick_pos)
                if occluded:
                    fill="DarkGRAY"
                else: 
                    fill="BROWN"

                draw.rectangle(brick_pos,fill=fill)

        caps=0
        for brick_idx in range(self.levels[0][0]+1):
            caps=caps+1
            brick_pos=self.get_cap_position(brick_idx,0)
            brick_pos[0]=brick_pos[0]-cap['width']/3
            brick_pos[2]=brick_pos[2]-cap['width']/3
            if brick_idx==self.levels[0][0]:
                brick_pos[2]=brick_pos[2]-cap['width']/3
                    
            fill="BLACK"
            draw.rectangle(brick_pos,fill=fill)

        for level_idx in range(1,len(levels)):
            brick_pos=self.get_cap_position(0,level_idx)
            if level_idx==len(self.levels)-1:
                brick_pos[0]=brick_pos[0]
            else:
                brick_pos[0]=brick_pos[0]-cap['width']/4
            brick_pos[2]=brick_pos[2]-cap['width']/2
                    
            fill="BLACK"
            draw.rectangle(brick_pos,fill=fill)
            if level_idx==len(self.levels)-1:
                brick_pos[0]=brick_pos[0]+cap['width']/4
            else:
                brick_pos[0]=brick_pos[0]+cap['width']/2
            if level_idx==1:
                brick_pos[0]=brick_pos[0]+cap['width']+cap['x_gap']
                brick_pos[2]=brick_pos[2]+cap['width']+cap['x_gap']
            
            
            brick_pos[1]=brick_pos[1]-cap['height']-cap['y_gap'] +2
            brick_pos[3]=brick_pos[3]-cap['height']-cap['y_gap'] 
            draw.rectangle(brick_pos,fill=fill)

            if level_idx==1:
                brick_pos=self.get_cap_position(1,level_idx)
                brick_pos[0]=brick_pos[0]-cap['width']/2
                brick_pos[2]=brick_pos[2]-cap['width']/2
                draw.rectangle(brick_pos,fill=fill)


        brick_pos=self.get_cap_position(55,1)
        print (brick_pos)
        brick_pos[0]=brick_pos[0]+cap['width']/2
        brick_pos[2]=brick_pos[2]+cap['width']/2
        draw.rectangle(brick_pos,fill=fill)

        brick_pos[1]=brick_pos[1]-cap['height']
        brick_pos[2]=brick_pos[2]-cap['width']/2-cap['x_gap']
        brick_pos[3]=brick_pos[3]-cap['height']-cap['y_gap']
        draw.rectangle(brick_pos,fill=fill)

        brick_pos=self.get_cap_position(55,1)
        print (brick_pos)
        brick_pos[0]=brick_pos[0]+cap['width']/2+cap['width']+cap['x_gap']
        brick_pos[2]=brick_pos[2]+cap['width']/2+cap['width']
        draw.rectangle(brick_pos,fill=fill)
        
        
        brick_pos=self.get_cap_position(57,2)
        print (brick_pos)
        brick_pos[0]=brick_pos[0]+cap['width']/2
        brick_pos[2]=brick_pos[2]+cap['width']/2
        draw.rectangle(brick_pos,fill=fill)
    
        brick_pos[1]=brick_pos[1]-cap['height']
        brick_pos[2]=brick_pos[2]-cap['width']/2-cap['x_gap']
        brick_pos[3]=brick_pos[3]-cap['height']-cap['y_gap']
        draw.rectangle(brick_pos,fill=fill)
        
        brick_pos=self.get_cap_position(57,2)
        print (brick_pos)
        brick_pos[0]=brick_pos[0]+cap['width']/2+cap['width']+cap['x_gap']
        brick_pos[2]=brick_pos[2]+cap['width']/4+cap['width']+cap['x_gap']
        draw.rectangle(brick_pos,fill=fill)
    

        brick_pos=self.get_cap_position(59,3)
        print (brick_pos)
        brick_pos[0]=brick_pos[0]+cap['width']/2
        brick_pos[2]=brick_pos[2]
        draw.rectangle(brick_pos,fill=fill)

        brick_pos[1]=brick_pos[1]-cap['height']
        brick_pos[2]=brick_pos[2]-cap['width']/4
        brick_pos[3]=brick_pos[3]-cap['height']-cap['y_gap']
        print (brick_pos)
        
        draw.rectangle(brick_pos,fill=fill)




        # Draw the transparently shaded polygon
        draw2.polygon(self.grade, fill=(5, 127, 50, 200)) # RGBA color with 50% transparency
        out = Image.alpha_composite(img, img2)

        # Save the image
        out.save("wall.png")
        print(blocks)
        print("Wall image saved as wall.png")

    def occluded_brick(self,brick_pos):
        for level_idx in range(len(self.levels)):
            for brick_idx in range(self.levels[level_idx][0]):
                lower_brick_pos=self.get_brick_position(brick_idx,level_idx)
                if lower_brick_pos[0]>=brick_pos[0] and lower_brick_pos[0]<=brick_pos[2]  and (lower_brick_pos[1]>brick_pos[3] or  lower_brick_pos[3]>brick_pos[3]):
                    return True
        return None

                
    def grade_coordinate(self,y,x,loc):
        y=y-1
        x=x-1
        pos=self.get_brick_position(x,y)
        if pos==None:
            print("No brick for {0},{1}".format(x,y))
            return [0,0]
        if loc==0:
            return  (pos[0],pos[3])
        if loc==1:
            return  (pos[2],pos[1])
        if loc==2:
            return  (pos[0],pos[3]+300)
        if loc==3:
            return  (pos[2],pos[3]+300)
        if loc==4:
            return  (pos[2],pos[3])
        
        return pos



levels=[ [29,0],
        [38,.5], 
        [57,1],
        [60,1.5],
        [59,2],
        [57,2.5],
        [54,4]]

grade=[
        [7,1,0],
        [7,29,1],
        [6,38,1],
        [5,57,1],
        [4,60,4],
        [4,60,3],
        [7,1,2],
        ]

#[4,56,0],
#[4,59,0],
#[4,59,1]
#
wall(levels,grade)
    
