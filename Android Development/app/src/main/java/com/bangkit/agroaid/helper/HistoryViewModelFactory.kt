package com.bangkit.agroaid.helper

import android.content.Context
import androidx.lifecycle.ViewModel
import androidx.lifecycle.ViewModelProvider
import com.bangkit.agroaid.di.DependencyInjection
import com.bangkit.agroaid.ui.PredictViewModel
import com.bangkit.agroaid.repository.AuthRepository
import com.bangkit.agroaid.repository.DataRepository
import com.bangkit.agroaid.ui.HistoryViewModel

class HistoryViewModelFactory private constructor(private val repository: DataRepository, private val authRepository: AuthRepository)
    : ViewModelProvider.NewInstanceFactory() {
    @Suppress("UNCHECKED_CAST")
    override fun <T : ViewModel> create(tClass: Class<T>): T {
        if (tClass.isAssignableFrom(HistoryViewModel::class.java)) {
            return  HistoryViewModel(repository, authRepository) as T
        } else if (tClass.isAssignableFrom(PredictViewModel::class.java)) {
            return  PredictViewModel(repository) as T
        }

        throw IllegalArgumentException("Unknown ViewModel class: " + tClass.name)
    }

    companion object {
        @Volatile
        private var storyInstance: HistoryViewModelFactory? = null
        fun getInstanceHistory(ctx: Context): HistoryViewModelFactory =
            storyInstance ?: synchronized(this) {
                storyInstance ?: HistoryViewModelFactory(DependencyInjection.provideRepositoryStory(ctx), DependencyInjection.provideRepositoryAuthentication(ctx))
            }.also { storyInstance = it }
    }
}