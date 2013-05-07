
import ctypes


so = ctypes.CDLL("/data/local/itbb/grib/grib_api-1.10.0/lib/libgrib_api.so")


# grib_handle* grib_handle_new_from_samples (grib_context* c, const char* res_name)
so.grib_handle_new_from_samples.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
def grib_handle_new_from_samples(name):
    return so.grib_handle_new_from_samples(0, name)


# int grib_is_defined(grib_handle* h, const char* key);
so.grib_is_defined.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
def grib_is_defined(grib_handle, key):
    return so.grib_is_defined(grib_handle, key)


# int grib_get_native_type(grib_handle* h, const char* name, int* type);
so.grib_get_native_type.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p]
def grib_get_native_type(grib_handle, key):
    value = ctypes.c_int()
    so.grib_get_native_type(grib_handle, key, ctypes.byref(value))
    return value.value


# int grib_get_long(grib_handle* h, const char* key, long* value);
so.grib_get_long.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p]
def grib_get_long(grib_handle, key):
    value = ctypes.c_long()
    so.grib_get_long(grib_handle, key, ctypes.byref(value))
    return value.value


# int grib_get_double(grib_handle* h, const char* key, double* value);
so.grib_get_double.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p]
def grib_get_double(grib_handle, key):
    value = ctypes.c_double()
    so.grib_get_double(grib_handle, key, ctypes.byref(value))
    return value.value


# int grib_get_string(grib_handle* h, const char* key, char* mesg, size_t *length);
so.grib_get_string.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_void_p]
def grib_get_string(grib_handle, key):
    length = ctypes.c_int(256)
    mesg = ctypes.create_string_buffer(length.value)
    so.grib_get_string(grib_handle, key, mesg, ctypes.byref(length))
    return mesg.value


# const char* grib_get_error_message(int code);
