package com.bangkit.agroaid.repository

import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.asLiveData
import com.bangkit.agroaid.data.local.UserData
import com.bangkit.agroaid.data.local.UserDataPreference
import com.bangkit.agroaid.data.remote.response.LoginResponse
import com.bangkit.agroaid.data.remote.response.LoginResult
import com.bangkit.agroaid.data.remote.response.SignupResponse
import com.bangkit.agroaid.data.remote.retrofit.ApiService
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response

class AuthRepository private constructor(private val api: ApiService, private val user: UserDataPreference) {

    private val _signupResponse = MutableLiveData<SignupResponse>()
    val signupResponse: LiveData<SignupResponse> = _signupResponse

    private val _msgError = MutableLiveData<String>()
    val msgError: LiveData<String> = _msgError

    private val _loginResult = MutableLiveData<LoginResult>()
    val loginResult: LiveData<LoginResult> = _loginResult

    private val _loadingValidation = MutableLiveData<Boolean>()
    val loadingValidation: LiveData<Boolean> = _loadingValidation

    companion object {
        @Volatile
        private var instanceRepository: AuthRepository? = null
        fun getInstanceRepository(api: ApiService, user: UserDataPreference): AuthRepository =
            instanceRepository ?: synchronized(this) {
                instanceRepository ?: AuthRepository(api, user)
            }.also { instanceRepository = it }
    }

    fun userSignup(fullname: String, username: String, emailUser: String, passwordUser: String) {
        _loadingValidation.value = true
        val client = api.signup(fullname, username, emailUser, passwordUser)
        client.enqueue(object : Callback<SignupResponse> {
            override fun onResponse(
                call: Call<SignupResponse>,
                response: Response<SignupResponse>
            ) {
                _loadingValidation.value = false
                if (response.isSuccessful) {
                    if (response.body() != null) {
                        _signupResponse.value = response.body()
                    }
                } else {
                    _msgError.value = response.message()
                }
            }

            override fun onFailure(call: Call<SignupResponse>, t: Throwable) {
                _loadingValidation.value = false
                _msgError.value = "Error: " + t.message
            }

        })
    }

    fun getUser(): LiveData<UserData> {
        return user.getUser().asLiveData()
    }

    fun userLogin(userEmail: String, userPassword: String) {
        _loadingValidation.value = true
        val client = api.login(userEmail, userPassword)
        client.enqueue(object : Callback<LoginResponse> {
            override fun onResponse(call: Call<LoginResponse>, response: Response<LoginResponse>) {
                _loadingValidation.value = false
                if (response.isSuccessful) {
                    if (response.body() != null) {
                        _loginResult.value = response.body()?.user
                    }
                } else {
                    _msgError.value = response.message()
                }
            }

            override fun onFailure(call: Call<LoginResponse>, t: Throwable) {
                _loadingValidation.value = false
                _msgError.value = "Terjadi Kesalahan: " + t.message
            }
        })
    }

    suspend fun saveUser(userData: UserData) {
        this.user.saveUser(userData)
    }
}
