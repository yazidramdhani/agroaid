from flask import Flask, request, jsonify
from PIL import Image
import tensorflow as tf
from keras.utils import img_to_array, load_img
import keras
from model_inference.preprocess import inference_pred

app = Flask(__name__)

# TODO Add Model
grape_model = keras.models.load_model('./models/grape_model/grape_model.h5')
pepperbell_model = keras.models.load_model('./models/pepperbell_model/pepperbell_model.h5')
potato_model = keras.models.load_model('./models/potato_model/potato_model.h5')

cherry_model = keras.models.load_model('./models/cherry/cherry_model.h5', compile=False)
cherry_model.compile(optimizer=tf.optimizers.Adam(learning_rate=0.001), loss='categorical_crossentropy', metrics=['accuracy'])

peach_model = keras.models.load_model('./models/peach/peach_model.h5', compile=False)
peach_model.compile(optimizer=tf.optimizers.Adam(learning_rate=0.001), loss='categorical_crossentropy', metrics=['accuracy'])

strawberry_model = keras.models.load_model('./models/strawberry/strawberry_model.h5', compile=False)
strawberry_model.compile(optimizer=tf.optimizers.Adam(learning_rate=0.001), loss='categorical_crossentropy', metrics=['accuracy'])

apple_model = keras.models.load_model('./models/apple/model_apple.h5', compile=False)
apple_model.compile(optimizer=tf.optimizers.Adam(learning_rate=0.001), loss='categorical_crossentropy', metrics=['accuracy'])

corn_model = keras.models.load_model('./models/corn/model_corn.h5', compile=False)
corn_model.compile(optimizer=tf.optimizers.Adam(learning_rate=0.001), loss='categorical_crossentropy', metrics=['accuracy'])

tomato_model = keras.models.load_model('./models/tomato/model_tomato.h5', compile=False)
tomato_model.compile(optimizer=tf.optimizers.Adam(learning_rate=0.001), loss='categorical_crossentropy', metrics=['accuracy'])

# TODO Add Labels
file_paths = ['./labels/grape_labels.txt', 
              './labels/pepperbell_labels.txt', 
              './labels/potato_labels.txt',
              './labels/cherry_labels.txt',
              './labels/peach_labels.txt',
              './labels/strawberry_labels.txt',
              './labels/apple_labels.txt',
              './labels/corn_labels.txt',
              './labels/tomato_labels.txt']
label_lists = []

for file_path in file_paths:
    with open(file_path, 'r') as file:
        labels = [line.strip() for line in file.readlines()]
    label_lists.append(labels)

# TODO Sesuai urutan file_paths
grape_labels, pepperbell_labels, potato_labels, cherry_labels, peach_labels, strawberry_labels, apple_labels, corn_labels, tomato_labels = label_lists

@app.route('/')
def hello():
    helo = "Ini versi tensorflow: " + tf.__version__
    return helo

if __name__ == '__main__':
    app.run()

