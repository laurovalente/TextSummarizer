from transformers import T5Tokenizer, TFT5ForConditionalGeneration

model_type = 't5-base'
file_object  = open("file2", "r")

phrase = file_object.read()
tokenizer = T5Tokenizer.from_pretrained(model_type)
model = TFT5ForConditionalGeneration.from_pretrained(model_type)
inputs = tokenizer.encode(phrase, return_tensors="tf")  # Batch size 1
outputs = model(inputs, decoder_input_ids=inputs)
inputs = tokenizer.encode("summarize: "+phrase, return_tensors="tf")  # Batch size 1
result = model.generate(inputs,num_beams=5,
								no_repeat_ngram_size=2,
								min_length=100,
								max_length=250,
								early_stopping=True)
t5_tokenizer = T5Tokenizer.from_pretrained(model_type)
t5_tokenizer.decode(result[0])
