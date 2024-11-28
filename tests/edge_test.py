if __name__ == "__main__":
    from RealtimeTTS import TextToAudioStream, EdgeEngine, EdgeVoice

    def dummy_generator():
        yield "Hey guys! These here are realtime spoken sentences based on edge text synthesis. "
        yield "With a voice based on microsoft azure tts technology. "

    #voice = GTTSVoice(s1peed=1.3)
    engine = EdgeEngine(rate=5, pitch=10)
    stream = TextToAudioStream(engine, output_device_index=0)

    print("Getting voices")
    voices = engine.get_voices()
    print(voices)
    #engine.set_voice("RyanNeural")  

    
    #voice = EdgeVoice("en-GB-RyanNeural", rate="+5%", volume="+0%", pitch="+10Hz")
    voice = EdgeVoice("en-GB-RyanNeural")
    engine.set_voice(voice)

    print("Starting to play stream")
    stream.feed(dummy_generator()).play(log_synthesized_text=True)
