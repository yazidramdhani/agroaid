package com.bangkit.agroaid.helper

import android.content.Context
import androidx.lifecycle.ViewModel
import androidx.lifecycle.ViewModelProvider
import com.bangkit.agroaid.di.DependencyInjection
import com.bangkit.agroaid.repository.AuthRepository
import com.bangkit.agroaid.ui.auth.LoginViewModel
import com.bangkit.agroaid.ui.auth.SignupViewModel

class AuthViewModelFactory private constructor(private val repository: AuthRepository)
    : ViewModelProvider.NewInstanceFactory() {

    @Suppress("UNCHECKED_CAST")
    override fun <T : ViewModel> create(tClass: Class<T>): T {
        if (tClass.isAssignableFrom(SignupViewModel::class.java)) {
            return  SignupViewModel(repository) as T
        }

        if (tClass.isAssignableFrom(LoginViewModel::class.java)) {
            return  LoginViewModel(repository) as T
        }

        throw IllegalArgumentException("Unknown ViewModel class: " + tClass.name)
    }

    companion object {
        @Volatile
        private var authenticationInstance: AuthViewModelFactory? = null
        fun getAuthenticationInstance(ctx: Context): AuthViewModelFactory =
            authenticationInstance ?: synchronized(this) {
                authenticationInstance ?: AuthViewModelFactory(DependencyInjection.provideRepositoryAuthentication(ctx))
            }.also { authenticationInstance = it }
    }
}