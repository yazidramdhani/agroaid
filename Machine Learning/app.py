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

# TODO Add Labels
file_paths = ['./labels/grape_labels.txt', 
              './labels/pepperbell_labels.txt', 
              './labels/potato_labels.txt',
              './labels/cherry_labels.txt',
              './labels/peach_labels.txt',
              './labels/strawberry_labels.txt']
label_lists = []

for file_path in file_paths:
    with open(file_path, 'r') as file:
        labels = [line.strip() for line in file.readlines()]
    label_lists.append(labels)

# TODO Sesuai urutan file_paths
grape_labels, pepperbell_labels, potato_labels, cherry_labels, peach_labels, strawberry_labels = label_lists

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
