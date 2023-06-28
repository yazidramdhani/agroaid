package com.bangkit.agroaid.data.local

import androidx.datastore.core.DataStore
import androidx.datastore.preferences.core.Preferences
import androidx.datastore.preferences.core.edit
import androidx.datastore.preferences.core.stringPreferencesKey
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.map

class UserDataPreference(private val dataUser: DataStore<Preferences>) {

    fun getUser() : Flow<UserData> {
        return dataUser.data.map {
            UserData(
                it[FULL_NAME] ?: "" ,
                it[USER_ID] ?: "" ,
                it[USER_NAME] ?: "" ,
                it[USER_TOKEN] ?: ""
            )
        }
    }

    suspend fun saveUser(userData: UserData) {
        dataUser.edit {
            it[FULL_NAME] = userData.fullName
            it[USER_ID] = userData.userId
            it[USER_NAME] = userData.userName
            it[USER_TOKEN] = userData.userToken
        }
    }

    suspend fun deleteUser() {
        dataUser.edit {
            it.clear()
        }
    }

    suspend fun login(token : String) {
        dataUser.edit {
            it[USER_TOKEN] = token
        }
    }

    companion object {
        @Volatile
        private var INSTANCE_USER: UserDataPreference? = null
        private val FULL_NAME = stringPreferencesKey("fullname")
        private val USER_ID = stringPreferencesKey("id")
        private val USER_NAME = stringPreferencesKey("name")
        private val USER_TOKEN = stringPreferencesKey("token")

        fun getInstanceUser(user: DataStore<Preferences>): UserDataPreference {
            return INSTANCE_USER ?: synchronized(this) {
                val userDataPreference = UserDataPreference(user)
                INSTANCE_USER = userDataPreference
                userDataPreference
            }
        }
    }
}