import scipy.io.wavfile
import os
import wave
import audioop

__author__ = 'clayton'


vals = scipy.io.wavfile.read('../test_data_raw/swwv9a.wav')


def downsample_wav(src, dst, inrate=44100, outrate=16000, inchannels=2, outchannels=1):
    """
    http://stackoverflow.com/questions/30619740/python-downsampling-wav-audio-file
    :param src:
    :param dst:
    :param inrate:
    :param outrate:
    :param inchannels:
    :param outchannels:
    :return:
    """
    if not os.path.exists(src):
        print 'Source not found!'
        return False

    if not os.path.exists(os.path.dirname(dst)):
        os.makedirs(os.path.dirname(dst))

    try:
        s_read = wave.open(src, 'r')
        s_write = wave.open(dst, 'w')
    except:
        print 'Failed to open files!'
        return False

    n_frames = s_read.getnframes()
    data = s_read.readframes(n_frames)

    try:
        converted = audioop.ratecv(data, 2, inchannels, inrate, outrate, None)
        if outchannels == 1:
            converted = audioop.tomono(converted[0], 2, 1, 0)
    except:
        print 'Failed to downsample wav'
        return False

    try:
        s_write.setparams((outchannels, 2, outrate, 0, 'NONE', 'Uncompressed'))
        s_write.writeframes(converted)
    except:
        print 'Failed to write wav'
        return False

    try:
        s_read.close()
        s_write.close()
    except:
        print 'Failed to close wav files'
        return False

    return True