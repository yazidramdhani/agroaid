package com.bangkit.agroaid.ui

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import coil.load
import com.bangkit.agroaid.data.remote.response.PredictionHistory
import com.bangkit.agroaid.databinding.ActivityDetailBinding

@Suppress("DEPRECATION")
class PredictionDetailActivity : AppCompatActivity() {
    private val activityDetailBinding by lazy { ActivityDetailBinding.inflate(layoutInflater) }
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(activityDetailBinding.root)
        val dataPredictionHistory: PredictionHistory? = intent.getParcelableExtra(HISTORY_DETAIL)
        activityDetailBinding.apply {
            ivHistoryDetail.load(dataPredictionHistory?.photoUrl)
            tvSymptom.text = dataPredictionHistory?.symptom
            tvPrediction.text = dataPredictionHistory?.prediction
            tvCause.text = dataPredictionHistory?.cause
            tvDisease.text = dataPredictionHistory?.disease
            tvMedicine.text = dataPredictionHistory?.medicine
            tvSolution.text = dataPredictionHistory?.solution
        }
    }

    companion object {
        const val HISTORY_DETAIL = "history_detail"
    }
}