# TODO Add Route
@app.route('/predict-grape', methods=['POST'])
def prediction_grape():
    if 'image' not in request.files:
        return jsonify({'error':'No image found'})

    image_file = request.files['image']
    image = Image.open(image_file).convert('RGB')
    
    predicted_disease = inference_pred(grape_model, image, grape_labels)

    if predicted_disease == "Grape___Black_rot":
        return jsonify({
            'prediction' : 'Sakit',
            'disease': 'Black Rot',
            'cause': 'Black Rot adalah penyakit tanaman anggur yang disebabkan oleh jamur bernama Guignardia bidwellii.',
            'symptom':'Gejala utama Black Rot biasanya muncul pada buah, daun, dan tangkai anggur. Pada daun, black rot menyebabkan bercak berwarna cokelat yang dikelilingi oleh daerah kuning. Bercak ini juga bisa berkembang menjadi lebih besar dan mengakibatkan kerusakan pada daun. Tangkai anggur juga dapat terinfeksi, ditandai dengan munculnya bercak cokelat dan retakan.',
            'solution': 'Untuk mengendalikan black rot, praktik budidaya yang baik sangat penting, seperti memangkas dan membuang bagian tanaman yang terinfeksi, menjaga kebersihan kebun, serta pengendalian kelembaban.',
            'medicine': 'Penggunaan obat seperti fungisida dapat menjadi pilihan untuk mengendalikan penyakit ini. Fungisida yang efektif adalah yang mengandung bahan aktif seperti mankozeb, kaptan, ziram, atau klorotalonil.'})
    
    elif predicted_disease == "Grape___Esca_(Black_Measles)":
        return jsonify({
            'prediction' : 'Sakit',
            'disease': 'Esca Black Measles',
            'cause': 'Esca adalah penyakit serius pada tanaman anggur yang disebabkan oleh beberapa faktor,  termasuk patogen seperti jamur Phaeomoniella chlamydospora, jamur Phomopsis viticola atau Phomopsis spp., serta kondisi lingkungan dan faktor genetik tanaman.',
            'symptom':'Gejala awal Esca biasanya terlihat pada daun yang terinfeksi. Daun-daun tersebut dapat menunjukkan pola perubahan warna seperti bercak-bercak coklat atau merah, serta kemudian berkembang menjadi daun kering dan mati. Batang dan ranting juga dapat menunjukkan gejala berupa perubahan warna, seperti pewarnaan merah atau coklat. Infeksi yang lebih parah dapat menyebabkan keguguran daun, penurunan pertumbuhan, dan kematian tanaman.',
            'solution': 'Untuk mengendalikan penyakit ini, bakar dan buang semua bagian tamanan yang terinfeksi untuk mencegah penyebaran penyakit. Selain itu, pertahankan kondisi kelembaban yang seimbang untuk mengurangi kondisi yang mendukung pertumbuhan jamur. Pemupukan yang tepat demi memberi nutrisi yang seimbang kepada tanaman anggur juga perlu diterapkan agar tanaman anggur tetap sehat dan kuat.',
            'medicine': 'Tidak ada obat yang efektif untuk penyakit ini. Oleh sebab itu, mohon lakukan pencegahan dengan cara yang sudah dijelaskan sebelumnya.'})
    
    elif predicted_disease == "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)":
        return jsonify({
            'prediction' : 'Sakit',
            'disease': 'Leaf Blight Isariopsis',
            'cause': 'Penyakit Leaf Blight pada anggur disebabkan oleh infeksi jamur Guignardia aesculi, Stagonospora ampelophaga, atau Elsinoë ampelina. Infeksi ini biasanya terjadi saat kondisi cuaca lembap, dengan suhu yang hangat.',
            'symptom':'Gejala Leaf Blight pada terlihat pada bagian daun. Munculnya bercak berwarna cokelat atau hitam pada daun anggur. Bercak ini dapat membesar dan menggabung menjadi area yang lebih besar, mengakibatkan nekrosis pada daun. Daun yang terinfeksi dapat mengering, menggulung, atau bahkan gugur.',
            'solution': 'Untuk mengendalikan penyakit ini, hilangkan semua daun-daun yang terinfeksi dan membuangnya dari area tanaman untuk mencegah penyebaran penyakit. Selain itu, hindari juga penyiraman yang berlebihan untuk mengurangi kelembaban yang menyebabkan perkembangan jamur.',
            'medicine': 'Penggunaan obat fungisida tembaga seperti tembaga hidroksida (copper hydroxide) atau tembaga oksiklorida (copper oxychloride) dapat digunakan.'})
    
    else:
        return jsonify({
            'prediction': 'Sehat',
            'disease' : None,
            'cause': None,
            'symptom':None,
            'solution': None,
            'medicine': None})

@app.route('/predict-pepperbell', methods=['POST'])
def prediction_pepperbell():
    if 'image' not in request.files:
        return jsonify({'error':'No image found'})
    
    image_file = request.files['image']
    image = Image.open(image_file).convert('RGB')
    
    predicted_disease = inference_pred(pepperbell_model, image, pepperbell_labels)

    if predicted_disease == "Pepper,_bell___Bacterial_spot":
        return jsonify({
            'prediction' : 'Sakit',
            'disease': 'Bacterial Spot',
            'cause': 'Penyakit Bacterial Spot pada tanaman pepperbell disebabkan oleh bakteri Xanthomonas campestris pv. vesicatoria. Bakteri ini dapat menyebar melalui air, angin, serangga, dan alat pertanian yang terkontaminasi.',
            'symptom':'Gejala penyakit ini adalah munculnya bintik-bintik kecil berwarna cokelat, hitam, atau kecokelatan pada daun, batang, dan buah. Bintik-bintik ini dapat berkembang menjadi lesi berbentuk bercak dengan tengah berwarna cokelat gelap dan pinggiran yang lebih terang. Lesi dapat memperbesar dan menggabung, mengakibatkan kerusakan pada tanaman.',
            'solution': 'Untuk mengendalikan penyakit ini, jaga kebersihan kebun dengan membuang sisa-sisa tanaman yang terinfeksi. Hindari penggunaan alat pertanian yang terkontaminasi untuk mengurangi penyebaran bakteri. Hindari pengairan yang berlebihan dan pastikan ada sirkulasi udara yang baik di sekitar tanaman untuk mengurangi kondisi lembab yang disukai oleh bakteri.',
            'medicine': 'Penggunaan obat fungisida tembaga seperti tembaga hidroksida (copper hydroxide) atau tembaga oksiklorida (copper oxychloride) dapat digunakan.'})
    
    else:
        return jsonify({
            'prediction': 'Sehat',
            'disease': None,
            'cause': None,
            'symptom': None,
            'solution': None,
            'medicine': None})

