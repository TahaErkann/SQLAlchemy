from models import session, User

#List all users
def get_all_users():
    users = session.query(User).all()
    if users:
        print("Tüm kayıtlı kullanıcılar:")
        for user in users:
            print(f"ID: {user.id}, Kullanıcı Adı: {user.username}, Mail: {user.email} Oluşturulma Tarihi: {user.created_at}")
    else:
        print("Kayıtlı kullanıcı bulunamadı.")
        

#List a specific user by ID
def get_user_by_id(user_id):
    user = session.query(User).filter_by(id=user_id).first()
    if user:
            print(f"Kullanıcı bulundu:\nID: {user.id}, Kullanıcı Adı: {user.username}, Mail: {user.email}, Oluşturulma Tarihi: {user.created_at}")
    else:
            print(f"ID {user_id} numaralı kullanıcı bulunamadı.")
            
if __name__ == "__main__":
    print("1 - Tüm kullanıcıları listele")
    print("2 - Belirli bir kullanıcıyı listele. ID Seçiniz.")
    
    choice = input("Seçiminizi yapınız (1 veya 2)")
    
    if choice == "1":
        get_all_users()
    
    elif choice == "2":
        try:
            user_id = int(input("Kullanıcı ID'sini giriniz:"))
            get_user_by_id(user_id)
        except ValueError:
            print("Lütfen geçerli bir sayı giriniz.")
            
    else:
        print("Geçersiz seçim. Lütfen 1 veya 2 rakamlarından birini seçiniz.")