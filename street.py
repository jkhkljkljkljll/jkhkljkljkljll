import pygame
import random
pygame.init()
endgame,window,fighter_x,fighter_y,immage,immage1,immage2,immage3,immage4,value1,immage5,fighter_x1,fighter_y1,f1,mass,time,gravity,d1,d2,fight_x,fight_y,immage7,immage8,immage9,immage10,immage11,immage12,value2,d,immage13,immage14,immage15,immage18,immage19,fonn,immage20,immage21,immage22,immage23,immage24,immage25="true",pygame.display.set_mode((800,600)),200,300,pygame.image.load("C:\\Users\\harsh\\Downloads\\356aa6271df24728d5dc16dc609432d5-removebg-preview (1).png"),pygame.image.load("C:\\Users\\harsh\\Downloads\\OIP-removebg-preview.png"),pygame.image.load("C:\\Users\\harsh\\Downloads\\ryu-high-low-block-removebg-preview.png"),pygame.image.load("C:\\Users\\harsh\\Downloads\\OIP-removebg-preview (3).png"),pygame.image.load("C:\\Users\\harsh\\Downloads\\OIP-removebg-preview (1).png"),0,pygame.image.load("C:\\Users\\harsh\\Downloads\\enhanced-buzz-31578-1444931339-28-removebg-preview.png"),500,300,305000,20,1,50,"true","false",200,450,pygame.image.load("C:\\Users\\harsh\\Downloads\\OIP-removebg-preview (4).png"),pygame.image.load("C:\\Users\\harsh\\Downloads\\OIP-removebg-preview (3) (1).png"),pygame.image.load("C:\\Users\\harsh\\Downloads\\356aa6271df24728d5dc16dc609432d5-removebg-preview.png"),pygame.image.load("C:\\Users\\harsh\\Downloads\\OIP-removebg-preview (1) (1).png"),pygame.image.load("C:\\Users\\harsh\\Downloads\\ryu-high-low-block-removebg-preview (1).png"),pygame.image.load("C:\\Users\\harsh\\Downloads\\enhanced-buzz-31578-1444931339-28-removebg-preview (1).png"),0,0,pygame.image.load("C:\\Users\\harsh\\Downloads\\istockphoto-641509146-170667a.jpg"),pygame.image.load("C:\\Users\\harsh\\Downloads\\R (1).png"),pygame.image.load("C:\\Users\\harsh\\Downloads\\R (1) (1).png"),pygame.image.load("C:\\Users\\harsh\\Downloads\\frame_00_delay-0.06s-removebg-preview.png"),pygame.image.load("C:\\Users\\harsh\\Downloads\\frame_00_delay-0.png"),pygame.font.SysFont(None,77),pygame.image.load("C:\\Users\\harsh\\Downloads\\screenshot-from-Street-Fighter-2-In-this-screenshot-Ryu-and-Ken-are-facing-off-removebg-preview.png"),pygame.image.load("C:\\Users\\harsh\\Downloads\\OIP-removebg-preview (5).png"),pygame.image.load("C:\\Users\\harsh\\Downloads\\screenshot-from-Street-Fighter-2-In-this-screenshot-Ryu-and-Ken-are-facing-off-removebg-preview (1).png"),pygame.image.load("C:\\Users\\harsh\\Downloads\\OIP-removebg-preview (5) (1).png"),pygame.image.load("C:\\Users\\harsh\\Downloads\\6c19fd9c3206359019a1d5325650a454.png"),pygame.image.load("C:\\Users\\harsh\\Downloads\\6c19fd9c3206359019a1d5325650a454 (1).png")
imm,imm1,imm2,imm3,imm4,imm5,f2,imm7,imm8,imm9,imm10,imm11,imm12,imm13,imm14,imm15,a,val,imm18,imm19,fonny,fonny2,fighterval,val1,val2,imm20,imm21,yt,imm22,imm23,yt1,yt2,dd,ff,acount,imm24,axe,imm25,fonny3,tt1,tt2=pygame.transform.scale(immage,[190,220]).convert_alpha(),pygame.transform.scale(immage1,[170,200]).convert_alpha(),pygame.transform.scale(immage2,[230,230]).convert_alpha(),pygame.transform.scale(immage3,[200,190]).convert_alpha(),pygame.transform.scale(immage4,[430,430]).convert_alpha(),pygame.transform.scale(immage5,[170,170]).convert_alpha(),f1,pygame.transform.scale(immage7,[170,200]).convert_alpha(),pygame.transform.scale(immage8,[200,190]).convert_alpha(),pygame.transform.scale(immage9,[190,220]).convert_alpha(),pygame.transform.scale(immage10,[430,430]).convert_alpha(),pygame.transform.scale(immage11,[230,230]).convert_alpha(),pygame.transform.scale(immage12,[170,170]).convert_alpha(),pygame.transform.scale(immage13,[800,600]),pygame.transform.scale(immage14,[180,180]),pygame.transform.scale(immage15,[180,180]),0,0,pygame.transform.scale(immage18,[200,200]),pygame.transform.scale(immage19,[200,200]),fonn.render("player 1",True,(255,255,0)),fonn.render("player 2",True,(255,255,0)),[[255,0,0,10,20,300,25],[255,0,0,480,20,300,25],[0,0,255,fighter_x,fighter_y,15,15],[255,0,0,fighter_x1,fighter_y1,15,15]],10,10,pygame.transform.scale(immage20,[200,200]),pygame.transform.scale(immage21,[190,190]),0,pygame.transform.scale(immage22,[200,200]),pygame.transform.scale(immage23,[190,190]),0,0,0,0,0,pygame.transform.scale(immage24,[190,90]),0,pygame.transform.scale(immage25,[190,90]),fonn.render("knock out",True,(255,0,0)),0,0
def imp1(f,mass,gravity,time,fight_x,fight_y,value,d,a,val,yt,ff,fightervall,endgame,tt):
    if(x.type==pygame.KEYDOWN  and value<=5 and tt<=0):
        fight_x,fight_y,f,value,val,yt,endgame,tt=l.force(fight_y,fight_x,x,value,d,a,yt,endgame,tt)
    elif(fight_y<300 and tt<=0):
        fight_x,fight_y,f,value,val,yt,endgame,tt=l.hello(fight_x,fight_y,f,mass,gravity,time,x,d,yt,endgame,tt)
    elif(fight_y>=300):
        fight_x,fight_y,f,value,val,yt,endgame,tt=l.hello1(val,yt,fight_x,ff,fightervall,endgame,tt)
    return fight_x,fight_y,f,value,val,yt,endgame,tt