@app.route('/predict-potato', methods=['POST'])
def prediction_potato():
    if 'image' not in request.files:
        return jsonify({'error':'No image found'})
    
    image_file = request.files['image']
    image = Image.open(image_file).convert('RGB')
    
    predicted_disease = inference_pred(potato_model, image, potato_labels)

    if predicted_disease == "Potato___Early_blight":
        return jsonify({
            'prediction': 'Sakit',
            'disease': 'Early Blight',
            'cause': 'Penyakit Early Blight pada tanaman kentang disebabkan oleh jamur bernama Alternaria solani. Jamur ini dapat menyebar melalui spora yang terbawa oleh angin, air, atau alat pertanian yang terkontaminasi.',
            'symptom':'Gejala penyakit ini adalah munculnya bercak-bercak berbentuk bulat atau oval pada daun kentang yang lebih tua. Bercak-bercak tersebut awalnya berwarna cokelat dengan tepi yang lebih gelap dan lebih terang di bagian tengahnya. Seiring perkembangan penyakit, bercak-bercak dapat memperbesar dan membentuk lesi yang mengering.',
            'solution': 'Untuk mengendalikan penyakit ini, penting untuk menghilangkan daun-daun yang terinfeksi atau tumbuhan yang telah mati dari area tanaman. Buang atau hancurkan bagian-bagian tanaman yang terinfeksi untuk mencegah penyebaran penyakit. Hindari menanam kentang atau tanaman dari keluarga solanaceae (misalnya, tomat, terong) pada lokasi yang sama setiap tahun. Rotasi tanaman dapat membantu mengurangi tingkat infeksi jamur. Penting juga untuk mengurangi kelembaban.',
            'medicine': 'Penggunaan obat fungisida seperti chlorothalonil dan mancozeb dapat digunakan.'})
    
    elif predicted_disease == "Potato___Late_blight":
        return jsonify({
            'prediction': 'Sakit',
            'disease': 'Late Blight',
            'cause': 'Penyakit Late Blight pada tanaman kentang disebabkan oleh jamur bernama Phytophthora infestans. Jamur ini dapat menyebar melalui spora yang terbawa oleh angin atau air, serta dapat menginfeksi daun, batang, dan buah kentang.',
            'symptom':'Munculnya bercak hijau keabu-abuan pada daun yang kemudian berubah menjadi cokelat kehitaman. Bercak-bercak ini berkembang dengan cepat dan daun-daun yang terinfeksi dapat melipat, mengering, dan menghitam.',
            'solution': 'Untuk mengendalikan penyakit ini, penting untuk menghilangkan daun-daun yang terinfeksi atau tumbuhan yang telah mati dari area tanaman. Buang atau hancurkan bagian-bagian tanaman yang terinfeksi untuk mencegah penyebaran penyakit. Hindari menanam kentang atau tanaman dari keluarga solanaceae (misalnya, tomat, terong) pada lokasi yang sama setiap tahun. Rotasi tanaman dapat membantu mengurangi tingkat infeksi jamur. Penting juga untuk mengurangi kelembaban.',
            'medicine': 'Penggunaan obat fungisida seperti mancozeb, chlorothalonil, fluazinam, atau fosetil-aluminium dapat digunakan.'})
    
    else:
        return jsonify({
            'prediction': 'Sehat',
            'disease': None,
            'cause': None,
            'symptom': None,
            'solution': None,
            'medicine': None})

@app.route('/predict-cherry', methods=['POST'])
def prediction_cherry():
    if 'image' not in request.files:
        return jsonify({'error':'No image found'})
    
    image_file = request.files['image']
    image = Image.open(image_file).convert('RGB')
    
    predicted_disease = inference_pred(cherry_model, image, cherry_labels)

    if predicted_disease == 'Cherry_(including_sour)___Powdery_mildew':
        return jsonify({
            'prediction':'Sakit',
            'disease':'Powdery Mildew',
            'cause':'Penyakit powdery mildew pada tanaman cherry disebabkan oleh infeksi jamur Erysiphe spp. atau Podosphaera spp.',
            'symptom':'Powdery mildew pada tanaman cherry ditandai dengan lapisan serbuk putih atau abu-abu pada daun, tangkai, dan buah, serta deformasi daun dan buah.',
            'solution':'Langkah-langkah pengendalian powdery mildew meliputi praktik sanitasi, pengaturan kelembaban yang baik, peningkatan sirkulasi udara, penggunaan bahan alami, dan jika diperlukan, penggunaan fungisida yang disetujui.',
            'medicine':'Beberapa fungisida yang umum digunakan untuk mengendalikan powdery mildew pada tanaman cherry antara lain azoxystrobin, myclobutanil, thiophanate-methyl, dan triadimefon, dengan mematuhi petunjuk dan dosis yang tertera pada label produk serta jangka waktu henti panen yang ditetapkan.'
        })
    else:
        return jsonify({
            'prediction': 'Sehat',
            'disease': None,
            'cause': None,
            'symptom': None,
            'solution': None,
            'medicine': None
        })

