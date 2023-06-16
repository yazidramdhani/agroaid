package com.bangkit.agroaid.ui

import android.Manifest
import android.content.Intent
import android.content.pm.PackageManager
import android.graphics.BitmapFactory
import android.net.Uri
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.provider.MediaStore
import android.view.View
import android.widget.Toast
import androidx.activity.result.contract.ActivityResultContracts
import androidx.core.app.ActivityCompat
import androidx.core.content.ContextCompat
import androidx.core.content.FileProvider
import androidx.lifecycle.ViewModelProvider
import com.bangkit.agroaid.data.remote.response.PredictionHistory
import com.bangkit.agroaid.databinding.ActivityMediaSelectBinding
import com.bangkit.agroaid.helper.*
import okhttp3.MediaType.Companion.toMediaTypeOrNull
import okhttp3.MultipartBody
import okhttp3.RequestBody.Companion.asRequestBody
import java.io.File
import android.util.Log
import kotlin.io.createTempFile

@Suppress("DEPRECATION")
class MediaSelectActivity : AppCompatActivity() {

    private lateinit var currentPath: String
    private lateinit var activityMediaSelectBinding: ActivityMediaSelectBinding
    private lateinit var predictViewModel: PredictViewModel
    private var file: File? = null

    override fun onRequestPermissionsResult(
        requestCode: Int,
        permissions: Array<String>,
        grantResults: IntArray
    ) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults)
        if (requestCode == REQUEST_CODE_PERMISSIONS) {
            if (!allPermissionsGranted()) {
                Toast.makeText(
                    this,
                    "Tidak mendapatkan permission.",
                    Toast.LENGTH_SHORT
                ).show()
                finish()
            }
        }
    }

    private fun allPermissionsGranted() = REQUIRED_PERMISSIONS.all {
        ContextCompat.checkSelfPermission(baseContext, it) == PackageManager.PERMISSION_GRANTED
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        activityMediaSelectBinding = ActivityMediaSelectBinding.inflate(layoutInflater)
        setContentView(activityMediaSelectBinding.root)
        if (!allPermissionsGranted()) {
            ActivityCompat.requestPermissions(
                this,
                REQUIRED_PERMISSIONS,
                REQUEST_CODE_PERMISSIONS
            )
        }

        activityMediaSelectBinding.btnCamera.setOnClickListener { startTakePhoto() }
        activityMediaSelectBinding.btnGallery.setOnClickListener { startGallery() }
        activityMediaSelectBinding.uploadButton.setOnClickListener { uploadStory() }
    }

    private fun startGallery() {
        val intent = Intent()
        intent.action = Intent.ACTION_GET_CONTENT
        intent.type = "image/*"
        val chooser = Intent.createChooser(intent, "Choose a Picture")
        launcherIntentGallery.launch(chooser)
    }

    private fun startTakePhoto() {
        val intent = Intent(MediaStore.ACTION_IMAGE_CAPTURE)
        intent.resolveActivity(packageManager)

        createTempFile(application).also {
            val photoURI: Uri = FileProvider.getUriForFile(
                this@MediaSelectActivity,
                "com.bangkit.agroaid",
                it
            )
            currentPath = it.absolutePath
            intent.putExtra(MediaStore.EXTRA_OUTPUT, photoURI)
            launcherIntentCamera.launch(intent)
        }
    }

    private val launcherIntentCamera = registerForActivityResult(
        ActivityResultContracts.StartActivityForResult()
    ) {
        if (it.resultCode == RESULT_OK) {
            val myFile = File(currentPath)
            file = myFile

            val result = BitmapFactory.decodeFile(file?.path)
            activityMediaSelectBinding.ivImage.setImageBitmap(result)
        }
    }

    private val launcherIntentGallery = registerForActivityResult(
        ActivityResultContracts.StartActivityForResult()
    ) { result ->
        if (result.resultCode == RESULT_OK) {
            val selectedImg: Uri = result.data?.data as Uri
            val myFile = uriToFile(selectedImg, this@MediaSelectActivity)
            file = myFile
            activityMediaSelectBinding.ivImage.setImageURI(selectedImg)
        }
    }

    private fun uploadStory() {
        val tokenUser = intent.getStringExtra(USER) as String
        predictViewModel = ViewModelProvider(
            this,
            HistoryViewModelFactory.getInstanceHistory(this)
        ).get(PredictViewModel::class.java)

        val plantType = intent.getStringExtra("plant_type") as String


        if (file != null) {
            val file = imageFileReduced(this.file as File)
            val requestImageFile = file.asRequestBody("image/jpeg".toMediaTypeOrNull())
            val imageMultipart: MultipartBody.Part = MultipartBody.Part.createFormData(
                "image",
                file.name,
                requestImageFile
            )

            predictViewModel.predictDisease(plantType, imageMultipart, tokenUser)
                .observe(this) { it ->
                    if (it != null) {
                        when (it) {
                            is Status.LoadingStatus -> activityMediaSelectBinding.pbPredict.visibility =
                                View.VISIBLE
                            is Status.SuccessStatus -> {
                                activityMediaSelectBinding.pbPredict.visibility = View.GONE
                                Toast.makeText(
                                    this@MediaSelectActivity,
                                    it.dataresponse.message,
                                    Toast.LENGTH_SHORT
                                ).show()
                                val dataHelp = it.dataresponse.data
                                val predictId = PredictionHistory(
                                    photoUrl = dataHelp.photoUrl,
                                    symptom = dataHelp.symptom,
                                    disease = dataHelp.disease,
                                    solution = dataHelp.disease,
                                    prediction = dataHelp.prediction,
                                    cause = dataHelp.cause,
                                    medicine = dataHelp.medicine,
                                    predictionId = dataHelp.predictionId,
                                    userId = dataHelp.userId
                                    )

                                Intent(this, PredictionDetailActivity::class.java).also {
                                    it.putExtra(PredictionDetailActivity.HISTORY_DETAIL, predictId)
                                    startActivity(it)
                                }
                            }
                            is Status.ErrorStatus -> {
                                activityMediaSelectBinding.pbPredict.visibility = View.GONE
                                Toast.makeText(
                                    this@MediaSelectActivity,
                                    it.messageerror,
                                    Toast.LENGTH_SHORT
                                ).show()
                                Log.d("masalah", it.messageerror)
                            }
                        }
                    }
                }
        }
    }

    companion object {
        private val REQUIRED_PERMISSIONS = arrayOf(Manifest.permission.CAMERA)
        private const val REQUEST_CODE_PERMISSIONS = 10
        const val USER = "user"
        const val CAMERA_X_RESULT = 200
    }
}