def imp2(f,mass,gravity,time,fight_x,fight_y,value,d,a,val,yt,dd,fightervall,endgame,tt):
    if(x.type==pygame.KEYDOWN  and value<=5 and tt<=0):
        fight_x,fight_y,f,value,val,yt,endgame,tt=h.force(fight_y,fight_x,x,value,d,a,yt,endgame,tt)
    elif(fight_y<300 and tt<=0):
        fight_x,fight_y,f,value,val,yt,endgame,tt=h.hello(fight_x,fight_y,f,mass,gravity,time,x,d,yt,endgame,tt)
    elif(fight_y>=300):
        fight_x,fight_y,f,value,val,yt,endgame,tt=h.hello1(val,yt,fight_x,dd,fightervall,endgame,tt)
    return fight_x,fight_y,f,value,val,yt,endgame,tt
class H:
    def force(self,fight_y,fight_x,x,value,d,a,yt,endgame,tt):
        if((x.key==pygame.K_BACKSPACE and d==0 or d==1) and fight_y>=300):
            window.blit(imm,[fight_x,fight_y-40])
        elif(x.key==pygame.K_RETURN and d==0 or d==2):
            window.blit(imm1,[fight_x+30,fight_y-20])
        elif((x.key==pygame.K_TAB and d==0 or d==3) and fight_y>=300):
            window.blit(imm2,[fight_x,fight_y-17])
        elif((x.key==pygame.K_ESCAPE and d==0 or d==4) and fight_y>=300):
            window.blit(imm3,[fight_x-20,fight_y])
        elif((x.key==pygame.K_RIGHT and d==0 or d==7) and fight_y>=300):
            fight_x+=8+a
            window.blit(imm14,[fight_x,fight_y])
        elif((x.key==pygame.K_LEFT and d==0 or d==8) and fight_y>=300):
            fight_x-=8-a
            window.blit(imm14,[fight_x,fight_y])
        elif((x.key==pygame.K_DELETE and d==0 or d==9) and fight_y>=300 and yt==0):
            window.blit(imm20,[fight_x,fight_y])
            yt=1
        pygame.time.wait(30)
        value=value+2
        return fight_x,fight_y,f,value,val,yt,endgame,tt
    def hello(self,fight_x,fight_y,f,mass,gravity,time,x,d,yt,endgame,tt):
        window.blit(imm4,[fight_x-250,fight_y-150])
        if((x.type==pygame.KEYDOWN and x.key==pygame.K_RIGHT and d==0) or d==5):
            fight_x+=0.7
        f=f-mass*gravity
        al=f/mass
        v=al/time
        dis=v*time
        fight_y=fight_y-dis/15000
        if(yt>0 and fight_x+150+yt<ff):
            window.blit(imm21,[fight_x+150+yt,270])
            yt+=0.9
        return fight_x,fight_y,f,value,val,yt,endgame,tt
    def hello1(self,val,yt,fight_x,dd,fightervall,endgame,tt):
        if(fightervall<=0):
            window.blit(imm24,[fight_x-50,fight_y+100])
            window.blit(fonny3,[300,200])
            tt+=1
        elif(val<=6):
            window.blit(imm18,[fight_x,fight_y])
            pygame.time.wait(25)
        elif(val>6):
            window.blit(imm5,[fight_x,300])
            val=10
            if(yt>0 and fight_x<800 and fight_x+150+yt<ff):
                window.blit(imm21,[fight_x+yt+150,270])
                yt+=0.9
            else:
                yt=0
        return fight_x,fight_y,f,value,val,yt,endgame,tt