@app.route('/predict-peach', methods=['POST'])
def prediction_peach():
    if 'image' not in request.files:
        return jsonify({'error':'No image found'})
    
    image_file = request.files['image']
    image = Image.open(image_file).convert('RGB')
    
    predicted_disease = inference_pred(peach_model, image, peach_labels)

    if predicted_disease == 'Peach___Bacterial_spot':
        return jsonify({
            'prediction': 'Sakit',
            'disease': 'Bacterial Spot',
            'cause': 'Penyakit bacterial spot pada tanaman peach disebabkan oleh infeksi bakteri Xanthomonas arboricola pv. pruni.',
            'symptom': 'Bacterial spot pada tanaman peach ditandai dengan munculnya bercak-bercak berwarna cokelat atau hitam pada daun, tangkai, dan buah. Bercak-bercak ini seringkali memiliki pinggiran yang lebih gelap dan ukuran yang bervariasi. Munculnya lepuhan pada daun juga dapat terjadi.',
            'solution': 'Langkah-langkah pengendalian bacterial spot meliputi praktik sanitasi, pengaturan kelembaban yang baik, pemangkasan dan pembuangan bagian tanaman yang terinfeksi, penggunaan varietas tahan, dan penggunaan fungisida yang mengandung bahan aktif tembaga.',
            'medicine': 'Beberapa fungisida yang mengandung tembaga seperti kuprum oksiklorida atau kuprum hidroksida dapat digunakan untuk mengendalikan bacterial spot pada tanaman peach. Pastikan untuk mengikuti petunjuk dan dosis yang tertera pada label produk serta mematuhi jangka waktu henti panen yang ditetapkan.'
        })
    else:
        return jsonify({
            'prediction': 'Sehat',
            'disease': None,
            'cause': None,
            'symptom': None,
            'solution': None,
            'medicine': None
        })

@app.route('/predict-strawberry', methods=['POST'])
def prediction_strawberry():
    if 'image' not in request.files:
        return jsonify({'error':'No image found'})
    
    image_file = request.files['image']
    image = Image.open(image_file).convert('RGB')
    
    predicted_disease = inference_pred(strawberry_model, image, strawberry_labels)

    if predicted_disease == 'Strawberry___Leaf_scorch':
        return jsonify({
            'prediction': 'Sakit',
            'disease': 'Leaf Scorch',
            'cause': 'Penyakit leaf scorch pada tanaman strawberry dapat disebabkan oleh beberapa faktor, termasuk infeksi bakteri seperti Xanthomonas fragariae atau patogen jamur seperti Colletotrichum spp.',
            'symptom': 'Leaf scorch pada tanaman strawberry ditandai dengan kemerahan, pengeringan, dan kekeringan pada tepi daun. Daun-daun tersebut kemudian menjadi coklat, kering, dan mudah pecah. Bisa juga terjadi bercak-bercak berwarna merah kecoklatan atau ungu pada daun dan tangkai.',
            'solution': 'Langkah-langkah pengendalian leaf scorch meliputi praktik sanitasi, pengaturan kelembaban yang baik, pengelolaan irigasi yang tepat, pemangkasan dan pembuangan bagian tanaman yang terinfeksi, serta penggunaan varietas yang tahan terhadap penyakit.',
            'medicine': 'Penggunaan fungisida atau bakterisida yang sesuai dapat membantu mengendalikan penyakit leaf scorch pada tanaman strawberry. Pilihlah produk yang mengandung bahan aktif yang direkomendasikan untuk melawan patogen yang menyebabkan penyakit tersebut. Pastikan untuk mengikuti petunjuk dan dosis yang tertera pada label produk serta mematuhi jangka waktu henti panen yang ditetapkan.'
        })
    else:
        return jsonify({
            'prediction': 'Sehat',
            'disease': None,
            'cause': None,
            'symptom': None,
            'solution': None,
            'medicine': None
        })

