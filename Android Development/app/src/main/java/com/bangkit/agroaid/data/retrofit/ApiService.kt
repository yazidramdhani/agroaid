package com.bangkit.agroaid.data.retrofit

import com.bangkit.agroaid.data.response.ForumPostResponse
import com.bangkit.agroaid.data.response.LoginResponse
import com.bangkit.agroaid.data.response.NewPostResponse
import com.bangkit.agroaid.data.response.SignupResponse
import retrofit2.Call
import retrofit2.http.*

interface ApiService {
    @POST("login")
    fun login(
        @Field("email") email: String,
        @Field("password") password: String
    ): Call<LoginResponse>

    @POST("signup")
    fun signup(
        @Field("email") email: String,
        @Field("password") password: String
    ): Call<SignupResponse>

    @POST("posts")
    fun newPost(
        @Header("Authorization") token: String,
        @Field("title") title: String,
        @Field("content") content: String
    ): Call<NewPostResponse>

    @GET("posts")
    fun getPosts(
        @Header("Authorization") token: String,
        @Field("postId") postId: String,
        @Field("userId") userId: String,
        @Field("User") User: String,
        @Field("title") title: String,
        @Field("content") content: String
    ): Call<ForumPostResponse>

    @POST("posts/{postId}/comments")
    fun addComment(

    )
}

