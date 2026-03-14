"""
Harcama Takip Uygulaması
MS323 Betik Dilleri Dersi Final Projesi
Bu program harcama eklemenizi ve toplamı görmenizi sağlar.
"""

from datetime import datetime

class HarcamaKayitlari:
    """
    Bu sınıf tüm harcama işlemlerini ve kayıtlarını yönetir.
    """
    
    def __init__(self):
        """Program ilk açıldığında boş bir harcama listesi hazırlar."""
        self.harcamalar = []
    
    def harcama_ekle(self):
        """
        Kullanıcıdan gerekli bilgileri alıp yeni bir harcama ekler.
        """
        print("\n***** HARCAMA KAYDET *****")
        
        # Açıklama girişi
        while True:
            try:
                aciklama = input("Açıklama (boş olamaz): ").strip()
                if not aciklama:
                    print("Hata: Açıklama boş olamaz!")
                    continue
                break
            except KeyboardInterrupt:
                print("\nİşlem iptal edildi.")
                return
            except Exception as e:
                print(f"Beklenmeyen hata: {e}")
                continue
        
        # Tutar girişi
        while True:
            try:
                tutar_str = input("Tutar (pozitif sayı): ").strip()
                tutar = float(tutar_str)
                if tutar <= 0:
                    print("Hata: Tutar pozitif bir sayı olmalıdır!")
                    continue
                break
            except ValueError:
                print("Hata: Geçerli bir sayı giriniz!")
            except KeyboardInterrupt:
                print("\nİşlem iptal edildi.")
                return
            except Exception as e:
                print(f"Beklenmeyen hata: {e}")
                continue
        
        # Tarih girişi
        while True:
            try:
                varsayilan_tarih = datetime.now().strftime("%d.%m.%Y")
                tarih_str = input(f"Tarih (GG.AA.YYYY) [Varsayılan: {varsayilan_tarih}]: ").strip()
                
                if not tarih_str:
                    tarih = datetime.now()
                else:
                    tarih = datetime.strptime(tarih_str, "%d.%m.%Y")
                break
            except ValueError:
                print("Hata: Geçerli bir tarih formatı giriniz (GG.AA.YYYY)!")
            except KeyboardInterrupt:
                print("\nİşlem iptal edildi.")
                return
            except Exception as e:
                print(f"Beklenmeyen hata: {e}")
                continue
        
        # Harcamayı listeye ekle
        harcama = {
            'aciklama': aciklama,
            'tutar': tutar,
            'tarih': tarih
        }
        self.harcamalar.append(harcama)
        print(f"\n[OK] Harcama başarıyla eklendi!")
    
    def harcamalari_listele(self):
        """
        Yapılan bütün harcamaları ekrana sırasıyla alt alta yazdırır.
        """
        print("\n*** HARCAMALAR LİSTESİ ***")
        
        if not self.harcamalar:
            print("Şu anda kayıtlı hiçbir harcama bulunmamaktadır.")
            return
        
        # Harcama tutarına göre büyükten küçüğe sıralama kodu
        sirali_harcamalar = sorted(self.harcamalar, key=lambda x: x['tutar'], reverse=True)
        
        print(f"\n{'No':<5} {'Tarih':<12} {'Açıklama':<30} {'Tutar':<15}")
        print("-" * 65)
        
        for idx, harcama in enumerate(sirali_harcamalar, 1):
            tarih_str = harcama['tarih'].strftime("%d.%m.%Y")
            print(f"{idx:<5} {tarih_str:<12} {harcama['aciklama']:<30} {harcama['tutar']:>10.2f} TL")
    
    def toplam_harcama_goster(self):
        """
        Şimdiye kadar yapılan toplam harcama tutarını hesaplayıp gösterir.
        """
        print("\n--- TOPLAM HARCAMA ---")
        
        if not self.harcamalar:
            print("Henüz kayıtlı harcama bulunmamaktadır.")
            print("Toplam Harcama: 0.00 TL")
            return
        
        toplam = sum(harcama['tutar'] for harcama in self.harcamalar)
        print(f"Toplam Harcama: {toplam:.2f} TL")
        print(f"Kayıtlı Harcama Sayısı: {len(self.harcamalar)}")
    
    def menu_goster(self):
        """
        Ekrana seçenekleri yazar ve kullanıcının seçim yapmasını bekler.
        """
        print("\n" + "=" * 40)
        print("   HARCAMA TAKİP SİSTEMİ")
        print("=" * 40)
        print("1 - Harcama Ekle")
        print("2 - Harcamaları Listele")
        print("3 - Toplam Harcamayı Göster")
        print("0 - Çıkış")
        print("=" * 40)
        
        try:
            secim = input("Seçiminiz: ").strip()
            return secim
        except KeyboardInterrupt:
            print("\n\nProgram sonlandırılıyor...")
            return '0'
        except Exception as e:
            print(f"Hata: {e}")
            return None
    
    def calistir(self):
        """
        Programı başlatır ve kapatılana kadar çalışmasını sağlar.
        """
        print("\n*** HARCAMA TAKİP UYGULAMASINA HOŞGELDİNİZ ***\n")
        
        while True:
            secim = self.menu_goster()
            
            if secim == '1':
                self.harcama_ekle()
            elif secim == '2':
                self.harcamalari_listele()
            elif secim == '3':
                self.toplam_harcama_goster()
            elif secim == '0':
                print("\nProgram sonlandırılıyor...")
                print("Başarılı çıkış! Görüşmek üzere.")
                break
            elif secim is None:
                continue 
            else:
                print("\n[!] Geçersiz seçim! Lütfen 0-3 arası bir değer giriniz.")

def main():
    """Programın başladığı yerdir ve ana sınıfı çalıştırır."""
    try:
        uygulama = HarcamaKayitlari()
        uygulama.calistir()
    except Exception as e:
        print(f"Program başlatılırken hata oluştu: {e}")
    finally:
        print("\nProgram kapatıldı.")

if __name__ == "__main__":
    main()