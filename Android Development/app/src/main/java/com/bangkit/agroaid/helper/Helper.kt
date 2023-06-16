package com.bangkit.agroaid.helper

sealed class Status<out R> private constructor() {
    data class SuccessStatus<out T>(val dataresponse: T) : Status<T>()
    data class ErrorStatus<out T>(val messageerror: String) : Status<T>()
    object LoadingStatus : Status<Nothing>()
}