@app.route('/predict-corn', methods=['POST'])
def prediction_corn():
    if 'image' not in request.files:
        return jsonify({'error':'No image found'})
    
    image_file = request.files['image']
    image = Image.open(image_file).convert('RGB')
    
    predicted_disease = inference_pred(corn_model, image, corn_labels)

    if predicted_disease == 'Corn_(maize)___Cercospora_leaf_spot':
        return jsonify({
            'prediction': 'Sakit',
            'disease': 'Maize Cercospora Leaf Spot',
            'cause': 'Penyakit Cercospora Leaf Spot pada tanaman jagung disebabkan oleh jamur patogen bernama Cercospora zeae-maydis.',
            'symptom': 'Gejala awalnya muncul sebagai bercak-bercak kecil berbentuk elips atau lonjong dengan warna putih atau abu-abu di daun jagung. Seiring perkembangan penyakit, bercak-bercak ini dapat memperbesar ukurannya dan berubah menjadi bercak berwarna coklat atau merah kecoklatan. Pada bercak yang lebih tua, sering terlihat pusaran hitam yang merupakan struktur jamur. Daun yang terinfeksi dapat mengering dan rontok.',
            'solution': 'Praktik rotasi tanaman dengan tanaman non-rumput, seperti kacang-kacangan atau sayuran lainnya, dapat membantu mengurangi penyebaran patogen dan memutus siklus penyakit. Hapus dan hancurkan sisa-sisa tanaman yang terinfeksi setelah panen untuk mengurangi sumber infeksi di musim berikutnya. Jaga kebersihan lahan dan peralatan pertanian untuk mengurangi penyebaran spora patogen. Hindari juga melakukan pengairan daun pada saat malam hari untuk mencegah kelembaban berlebih dan kondisi yang mendukung pertumbuhan jamur.',
            'medicine': 'Fungisida yang mengandung bahan aktif seperti mankozeb, klorotalonil, atau tembaga dapat digunakan untuk mengendalikan penyakit ini.'
        })
    
    elif predicted_disease == "Corn_(maize)___Common_rust_":
        return jsonify({
            'prediction': 'Sakit',
            'disease': 'Common Rust',
            'cause': 'Penyakit Common Rust pada tanaman jagung disebabkan oleh jamur patogen bernama Puccinia sorghi.',
            'symptom': 'Gejala awalnya muncul sebagai bercak-bercak kecil berwarna kuning atau oranye pucat pada permukaan atas daun jagung. Bercak-bercak ini kemudian berkembang menjadi pustula-pustula berukuran kecil yang berisi spora jamur. Pustula biasanya berwarna oranye hingga coklat kemerahan dan terlihat menonjol di permukaan daun. Daun yang terinfeksi dapat mengering, berubah menjadi kuning, dan mengalami penurunan hasil. Pada perkembangan penyakit yang lebih lanjut, pustula juga dapat muncul pada batang dan tongkol jagung. Pustula pada batang biasanya terlihat lebih besar dan terkadang berwarna hitam. Pada tongkol, pustula biasanya terletak di permukaan luar dan bisa mempengaruhi kualitas dan hasil panen.',
            'solution': 'Bersihkan lahan dari sisa-sisa tanaman yang terinfeksi setelah panen untuk mengurangi sumber infeksi di musim berikutnya. Lakukan rotasi tanaman dengan tanaman non-rumput, seperti kacang-kacangan atau sayuran lainnya, untuk memutus siklus penyakit dan mengurangi penyebaran patogen.',
            'medicine': 'Fungisida yang mengandung bahan aktif seperti triazol, strobilurin, atau triazol dan strobilurin kombinasi dapat digunakan untuk mengendalikan penyakit Common Rust.'
        })
    
    elif predicted_disease == "Corn_(maize)___Northern_Leaf_Blight":
        return jsonify({
            'prediction': 'Sakit',
            'disease': 'Northern Leaf Blight',
            'cause': 'Penyakit Northern Leaf Blight pada tanaman jagung disebabkan oleh jamur patogen bernama Setosphaeria turcica.',
            'symptom': 'Gejala awalnya muncul sebagai bercak-bercak berbentuk elips atau lonjong berwarna hijau keabu-abuan pada daun jagung. Bercak-bercak ini kemudian berkembang menjadi bercak-barcak coklat dengan tepi yang jelas. Bercak-bercak tersebut biasanya terletak di antara tulang daun dan dapat meluas seiring perkembangan penyakit. Daun yang terinfeksi dapat mengering dan mengalami nekrosis.',
            'solution': 'Bersihkan lahan dari sisa-sisa tanaman yang terinfeksi setelah panen untuk mengurangi sumber infeksi di musim berikutnya. Lakukan rotasi tanaman dengan tanaman non-rumput, seperti kacang-kacangan atau sayuran lainnya, untuk memutus siklus penyakit dan mengurangi penyebaran patogen.',
            'medicine': 'Fungisida yang mengandung bahan aktif seperti triazol, strobilurin, atau triazol dan strobilurin kombinasi dapat digunakan untuk mengendalikan penyakit Northern Leaf Blight'
        })
    
    else:
        return jsonify({
            'prediction': 'Sehat',
            'disease': None,
            'cause': None,
            'symptom': None,
            'solution': None,
            'medicine': None
        })
        
