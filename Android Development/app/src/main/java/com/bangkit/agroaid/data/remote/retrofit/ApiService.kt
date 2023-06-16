package com.bangkit.agroaid.data.remote.retrofit

import com.bangkit.agroaid.data.remote.response.*
import okhttp3.MultipartBody
import retrofit2.Call
import retrofit2.http.*

interface ApiService {
    @FormUrlEncoded
    @POST("login")
    fun login(
        @Field("email") email: String,
        @Field("password") password: String
    ): Call<LoginResponse>

    @FormUrlEncoded
    @POST("signup")
    fun signup(
        @Field("fullname") fullname: String,
        @Field("username") username: String,
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
        @Header("Authorization") token: String
    ): ForumResponse

    @POST("posts/{postId}/comments")
    fun addComment(
        @Header("Authorization") token: String,
        @Field("content") content: String,
        @Path("postId") postId: String
    ): Call<CommentResponse>

    @GET("posts/{postId}/comments")
    fun getAllComments(
        @Header("Authorization") token: String,
        @Path("postId") postId: String
    ): CommentResponse

    @Multipart
    @POST("predict")
    suspend fun predictDisease(
        @Query("type") plant: String,
        @Part image: MultipartBody.Part,
        @Header("Authorization") token: String
    ): PredictResponse

    @GET("predictions")
    suspend fun getHistory(
        @Header("Authorization") token:String
    ): HistoryResponse

}

