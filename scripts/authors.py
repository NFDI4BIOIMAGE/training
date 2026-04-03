our_authors = [
  "Haase, Robert",
  "Lampert, Mara", 
  "Huang, Yixin", 
  "Gihlein, Lea", 
  "Massei, Riccardo", 
  "Caporal, Clement", 
  "Wetzker, Conni", 
  "Zoccoler, Marcelo", 
  "Schrader, Andrea",
  "Wendt, Jens",
  "Zobel, Thomas",
  "Wetzker, Cornelia",
  "Fuchs, Vanessa",  
  "Müller, Maximilian",
  "Ahmadi, Mohsen",
  "Schmidt, Christian", 
  "Weidtkamp-Peters, Stefanie",
  "Kunis, Susanne",
  "Boissonnet, Tom",
  "Ferrando-May, Elisa",
  "Moore, Josh",
  "Tischer, Christian",
  "Bortolomeazzi, Michele"
]

temp = []
for author in our_authors:
    temp.append(author)
    if "," in author:
        lastname = author.split(",")[0].strip()
        firstname = author.split(",")[1].strip()
        temp.append(firstname + " " + lastname)

our_authors = temp