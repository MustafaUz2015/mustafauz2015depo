import pygame
import random
pygame.init()
ekran = pygame.display.set_mode((800, 600),pygame.RESIZABLE)
class Renkler:
    pembe = (255, 192, 203)
    acik_kirmizi = (255, 99, 71)
    kirmizi = (255, 0, 0)
    kizil_turuncu = (255, 69, 0)
    turuncu = (255, 165, 0)
    turuncu_sari = (255, 140, 0)
    sari = (255, 255, 0)
    kapali_sari = (204, 204, 0)
    acik_yesil = (144, 238, 144)
    yesil = (0, 255, 0)
    koyu_yesil = (0, 100, 0)
    acik_mavi = (173, 216, 230)
    mavi = (0, 0, 255)
    kapali_mavi = (0, 0, 139)
    lacivert = (0, 0, 128)
    mor = (128, 0, 128)
    lilac = (200, 162, 200)
    beyaz = (255, 255, 255)
    acik_gri = (192, 192, 192)
    gri = (128, 128, 128)
    kapali_gri = (64, 64, 64)
    siyah = (0, 0, 0)
    kahverengi = (139, 69, 19)
    kahverengi_sari = (210, 105, 30)
    altınsarisi = (255, 255, 0)
    elmasrengi = (255, 215, 0)
    gümüşrengi = (192, 192, 192)
    zümrüt = (0, 255, 127)
buton1 = pygame.Rect(100, 100, 200, 50)
karakterkare = pygame.Rect(400, 300, 50, 50)
daire = pygame.Rect(500, 300, 50, 50)

pygame.display.set_caption("Daire Toplama Oyunu")
calisiyor = True

while calisiyor:

    ekran.fill(Renkler.kapali_gri)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            calisiyor = False
    pygame.font.init()
    font = pygame.font.SysFont(None, 36)
    text = font.render("Başlamak için butona tıklayın veya boşluk tuşuna basın.", True, Renkler.beyaz)
    ekran.blit(text, (100, 50))

    pygame.draw.rect(ekran, Renkler.kirmizi, buton1)
    
    if buton1.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] == 1 or pygame.key.get_pressed()[pygame.K_SPACE]:
        oyunekrani = pygame.display.set_mode((1000, 800),pygame.RESIZABLE)
        puan = 0
        karakter_rengi = Renkler.beyaz
        renkdeğisti = False
        alarmsuresi = 0
        
        while calisiyor:
            simdi = pygame.time.get_ticks()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    calisiyor = False
            oyunekrani.fill(Renkler.kapali_gri)
            pygame.font.init()
            font = pygame.font.SysFont(None, 36)
            
            textkarsilama = font.render("Oyuna hoşgeldiniz!", True, Renkler.beyaz)
            oyunekrani.blit(textkarsilama, ((1000 - textkarsilama.get_width()) / 2, 50))
            
            pygame.font.init()
            font = pygame.font.SysFont(None, 36)
            textbilgi = font.render(" Sarı daireleri toplayın (sağa d veya sağ ok, sola a veya sol ok, yukarı w, aşağı s)", True, Renkler.beyaz)
            oyunekrani.blit(textbilgi, ((1000 - textbilgi.get_width()) / 2, 100))
            
            pygame.font.init()
            font = pygame.font.SysFont(None, 36)
            textpuan = font.render(f"Puan: {puan}", True, Renkler.beyaz)
            oyunekrani.blit(textpuan, (50, 20))
            
            en_yakin_x = max(karakterkare.left, min(daire.centerx, karakterkare.right))
            en_yakin_y = max(karakterkare.top, min(daire.centery, karakterkare.bottom))
            if renkdeğisti == True:
                pygame.mixer.init()
                pygame.mixer.Sound("latent-rick-retro-arcade-level-up-552982.mp3").play()
                renkdeğisti = False
                alarmsuresi = pygame.time.get_ticks()
            if simdi - alarmsuresi > 1000:
                pass

            uzaklik_x = daire.centerx - en_yakin_x
            uzaklik_y = daire.centery - en_yakin_y
            toplam_uzaklik_karesi = (uzaklik_x ** 2) + (uzaklik_y ** 2)
            pygame.draw.rect(oyunekrani, karakter_rengi, karakterkare)
            pygame.draw.circle(oyunekrani, Renkler.sari, (daire.centerx, daire.centery), karakterkare.width // 2)

            if puan >= 0 and puan < 10:
                karakter_rengi = Renkler.beyaz
            elif puan == 10:
                karakter_rengi = Renkler.acik_yesil
                renkdeğisti = True
                puan += 1
            elif puan > 10 and puan < 50:
                karakter_rengi = Renkler.acik_yesil
            elif puan == 50:
                karakter_rengi = Renkler.yesil
                renkdeğisti = True
                puan += 1
            elif puan > 50 and puan < 100:
                karakter_rengi = Renkler.yesil
            elif puan == 100:
                karakter_rengi = Renkler.mavi
                renkdeğisti = True
                puan += 1
            elif puan > 100 and puan < 250:
                karakter_rengi = Renkler.mavi
            elif puan == 250:
                karakter_rengi = Renkler.kahverengi_sari
                renkdeğisti = True
                puan += 1
            elif puan > 250 and puan < 500:
                karakter_rengi = Renkler.kahverengi_sari
            elif puan == 500:
                karakter_rengi = Renkler.turuncu
                renkdeğisti = True
                puan += 1
            elif puan > 500 and puan < 750:
                karakter_rengi = Renkler.turuncu
            elif puan == 750:
                karakter_rengi = Renkler.siyah
                renkdeğisti = True
                puan += 1
            elif puan > 750 and puan < 1000:
                karakter_rengi = Renkler.siyah
            elif puan == 1000:
                karakter_rengi = Renkler.kirmizi
                renkdeğisti = True
                puan += 1
            elif puan > 1000:
                karakter_rengi = Renkler.kirmizi
                
            if toplam_uzaklik_karesi < ((daire.width / 2) ** 2):
                pygame.mixer.init()
                pygame.mixer.Sound("Pickup.wav").play()
                daire.x = random.randint(50, 950)
                daire.y = random.randint(100, 750)
                puan += 1

            if pygame.key.get_pressed()[pygame.K_w] or pygame.key.get_pressed()[pygame.K_UP]:
                karakterkare.y -= 2
            if pygame.key.get_pressed()[pygame.K_s] or pygame.key.get_pressed()[pygame.K_DOWN]:
                karakterkare.y += 2
            if pygame.key.get_pressed()[pygame.K_a] or pygame.key.get_pressed()[pygame.K_LEFT]:
                karakterkare.x -= 2
            if pygame.key.get_pressed()[pygame.K_d] or pygame.key.get_pressed()[pygame.K_RIGHT]:
                karakterkare.x += 2
            pygame.display.flip()
        
    pygame.display.flip()
pygame.quit()