@app.route('/predict-apple', methods=['POST'])
def prediction_apple():
    if 'image' not in request.files:
        return jsonify({'error':'No image found'})
    
    image_file = request.files['image']
    image = Image.open(image_file).convert('RGB')
    
    predicted_disease = inference_pred(apple_model, image, apple_labels)

    if predicted_disease == "Apple___Apple_scab":
        return jsonify({
            'prediction' : 'Sakit',
            'disease': 'Apple scab',
            'cause': 'Penyakit scab pada tanaman apel disebabkan oleh jamur Venturia inaequalis. Jamur ini menyebar melalui spora yang terbentuk pada jaringan yang terinfeksi, serta melalui sisa-sisa tanaman yang terinfeksi pada musim dingin.',
            'symptom':'Daun yang terinfeksi scab biasanya memiliki bercak-bercak berwarna cokelat atau hitam yang kasar dan bersisik. Bercak tersebut dapat tumbuh dan menyatu seiring perkembangan penyakit.',
            'solution': 'Penting untuk menghilangkan dan membuang sisa-sisa tanaman yang terinfeksi, termasuk daun jatuh dan buah yang terserang scab. Ini akan membantu mengurangi sumber infeksi pada musim berikutnya. Mengurangi kepadatan buah pada pohon dapat membantu meningkatkan sirkulasi udara, mengurangi kelembaban, dan menghambat penyebaran jamur.',
            'medicine': 'Fungisida yang umumnya digunakan untuk mengendalikan scab pada apel termasuk mankozeb, klorotalonil, dan captan. Namun, penting untuk mengikuti petunjuk label dan rekomendasi spesifik dari ahli pertanian dalam penggunaan fungisida.'})
    
    elif predicted_disease=="Apple___Black_rot":
        return jsonify({
            'prediction': 'Sakit',
            'disease': 'Apple Black rot',
            'cause': 'Black rot pada tanaman apel disebabkan oleh jamur bernama Botryosphaeria obtusa. Infeksi terjadi terutama melalui luka pada buah atau bagian tanaman yang rusak, seperti tunas, ranting, atau daun yang terluka.',
            'symptom': 'Daun yang terinfeksi black rot mungkin memiliki bercak cokelat dengan tepi merah kecokelatan. Bercak tersebut dapat membesar dan menyebabkan nekrosis pada daun.',
            'solution': 'Menghilangkan dan membuang sisa-sisa tanaman yang terinfeksi black rot sangat penting untuk mengurangi sumber infeksi pada musim berikutnya. Ini termasuk membuang buah yang terinfeksi, daun jatuh, dan ranting yang terinfeksi.Mengurangi kepadatan buah pada pohon apel dapat membantu meningkatkan sirkulasi udara dan mengurangi kelembaban, yang dapat menghambat pertumbuhan jamur black rot.',
            'medicine': 'Fungisida yang umum digunakan untuk mengendalikan black rot pada apel termasuk fungisida berbahan aktif seperti kaptan, mankozeb, atau klorotalonil. Penting untuk mengikuti petunjuk label dan rekomendasi ahli pertanian untuk penggunaan yang efektif dan aman.'})
        
    elif predicted_disease=="Apple___Cedar_apple_rust":
         return jsonify({
            'prediction': 'Sakit',
            'disease': 'Apple Cedar Apple rust',
            'cause': 'Cedar apple rust disebabkan oleh jamur bernama Gymnosporangium juniperi-virginianae. Siklus hidup jamur ini melibatkan dua inang, yaitu tanaman apel (Malus spp.) dan pohon cedar atau juniper (Juniperus spp.). Infeksi terjadi ketika spora jamur yang dihasilkan oleh pohon cedar menyebar ke tanaman apel melalui angin.',
            'symptom': 'Daun yang terinfeksi cedar apple rust memiliki bercak kuning atau oranye dengan tepi yang lebih gelap. Bercak tersebut dapat berkembang menjadi area yang membesar dan mungkin terdapat benjolan kecil berwarna oranye pada permukaan bawah daun.',
            'solution': 'Menghilangkan tanaman cedar atau juniper yang berada dekat dengan tanaman apel dapat membantu mengurangi sumber infeksi. Ini termasuk menghapus pohon cedar yang terinfeksi atau menjaga jarak yang cukup antara tanaman apel dan cedar.Menjarangkan buah pada pohon apel dapat membantu meningkatkan sirkulasi udara dan mengurangi kelembaban, sehingga menghambat pertumbuhan jamur cedar apple rust.',
            'medicine': 'Fungisida seperti triadimefon, myclobutanil, dan mankozeb dapat digunakan untuk mengendalikan cedar apple rust pada tanaman apel. Penting untuk mengikuti petunjuk label dan rekomendasi ahli pertanian untuk penggunaan yang efektif dan aman.'})
         
    else:
        return jsonify({
            'prediction': 'Sehat',
            'disease': None,
            'cause': None,
            'symptom': None,
            'solution': None,
            'medicine': None
        })

