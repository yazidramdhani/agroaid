package com.bangkit.agroaid.repository

import androidx.lifecycle.LiveData
import androidx.lifecycle.liveData
import com.bangkit.agroaid.data.local.UserDataPreference
import com.bangkit.agroaid.data.remote.response.PredictResponse
import com.bangkit.agroaid.data.remote.response.PredictionHistory
import com.bangkit.agroaid.data.remote.retrofit.ApiConfig
import com.bangkit.agroaid.data.remote.retrofit.ApiService
import com.bangkit.agroaid.helper.Status
import okhttp3.MultipartBody
import okhttp3.RequestBody
import retrofit2.http.Path

class DataRepository private constructor(private val api: ApiService, private val user: UserDataPreference) {

    companion object {
        @Volatile
        private var instanceRepository: DataRepository? = null
        fun getInstanceRepository(api: ApiService, user: UserDataPreference) : DataRepository =
            instanceRepository ?: synchronized(this) {
                instanceRepository ?: DataRepository(api, user)
            }.also { instanceRepository = it }
    }

    suspend fun deleteUser() {
        user.deleteUser()
    }

    fun predictDisease(plantType: String, image: MultipartBody.Part, tokenUser: String) : LiveData<Status<PredictResponse>> = liveData {
        emit(Status.LoadingStatus)
        try {
            val statusResponse = ApiConfig.getApiService().predictDisease(plant = plantType , image = image, token = tokenUser)
            if (statusResponse != null){
                emit(Status.SuccessStatus(statusResponse))
            } else {
                emit(Status.ErrorStatus("Terjadi Kesalahan, Silahkan Coba Kembali"))
            }
        } catch (exception: Exception) {
            emit(Status.ErrorStatus(exception.message ?: "Unknown error"))
        }
    }

    fun getHistory(tokenUser : String) : LiveData<Status<List<PredictionHistory>>> = liveData {
        emit(Status.LoadingStatus)
        try {
            val statusResponse = ApiConfig.getApiService().getHistory(tokenUser)
            if (statusResponse.listHistory != null) {
                emit(Status.SuccessStatus(statusResponse.listHistory))
            } else {
                emit(Status.ErrorStatus("Terjadi Kesalahan"))
            }
        } catch (exception: Exception) {
            emit(Status.ErrorStatus(exception.message ?: "Unknown error"))
        }
    }
}