class L:
    def force(self,fight_y,fight_x,x,value,d,a,yt,endgame,tt):
        if((x.key==pygame.K_BACKSPACE and d==0 or d==1) and fight_y>=300):
            window.blit(imm9,[fight_x-40,fight_y-40])
        elif(x.key==pygame.K_RETURN and d==0 or d==2):
            window.blit(imm7,[fight_x-50,fight_y-20])
        elif((x.key==pygame.K_TAB and d==0 or d==3) and fight_y>=300):
            window.blit(imm11,[fight_x-30,fight_y-20])
        elif((x.key==pygame.K_ESCAPE and d==0 or d==4) and fight_y>=300):
            window.blit(imm8,[fight_x,fight_y+5])
        elif((x.key==pygame.K_RIGHT and d==0 or d==7) and fight_y>=300):
            fight_x+=8+a
            window.blit(imm15,[fight_x,fight_y])
        elif((x.key==pygame.K_LEFT and d==0 or d==8) and fight_y>=300):
            fight_x-=8-a
            window.blit(imm15,[fight_x,fight_y])
        elif((x.key==pygame.K_DELETE and d==0 or d==9) and fight_y>=300 and yt==0):
            window.blit(imm22,[fight_x,fight_y])
            yt=1
        pygame.time.wait(30)
        value+=2
        return fight_x,fight_y,f,value,val,yt,endgame,tt
    def hello(self,fight_x,fight_y,f,mass,gravity,time,x,d,yt,endgame,tt):
        window.blit(imm10,[fight_x,fight_y-150])
        if((x.type==pygame.KEYDOWN and x.key==pygame.K_LEFT and d==0) or d==5):
            fight_x-=0.7
        f=f-mass*gravity
        al=f/mass
        v=al/time
        dis=v*time
        fight_y=fight_y-dis/15000
        if(yt>0 and fight_x-150-yt>dd):
            window.blit(imm23,[fight_x-yt-150,270])
            yt+=0.9
        return fight_x,fight_y,f,value,val,yt,endgame,tt
    def hello1(self,val,yt,fight_x,ff,fightervall,endgame,tt):
        if(fightervall<=0):
            window.blit(imm25,[fight_x-50,fight_y+100])
            window.blit(fonny3,[300,200])
            tt+=1
        elif(val<=6):
            window.blit(imm19,[fight_x,300])
            pygame.time.wait(25)
        elif(val>6):
            window.blit(imm12,[fight_x,300])
            val=10
            if(yt>0 and fight_x<800 and fight_x>0 and fight_x-150-yt>dd):
                window.blit(imm23,[(fight_x-150)-yt,270])
                yt+=0.9
            else:
                yt=0
        return fight_x,fight_y,f,value,val,yt,endgame,tt