@app.route('/predict-tomato', methods=['POST'])
def prediction_tomato():
    if 'image' not in request.files:
        return jsonify({'error':'No image found'})
    
    image_file = request.files['image']
    image = Image.open(image_file).convert('RGB')
    
    predicted_disease = inference_pred(tomato_model, image, tomato_labels)

    if predicted_disease == "Tomato___Bacterial_spot":
        return jsonify({
            "prediction": "Sakit",
            "disease": "Bacterial spot",
            "cause": "Infeksi bakteri Xanthomonas spp., terutama Xanthomonas campestris pv. vesicatoria",
            "symptom": "Bercak-bercak kecil berwarna cokelat atau hitam pada daun, batang, dan buah. Klorosis atau pucat di sekitar bercak. Gugurnya daun jika infeksi parah.",
            "solution": "Praktik sanitasi, Pengaturan kelembaban yang baik, Pemangkasan dan pembuangan bagian tanaman yang terinfeksi, Penggunaan varietas tahan, Rotasi tanaman",
            "medicine": "Fungisida atau bakterisida yang mengandung bahan aktif efektif melawan bakteri Xanthomonas spp., seperti tembaga, streptomisin sulfat, dan oksitetrasiklin"})
    
    elif predicted_disease=="Tomato___Early_blight":
        return jsonify({
            "prediction": "Sakit",
            "disease": "Early Blight",
            "cause": "Infeksi jamur Alternaria solani",
            "symptom": "Munculnya bercak cokelat dengan tepi yang berwarna kuning pada daun yang lebih tua. Bercak kemudian berkembang menjadi cincin berwarna cokelat dengan pusat yang mengering. Daun-daun terinfeksi juga dapat menguning, mengering, dan gugur.",
            "solution": "Praktik sanitasi, Pengaturan kelembaban yang baik, Pemangkasan dan pembuangan bagian tanaman yang terinfeksi, Penggunaan rotasi tanaman, Penggunaan mulsa, dan Penggunaan fungisida yang mengandung bahan aktif seperti klorotalonil atau mankozeb.",
            "medicine": "Fungisida yang mengandung bahan aktif seperti klorotalonil atau mankozeb dapat digunakan untuk mengendalikan penyakit Early Blight pada tanaman tomat."})
    
    elif predicted_disease=="Tomato___Late_blight":
        return jsonify({
            "prediction": "Sakit",
            "disease": "Late Blight",
            "cause": "Infeksi jamur Phytophthora infestans",
            "symptom": "Munculnya bercak kehijauan pada daun yang berkembang menjadi bercak berwarna cokelat kehitaman. Bercak tersebut dapat menyebar ke batang dan buah. Daun terinfeksi juga dapat mengalami layu dan kekuningan. Pada cuaca lembab, munculnya lapisan jamur berwarna putih pada permukaan bercak.",
            "solution": "Praktik sanitasi, Pengaturan kelembaban yang baik, Pemangkasan dan pembuangan bagian tanaman yang terinfeksi, Penggunaan rotasi tanaman, Penggunaan mulsa, Penggunaan fungisida yang mengandung bahan aktif seperti fosetyl-aluminium, fluazinam, atau mankozeb.",
            "medicine": "Fungisida yang mengandung bahan aktif seperti fosetyl-aluminium, fluazinam, atau mankozeb dapat digunakan untuk mengendalikan penyakit Late Blight pada tanaman tomat."})
    
    elif predicted_disease=="Tomato___Leaf_Mold":
        return jsonify({
             "prediction": "Sakit",
             "disease": "Leaf Mold",
             "cause": "Infeksi jamur Fulvia fulva (sebelumnya disebut Cladosporium fulvum)",
             "symptom": "Munculnya bercak kuning pucat pada daun yang berkembang menjadi bercak berwarna kuning atau kecokelatan yang terbungkus oleh lapisan abu-abu hingga cokelat. Lapisan jamur berwarna abu-abu atau cokelat juga terlihat pada bagian bawah daun.",
             "solution": "Praktik sanitasi, Pengaturan kelembaban yang baik, Pengaturan sirkulasi udara, Pemangkasan dan pembuangan bagian tanaman yang terinfeksi, Penggunaan varietas tahan, Penggunaan mulsa, Penggunaan fungisida yang mengandung bahan aktif seperti mankozeb, klorotalonil, atau copper oxychloride.",
             "medicine": "Fungisida yang mengandung bahan aktif seperti mankozeb, klorotalonil, atau copper oxychloride dapat digunakan untuk mengendalikan penyakit Leaf Mold pada tanaman tomat."})
    
    elif predicted_disease=="Tomato___Septoria_leaf_spot":
        return jsonify({
              "prediction": "Sakit",
              "disease": "Septoria Leaf Spot",
              "cause": "Infeksi jamur Septoria lycopersici",
              "symptom": "Munculnya bercak-bercak kecil berwarna cokelat atau hitam dengan tepi yang berwarna kuning pada daun bagian bawah tanaman. Bercak-bercak tersebut dapat membesar dan berkembang menjadi lesi berbentuk bulat dengan pusat yang lebih terang dan tepi yang berwarna cokelat.",
              "solution": "Praktik sanitasi, Pengaturan kelembaban yang baik, Pemangkasan dan pembuangan bagian tanaman yang terinfeksi, Penggunaan mulsa, Penggunaan fungisida yang mengandung bahan aktif seperti klorotalonil atau mankozeb.",
              "medicine": "Fungisida yang mengandung bahan aktif seperti klorotalonil atau mankozeb dapat digunakan untuk mengendalikan penyakit Septoria Leaf Spot pada tanaman tomat."})
    
    elif predicted_disease=="Tomato___Spider_mites Two-spotted_spider_mite":
        return jsonify({
               "prediction": "Sakit",
               "disease": "Two-spotted spider mite",
               "cause": "Serangan tungau merah (Tetranychus urticae)",
               "symptom": "Adanya daun yang menguning dan keriting, munculnya bintik-bintik kecil berwarna kuning atau putih di bagian atas daun, dan adanya jaring halus yang dihasilkan oleh tungau di antara daun.",
               "solution": "Praktik sanitasi, Pengaturan kelembaban yang baik, Pengelolaan gulma, Penggunaan predator alami seperti tungau predator (Phytoseiulus persimilis), Penggunaan insektisida yang sesuai.",
               "medicine": "Insektisida yang mengandung bahan aktif seperti abamectin, bifenthrin, atau acequinocyl dapat digunakan untuk mengendalikan Two-spotted spider mite pada tanaman tomat."})
    
    elif predicted_disease=="Tomato___Target_Spot":
        return jsonify({
            "prediction": "Sakit",
            "disease": "Target Spot",
            "cause": "Infeksi jamur Corynespora cassiicola",
            "symptom": "Munculnya bercak-bercak berbentuk bulat dengan pusat cokelat tua atau hitam dan tepi yang terang berwarna kuning atau cokelat pada daun, batang, dan buah. Bercak tersebut dapat berkembang menjadi lubang pada daun yang terinfeksi.",
            "solution": "Praktik sanitasi, Pengaturan kelembaban yang baik, Pemangkasan dan pembuangan bagian tanaman yang terinfeksi, Penggunaan fungisida yang mengandung bahan aktif seperti klorotalonil atau azoxystrobin.",
            "medicine": "Fungisida yang mengandung bahan aktif seperti klorotalonil atau azoxystrobin dapat digunakan untuk mengendalikan penyakit Target Spot pada tanaman tomat."})
    
    elif predicted_disease=="Tomato___Tomato_Yellow_Leaf_Curl_Virus":
        return jsonify({
            "prediction": "Sakit",
            "disease": "Tomato Yellow Leaf Curl Virus",
            "cause": "Infeksi virus Tomato yellow leaf curl virus (TYLCV)",
            "symptom": "Daun menjadi keriting ke atas, menguning, dan menggulung. Pertumbuhan tanaman terhambat, bunga dan buah menjadi berkurang, serta daun-daun yang terinfeksi dapat mengalami pembusukan.",
            "solution": "Praktik sanitasi, Pengendalian serangga vektor seperti whitefly (Bemisia tabaci), Penggunaan varietas tahan, Penggunaan mulsa, Penggunaan fungisida atau insektisida untuk mengendalikan vektor penyakit.",
            "medicine": "Tidak ada obat yang dapat menyembuhkan Tomato Yellow Leaf Curl Virus. Pengendalian serangga vektor dan praktik pengelolaan yang baik dapat membantu mengurangi penyebaran penyakit."})
    
    elif predicted_disease=="Tomato___Tomato_mosaic_virus":
        return jsonify({
             "prediction": "Sakit",
             "disease": "Tomato Mosaic Virus",
             "cause": "Infeksi virus Tomato mosaic virus (ToMV)",
             "symptom": "Daun-daun tanaman memiliki pola mosaik atau bercak-bercak kuning atau hijau gelap. Pertumbuhan tanaman terhambat, buah tidak berkembang dengan baik, dan tanaman dapat mengalami pembusukan.",
             "solution": "Praktik sanitasi, Pengendalian serangga vektor seperti aphid (Aphis spp.), Penggunaan varietas tahan, Penggunaan mulsa, Penggunaan fungisida atau insektisida untuk mengendalikan vektor penyakit.",
             "medicine": "Tidak ada obat yang dapat menyembuhkan Tomato Mosaic Virus. Pengendalian serangga vektor dan praktik pengelolaan yang baik dapat membantu mengurangi penyebaran penyakit."})
    else:
        return jsonify({
            'prediction': 'Sehat',
            'disease': None,
            'cause': None,
            'symptom': None,
            'solution': None,
            'medicine': None
        })          