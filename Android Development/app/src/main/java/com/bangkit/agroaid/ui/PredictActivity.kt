@file:Suppress("DEPRECATION")

package com.bangkit.agroaid.ui

import android.Manifest
import android.content.Intent
import android.content.pm.PackageManager
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import androidx.core.app.ActivityCompat
import androidx.core.content.ContextCompat
import androidx.lifecycle.ViewModelProvider
import com.bangkit.agroaid.data.remote.response.Data
import com.bangkit.agroaid.databinding.ActivityPredictBinding
import com.bangkit.agroaid.helper.HistoryViewModelFactory

class PredictActivity : AppCompatActivity() {
    private lateinit var historyViewModel: HistoryViewModel
    private lateinit var predictBinding: ActivityPredictBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        predictBinding = ActivityPredictBinding.inflate(layoutInflater)
        setContentView(predictBinding.root)

        historyViewModel = ViewModelProvider(
            this,
            HistoryViewModelFactory.getInstanceHistory(this)
        )[HistoryViewModel::class.java]

        if (::historyViewModel.isInitialized) {
            historyViewModel.getSessionUser().observe(this) { data ->
                if (data.userToken != "") {
                    predictBinding.btnApple.setOnClickListener {
                        val predict = Intent(this@PredictActivity, MediaSelectActivity::class.java)
                        predict.putExtra(
                            MediaSelectActivity.USER,
                            "Bearer ${data.userToken}"
                        )
                        predict.putExtra("plant_type", "apple")
                        startActivity(predict)
                    }
                    predictBinding.btnCherry.setOnClickListener {
                        val predict = Intent(this@PredictActivity, MediaSelectActivity::class.java)
                        predict.putExtra(
                            MediaSelectActivity.USER,
                            "Bearer ${data.userToken}"
                        )
                        predict.putExtra("plant_type", "cherry")
                        startActivity(predict)
                    }
                    predictBinding.btnCorn.setOnClickListener {
                        val predict = Intent(this@PredictActivity, MediaSelectActivity::class.java)
                        predict.putExtra(
                            MediaSelectActivity.USER,
                            "Bearer ${data.userToken}"
                        )
                        predict.putExtra("plant_type", "corn")
                        startActivity(predict)
                    }
                    predictBinding.btnGrape.setOnClickListener {
                        val predict = Intent(this@PredictActivity, MediaSelectActivity::class.java)
                        predict.putExtra(
                            MediaSelectActivity.USER,
                            "Bearer ${data.userToken}"
                        )
                        predict.putExtra("plant_type", "grape")
                        startActivity(predict)
                    }
                    predictBinding.btnPeach.setOnClickListener {
                        val predict = Intent(this@PredictActivity, MediaSelectActivity::class.java)
                        predict.putExtra(
                            MediaSelectActivity.USER,
                            "Bearer ${data.userToken}"
                        )
                        predict.putExtra("plant_type", "peach")
                        startActivity(predict)
                    }
                    predictBinding.btnPepperbell.setOnClickListener {
                        val predict = Intent(this@PredictActivity, MediaSelectActivity::class.java)
                        predict.putExtra(
                            MediaSelectActivity.USER,
                            "Bearer ${data.userToken}"
                        )
                        predict.putExtra("plant_type", "pepperbell")
                        startActivity(predict)
                    }
                    predictBinding.btnPotato.setOnClickListener {
                        val predict = Intent(this@PredictActivity, MediaSelectActivity::class.java)
                        predict.putExtra(
                            MediaSelectActivity.USER,
                            "Bearer ${data.userToken}"
                        )
                        predict.putExtra("plant_type", "potato")
                        startActivity(predict)
                    }
                    predictBinding.btnStrawberry.setOnClickListener {
                        val predict = Intent(this@PredictActivity, MediaSelectActivity::class.java)
                        predict.putExtra(
                            MediaSelectActivity.USER,
                            "Bearer ${data.userToken}"
                        )
                        predict.putExtra("plant_type", "strawberry")
                        startActivity(predict)
                    }
                    predictBinding.btnTomato.setOnClickListener {
                        val predict = Intent(this@PredictActivity, MediaSelectActivity::class.java)
                        predict.putExtra(
                            MediaSelectActivity.USER,
                            "Bearer ${data.userToken}"
                        )
                        predict.putExtra("plant_type", "tomato")
                        startActivity(predict)
                    }
                }
            }
        }
    }
}