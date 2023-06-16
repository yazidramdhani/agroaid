package com.bangkit.agroaid.helper

import android.app.Application
import android.content.ContentResolver
import android.content.Context
import android.graphics.Bitmap
import android.graphics.BitmapFactory
import android.net.Uri
import android.os.Environment
import com.bangkit.agroaid.R
import java.io.*
import java.text.SimpleDateFormat
import java.util.*

private const val FORMAT_FILENAME = "dd-MMM-yyyy"

val stampTime: String = SimpleDateFormat(
    FORMAT_FILENAME,
    Locale.US
).format(System.currentTimeMillis())

fun createTempFile(ctx: Context): File {
    val dir: File? = ctx.getExternalFilesDir(Environment.DIRECTORY_PICTURES)
    return File.createTempFile(stampTime, ".jpg", dir)
}

fun createFile(app: Application): File {
    val mediaDir = app.externalMediaDirs.firstOrNull()?.let {
        File(it, app.resources.getString(R.string.app_name)).apply { mkdirs() }
    }
    val output = if (
        mediaDir != null && mediaDir.exists()
    ) mediaDir else app.filesDir

    return File(output, "$stampTime.jpg")
}

fun uriToFile(img: Uri, ctx: Context): File {
    val contentResolver: ContentResolver = ctx.contentResolver
    val file = createTempFile(ctx)
    val inputStream = contentResolver.openInputStream(img) as InputStream
    val outputStream: OutputStream = FileOutputStream(file)
    val buf = ByteArray(1024)
    var len: Int
    while (inputStream.read(buf).also { len = it } > 0) outputStream.write(buf, 0, len)
    outputStream.close()
    inputStream.close()
    return file
}

fun imageFileReduced(file: File): File {
    val bitmap = BitmapFactory.decodeFile(file.path)
    var compressQuality = 100
    var streamLength: Int
    do {
        val bmpStream = ByteArrayOutputStream()
        bitmap.compress(Bitmap.CompressFormat.JPEG, compressQuality, bmpStream)
        val bmpPicByteArray = bmpStream.toByteArray()
        streamLength = bmpPicByteArray.size
        compressQuality -= 5
    } while (streamLength > 1000000)
    bitmap.compress(Bitmap.CompressFormat.JPEG, compressQuality, FileOutputStream(file))
    return file
}