h,l=H(),L()
while(endgame=="true"):
    window.blit(imm13,[0,0])
    for p,q,r,s,t,u,v in fighterval:
        pygame.draw.rect(window,(p,q,r),[s,t,u,v])
    window.blit(fonny,[10,40])
    window.blit(fonny2,[480,40])
    if(fighter_x-fighter_x1<=0 and fighter_y>=300 and fighter_y1>=300):
        d1,d2=1,0
    elif(fighter_x-fighter_x1>0 and fighter_y>=300 and fighter_y1>=300):
        d1,d2=0,1
    for x in pygame.event.get():
        if(x.type==pygame.QUIT):
            endgame="false"
        elif(x.type==pygame.KEYDOWN):
            if(fighter_y1<300 and abs(fighter_x-fighter_x1)>50 and abs(fighter_x-fighter_x1)<155):
                d,a=random.choice([2,5]),0
            elif(abs(fighter_x-fighter_x1)>50 and abs(fighter_x-fighter_x1)<155 and (x.key==pygame.K_BACKSPACE or x.key==pygame.K_RETURN or x.key==pygame.K_TAB or x.key==pygame.K_RIGHT or x.key==pygame.K_DELETE)):
                d,a=random.choice([3,6,4,7,1,9]),0
            elif(abs(fighter_x-fighter_x1)>50 and abs(fighter_x-fighter_x1)<155 and (x.key==pygame.K_ESCAPE or x.key==pygame.K_SPACE or x.key==pygame.K_LEFT or x.key==pygame.K_DELETE)):
                d,a=random.choice([8,6,2,3,7]),0
            elif(abs(fighter_x-fighter_x1)<=50):
                d,a=random.choice([7,8]),20                                                                                                                                  
            elif(abs(fighter_x-fighter_x1)>=155):
                if(acount%5==0):
                    d,a=random.choice([7,8,9]),0
                else:
                    d,a=random.choice([7,8]),0
            if(x.key==pygame.K_SPACE and fighter_y>=300):
                f1,mass,gravity,time,fighter_y=344000,20,65,1,fighter_y-1
            if(d==6 and fighter_y1>=300):
                f2,mass,gravity,time,fighter_y1=344000,20,65,1,fighter_y1-1
            value1,value2=0,0
    if(d1==1):
        fight_x,fight_y,f,value,val,yt,dd=fighter_x,fighter_y,f1,value1,val1,yt1,fighter_x
        fight_x,fight_y,f,value,val,yt1,endgame,tt1=imp2(f,mass,gravity,time,fight_x,fight_y,value,0,0,val,yt,dd,fighterval[0][5],endgame,tt1)
        fighter_x,fighter_y,f1,value1,fighterval[2][3],fighterval[2][4],val1=fight_x,fight_y,f,value,fight_x+70,fight_y+190,val
    elif(d2==1):
        fight_x,fight_y,f,value,val,yt,dd=fighter_x1,fighter_y1,f2,value2,val2,yt2,fighter_x1
        fight_x,fight_y,f,value,val,yt2,endgame,tt2=imp2(f,mass,gravity,time,fight_x,fight_y,value,d,a,val,yt,dd,fighterval[1][5],endgame,tt2)
        fighter_x1,fighter_y1,f2,value2,fighterval[3][3],fighterval[3][4],val2=fight_x,fight_y,f,value,fight_x+70,fight_y+190,val
    if(d1==0):
        fight_x,fight_y,f,value,val,yt,ff=fighter_x,fighter_y,f1,value1,val1,yt1,fighter_x
        fight_x,fight_y,f,value,val,yt1,endgame,tt1=imp1(f,mass,gravity,time,fight_x,fight_y,value,0,0,val,yt,ff,fighterval[0][5],endgame,tt1)
        fighter_x,fighter_y,f1,value1,fighterval[2][3],fighterval[2][4],val1=fight_x,fight_y,f,value,fight_x+70,fight_y+190,val
    elif(d2==0):
        fight_x,fight_y,f,value,val,yt,ff=fighter_x1,fighter_y1,f2,value2,val2,yt2,fighter_x1
        fight_x,fight_y,f,value,val,yt2,endgame,tt2=imp1(f,mass,gravity,time,fight_x,fight_y,value,d,a,val,yt,ff,fighterval[1][5],endgame,tt2)
        fighter_x1,fighter_y1,f2,value2,fighterval[3][3],fighterval[3][4],val2=fight_x,fight_y,f,value,fight_x+70,fight_y+190,val
    if(x.type==pygame.KEYDOWN and (x.key==pygame.K_BACKSPACE or x.key==pygame.K_ESCAPE or x.key==pygame.K_RETURN or x.key==pygame.K_DELETE) and (abs(fighter_x-fighter_x1)<110 and abs(fighter_y-fighter_y1)<70 and d!=3)):
        val2,fighterval[1][5]=0,fighterval[1][5]-5
    if(x.type==pygame.KEYDOWN and (d==1 or d==2 or d==4 or d==9) and (abs(fighter_x-fighter_x1)<110 and abs(fighter_y-fighter_y1)<70 and x.key!=pygame.K_TAB)):
        val1,d,fighterval[0][5]=0,50,fighterval[0][5]-25
    if(tt1>600 or tt2>600):
        endgame="false"
    val1,val2,acount=val1+1,val2+1,acount+1
    pygame.display.update()
pygame.quit()

