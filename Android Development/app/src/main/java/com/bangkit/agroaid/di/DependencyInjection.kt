package com.bangkit.agroaid.di

import android.content.Context
import androidx.datastore.core.DataStore
import androidx.datastore.preferences.core.Preferences
import androidx.datastore.preferences.preferencesDataStore
import com.bangkit.agroaid.data.local.UserDataPreference
import com.bangkit.agroaid.data.remote.retrofit.ApiConfig
import com.bangkit.agroaid.repository.AuthRepository
import com.bangkit.agroaid.repository.DataRepository

private val Context.dataStore : DataStore<Preferences> by preferencesDataStore(name = "session")

object DependencyInjection {
    fun provideRepositoryAuthentication(ctx: Context) : AuthRepository {
        val api = ApiConfig.getApiService()
        val user= UserDataPreference.getInstanceUser(ctx.dataStore)
        return AuthRepository.getInstanceRepository(api, user)
    }

    fun provideRepositoryStory(ctx: Context) : DataRepository {
        val api = ApiConfig.getApiService()
        val user= UserDataPreference.getInstanceUser(ctx.dataStore)
        return DataRepository.getInstanceRepository(api, user)
    }
}