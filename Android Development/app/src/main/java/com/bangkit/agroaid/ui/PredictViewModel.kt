package com.bangkit.agroaid.ui

import androidx.lifecycle.LiveData
import androidx.lifecycle.ViewModel
import com.bangkit.agroaid.data.remote.response.PredictResponse
import com.bangkit.agroaid.helper.Status
import com.bangkit.agroaid.repository.DataRepository
import okhttp3.MultipartBody
import okhttp3.RequestBody

class PredictViewModel(private val dataRepository : DataRepository) : ViewModel() {
    fun predictDisease(plantType : String, image : MultipartBody.Part, tokenUser : String) : LiveData<Status<PredictResponse>> {
        return dataRepository.predictDisease(plantType, image, tokenUser)
    }
}