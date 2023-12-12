# invoice-assistant-t5
invoice assistant application created by chatGPT

Google Colab notebook: [here](https://colab.research.google.com/drive/1I6l2HQ8iK7dFvVIVz1tbDCyNvmDa903t?usp=sharing)</br>
ChatGPT conversation: [here](https://chat.openai.com/share/37eb17fa-982c-44f6-8ab5-5b8290711493)</br>
Llama2 chatbot code was based on walkthrough from: [here](https://colab.research.google.com/github/mlc-ai/notebooks/blob/main/mlc-llm/tutorial_chat_module_getting_started.ipynb#scrollTo=Cm85Ap3zDmYB)</br>

# Notes/Observations
- Initial GPT design had a few bugs:
  - The prompt to the T5 model did not have the field parameters that we were looking for
  - The T5 model did not have the correct answer to the question.  After a few manual prompt attempts it looked like it would only provide translations to german.  It seemed easier to switch to the LLama chatbot since we had tested it earlier with good results.  colab notebook: [here](https://colab.research.google.com/drive/19KNUvxpfziMVys_9okKS0WKs_FtBau4w?usp=sharing)
  - The invoice generation code worked well.  Looks like it provided docstring and good code for test data generation
- After switching to LLama there were some small adjustments needed to work on the colab environment.  Namely directory structure, cloing the application, etc.
- One challenging part was to have the LLAMA chatbot consistently display the same formatted answer so that the application could gather the fields to be exported to csv.  Had to tell the llama chatbot to "output the data in json" format so that we can capture that output in a consistent way.  Otherwise the llama chatbot would be inconsistent on how it printed out the different fields in the chat
- Google colab runs out of cycles at some point and asks you to pay.  Seems that there is a certain amount of computational resources alloted per day.

# future plans/considerations
At this point the code runs fine without any errors in google colab.  Some of the flow might change depending on where this is run.  Specially on a local machine
- Still have not done much functional testing.  Would like to expand on the functional test code and try larger samples.  The functional test code that chatGPT created does not seem to check whether the data is accurate.  Only targeted edge cases so that needs to be expanded but otherwise it created a bunch of code that would have taken a lot longer.
- Try training the model further to be more accurate on the response.
- Try different models
- Create training data instead of test data.  I'm assuming training data would have an input prompt and expected outcome in order to tell the model where it got it wrong
