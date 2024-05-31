Introduction to OpenAI Models

Christine Al-Thifairy

April 2024

Contents

1 Prerequisites

1.1 Essential technical skills . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

1.2 Software and tools . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

1.3 Soft skills and concept understanding . . . . . . . . . . . . . . . . . . . . . .

2 Getting started with OpenAI models

2.1 Creating an OpenAI account

. . . . . . . . . . . . . . . . . . . . . . . . . . .

2.2 Obtaining API keys . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

2.3 Setting up environment variables for OpenAI API key . . . . . . . . . . . . . .

2.3.1 Windows . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

2.3.2 Mac OS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

2.4 Adding a payment method and billing settings . . . . . . . . . . . . . . . . . .

2.5 Understanding rate limits in OpenAI

. . . . . . . . . . . . . . . . . . . . . . .

2.6 ”Hello World” using OpenAI python

. . . . . . . . . . . . . . . . . . . . . . .

3 Privacy and security in OpenAI’s chat and API services

3.1 Opt-Out Policies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

4 OpenAI models

4.1 Model context widow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

4.2 OpenAI Playground . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

4.2.1 Chat example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

4.2.2 Uploading images and files . . . . . . . . . . . . . . . . . . . . . . . .

5 Playground vs OpenAI API state behaviour

5.1 Playground stateful interaction . . . . . . . . . . . . . . . . . . . . . . . . . .

5.2 API stateless interaction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

6 Create chat completions

6.1 System role . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

6.2 Few-shot learning with chat completion . . . . . . . . . . . . . . . . . . . . .

7 Audio

7.1 Create speech . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

2

4

4

4

5

5

5

5

6

6

7

7

8

8

11

11

12

13

14

15

17

17

17

19

22

23

25

27

27

7.2 Create transcription . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

7.3 Create translation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

8 Embeddings

8.1 Using embeddings for sentiment analysis . . . . . . . . . . . . . . . . . . . .

9 Images

9.1 Create images . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

9.2 Create image edit

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

9.3 Create image variations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

10 Moderation

11 File API

11.1 Upload files . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

11.2 List files . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

11.3 Delete file . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

12 Batch API

12.1 Example without batch job . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

12.2 Example with batch job . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

12.2.1 Preparing jsonl file . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

12.2.2 Upload batch file . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

12.2.3 Creating batch job . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

12.2.4 Checking batch status . . . . . . . . . . . . . . . . . . . . . . . . . . .

12.3 Cancelling a batch . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

12.4 List batch . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

28

29

30

33

36

36

38

42

44

47

47

48

49

50

50

53

53

56

56

57

59

60

3

1 Prerequisites

1.1 Essential technical skills

The following technical skills are crucial for anyone looking to fully benefit from this course

material, providing the necessary groundwork for more advanced topics:

• Python proficiency: Comprehensive understanding of Python programming, including

familiarity with its syntax, libraries, and environment setup.

• Working with APIs: Basic knowledge of how to make API calls using Python, including

handling HTTP requests and responses.

1.2 Software and tools

This section lists the software and tools that participants will need throughout the course.

• Installation of Python and necessary libraries.

$ pip install requests
$ pip install openai
$ pip install scikit - learn
$ pip install pandas

If you are working within a Python virtual environment and you want to ensure that you are

using the pip associated with that environment. Using python -m pip ensures that pip is

run from the Python interpreter corresponding to your environment.

$ python -m pip requests
$ python -m pip openai
$ python -m pip install scikit - learn
$ python -m pip install pandas

1

2

3

4

1

2

3

4

• Familiarity with a code editor or IDE (Integrated Development Environment) like VS Code

or PyCharm.

4

1.3 Soft skills and concept understanding

• It would be helpful to understand basic concepts of Artificial Intelligence and machine

learning specifically training models using Python libraries such as Scikit-learn or Tensor-

Flow, but not essential for this course.

• Problem-solving abilities and patience for debugging code and understanding AI behav-

iors.

2 Getting started with OpenAI models

OpenAI operates as a paid service, offering access to various AI models like GPT-4 and

DALL-E, with pricing that varies based on usage and computational demands.

2.1 Creating an OpenAI account

To access the OpenAI API, first you need to create an account on the OpenAI platform.

Please register at the following URL:

https://platform.openai.com/signup

Follow the on-screen instructions to complete the registration process.

2.2 Obtaining API keys

Once you have registered an account on the OpenAI platform, the next step is to obtain

your API key, which is essential for making API requests. API keys serve as both a unique

identifier and a secret token for authentication, allowing you to perform API calls securely.

To obtain your API key, follow these steps:

1. Log in to your OpenAI account dashboard by visiting https://platform.openai.com.

2. Navigate to the API Keys section from the menu on the left.

3. Click on the ‘Create new key‘ button to generate a new API key. Once created, your

key will be displayed on the screen. Be sure to copy this key and store it securely in

a password manager or other secure storage. Once generated, you won’t be able to

view the key again.

5

4. It is recommended to label your API key according to the usage environment (e.g.,

development, production) to help manage multiple keys.

Figure 1: Generate API keys screen

Remember, your API key is like a password:

• Do not share it publicly on blogs, GitHub, or other platforms.

• Keep it secure by using environment variables or secure vaults when integrating into

applications.

• If you suspect your API key has been compromised, revoke it immediately and generate

a new one from the dashboard.

Managing your API keys responsibly ensures the security of your applications and prevents

unauthorised access to your OpenAI services.

2.3 Setting up environment variables for OpenAI API key

To keep your OpenAI API key secure in your application, it is recommended to store it in

environment variables. This prevents accidental exposure in source code and helps manage

keys for different environments (development, production).

Below are the steps to set up environment variables on Windows and macOS:

2.3.1 Windows

1. Open System properties and select Advanced system settings.

2. Go to the Advanced tab and click on Environment Variables.

6

3. Select New. . .

from the User variables section(top). Add your name/key value pair,

replacing <yourkey> with your API key.

Variable name: OPENAI API KEY

Variable value: <yourkey>

4. Click OK to save and close all dialogs.

2.3.2 Mac OS

1. Add the following line to your terminal configuration file:

1

export OPENAI_API_KEY = " your_api_key_here "

2. To apply the changes, open new terminal window.

In both cases, ensure that you replace "your api key here" with your actual OpenAI API

key. Once set, you can access your API key in your applications via the environment variable

OPENAI API KEY, thus keeping your credentials secure.

Note: All the necessary code snippets, json files, csv files, images and audio files in this

course are hosted on Introduction to OpenAI Models GitHub repository.

2.4 Adding a payment method and billing settings

To start using OpenAI services and manage your billing, you need to add a valid payment

method, such as a credit card, to your account. Under Settings menu item on the left

navigate to Billing page to access payment method and billing. First time it will show ”Free

trial”.

Figure 2: Billing no credits

Figure 3: Billing with credits

OpenAI services are pre-paid billing or ”Pay as you go”. Users need to pre-purchase

credits to use the API and Playground. Once you setup your payment method you can buy

7

credits by clicking on ”Add to credit balance” button.

You might like to start with $10.00. This will be enough to do all the exercises in this course.

For more details on how to buy credits and invoices navigate to https://help.openai.com/

en/articles/8264644-what-is-prepaid-billing page.

2.5 Understanding rate limits in OpenAI

When you use OpenAI’s services, there are certain rules about how often you can send

requests, like asking questions or generating images. These rules are called ”rate limits.”

Think of rate limiting as a traffic light system for data. It helps manage the flow of requests

so that the service can handle everyone’s needs without getting overwhelmed.

When you sign up for OpenAI and choose a plan, you’re given a certain number of ”tokens”

that you can use within a specific time frame, say, per minute or per day. If you try to send

too many requests too quickly and use up all your tokens, OpenAI will temporarily stop

accepting your requests until the time limit resets.

If you find you’re consistently hitting your rate limits, consider upgrading your plan to get a

higher limit.

To view your rate limits navigate to Limits from the Setting menu item on the left.

Figure 4: Limits page

2.6 ”Hello World” using OpenAI python

Once you finish setting up your payment method and are ready to go, try this simple example

which demonstrates a simple request to the chat completion API.

8

1 from openai import OpenAI

2

3 client = OpenAI ()

4

5 completion = client . chat . completions . create (

model = " gpt -3.5 - turbo -0125 " ,

messages =[

{ " role " : " user " , " content " : " Say hello word " } ,

]

6

7

8

9

10 )

11

12 print ( completion . choices [0]. message . content )

In the initialisation of the client object with the OpenAI() constructor, you can specify the

API key directly as an argument, like this:

1 client = OpenAI (

api_key = os . environ . get ( " OPENAI_API_KEY " ) ,

2

3 )

However, this step is optional—it can be omitted if the API key is already set as an envi-

ronment variable named OPENAI API KEY allowing you to initialise the client simply with:

1 client = OpenAI ()

This makes the code cleaner and less error-prone, as it reduces the direct handling of

sensitive information within the application code base.

To manually send a request to an OpenAI API endpoint without using the OpenAI library, you

can use the Python requests library. This approach involves constructing the HTTP request

manually, which includes setting the appropriate headers, method, and body. Here’s how

you can do it to achieve the same result as your previous example:

1 import os

2 import requests

3

9

4 OPENAI_API_KEY = os . getenv ( " OPENAI_API_KEY " )

5 url = " https :// api . openai . com / v1 / chat / completions "

6

7 headers = {

" Content - Type " : " application / json " ,

" Authorization " : f " Bearer { OPENAI_API_KEY } "

8

9

10 }

11

12 data = {

" model " : " gpt -3.5 - turbo -0125 " ,

" messages " : [

{ " role " : " user " , " content " : " Say Hello World " }

]

13

14

15

16

17 }

18

19 # Make the POST request

20 response = requests . post ( url , headers = headers , json = data )

21

22 # Check if the request was successful

23 if response . status_code == 200:

24

25

26

27

28

# Get the completion message from the response

response_json = response . json ()

choices = response_json [ " choices " ]

completion = choices [0][ " message " ][ " content " ]

print ( completion )

29 else :

30

print ( " Failed to fetch data : " , response . status_code , response .

text )

For the rest of this book, we will use the OpenAI Python library for all examples because this

library not only simplifies the code necessary to communicate with OpenAI’s API but also

provides built-in functions specifically designed for AI tasks, ensuring we can focus more on

development and less on managing underlying API protocols.

10

3 Privacy and security in OpenAI’s chat and API services

OpenAI collects data from user interactions to improve its models. This data helps the

AI learn from real-world usage, enhancing its ability to understand and generate natural

language. OpenAI claims that before using the data for training, OpenAI anonymises it to

remove any personal identifiers. This means that individual users cannot be identified from

the data.

The data is then aggregated, which involves combining it with data from many other users.

This ensures that no single conversation stands out and the AI learns from a broad set of

examples.

3.1 Opt-Out Policies

Read https://brightinventions.pl/blog/openai-api-privacy-policies-explained/

You can opt-out of continuously training the model with your chat inputs by going to:

Settings > Data controls > Improve the model for everyone and setting it to “Off.”

This setting applies to your account and is not tied to a specific device.

Figure 5: Opting-out from using conversations in training

By turning off the ”Improve the model for everyone” setting, you have opted out of allowing

your data to be used to train and improve OpenAI’s models. The performance of the AI will

not be affected. You will still have access to the same capabilities and features.

11

4 OpenAI models

The OpenAI platform is powered by a diverse set of models, each designed with distinct

capabilities. This section delves into their unique functionalities and discusses optimal use

cases for each, providing a comprehensive understanding of how these models can be

leveraged in various domains and applications.

Note: It is recommended to refer to the official OpenAI documentation for the most up-to-

date information on API endpoints and available models.

12

Model

GPT-4o

Description of use

GPT-4o (”o” for ”omni”) is the most advanced model. It is multi-

modal (accepting text or image inputs and outputting text), and it

has the same high intelligence as GPT-4 Turbo but is much more

efficient—it generates text 2x faster and is 50% cheaper.

GPT-4

A set of models (The latest in the GPT series) that improve on

GPT-3.5 and can understand and generate natural language and

code. Ideal for complex text generation tasks, such as compos-

ing emails, generating creative content, and simulating human-

like dialogue.

GPT-3.5

A set of models that improve on GPT-3 and can understand and

generate natural language and code.

Embeddings

A set of models that can convert text into numerical vector form

to facilitate text similarity.

DALL-E

A set of models that can generate original images from natural

language.

Whisper

A set of models that can transcribe and translate speech to text.

Text to speech (TTS)

A set of models that can synthesize text to speech.

Moderation

A set of models that provide classification capabilities that look

for content in the following categories:

hate, hate/threatening, self-harm, sexual, sexual/minors, vio-

lence, and violence/graphic.

4.1 Model context widow

The model context window or ”token limit” refers to the maximum amount of text (measured

in tokens) that a language model like GPT-4 can process at once.

13

The context window determines how much conversation or text history the model can re-

member and use to generate relevant responses. If the token limit is exceeded, the model

will truncate the oldest part of the context (conversation) to make room for new input.

Here are other key points about the context window:

• Tokens can be as short as one character or as long as one word (e.g., ”a” and ”apple”

are both single tokens). Typically, one token is about 4 bytes, and on average, a word in

English is about 1.3 tokens.

• The size of the context window varies for each model. For example, gpt-4o can handle up

to 128,000 tokens while gpt-3.5-turbo can handle up to 16,385 tokens.

• The context window includes both input and output tokens. If you input 2,000 tokens and

expect an output of 500 tokens, the total usage is 2,500 tokens.

If you’re building an application with OpenAI’s API, you need to manage the context to

ensure important information is retained within the token limit. For instance, in a customer

service bot, summarising earlier interactions can help stay within the token limit while still

providing relevant responses.

Read the official documents of OpenAI to find out what is the limit of the context window for

each model.

4.2 OpenAI Playground

The OpenAI Playground is an online platform provided as a paid service by OpenAI which

allows you to experiment and interact with models and test different prompts and parameters

to observe the model response without writing any code.

The Playground UI provides a facility to select different models, setting parameters (such as

temperature, max tokens) and ability to instantly see the output generated by the model.

Currently, the OpenAI Playground allows you to try out three primary modes: Chat, Assis-

tants, and Completion (legacy). We are going to demonstrate how to use the Playground

with Chat mode.

You can access the Playground from https://platform.openai.com/playground or from

sidebar menu.

14

4.2.1 Chat example

When you first access the Playground, you will be initially in Chat mode.

Figure 6: OpenAI Playground

Next we are going to compose a user question (also known as a prompt) and use the default

model and leave the parameter settings as they are. We’re going to ask the model to list five

cruciferous vegetables. We type the user prompt and then click on the Submit button. The

model response will appear as an assistant.

15

Figure 7: Prompting using the Playground

You can view generated source code for the conversation by clicking the View code button

top right.

Figure 8: View entire request code

In order to change the parameter settings on the page, you must have some technical skills

to understand what different controls do to perform more comprehensive tests.

16

4.2.2 Uploading images and files

You can upload image or files related to your conversation in the Playground. Here in this

example, we used it to upload a photo of Sam the cat and asked the model to describe the

image in a funny way.

Figure 9: Using the GPT-4o model to describe an uploaded image

5 Playground vs OpenAI API state behaviour

When using the OpenAI API, each call to the model is stateless by default. This means

that unless you explicitly pass the history of the conversation, each request is treated as a

standalone interaction without any knowledge of previous interactions.

5.1 Playground stateful interaction

When users interact with the Playground, the model reads through the entire history of

the conversation to understand the evolving dialogue and context before answering the last

request.

This method allows the model to adapt its responses based on the flow of the conversation.

Let’s see how the Playground handles longer interactions. We are going to instruct the

model to translate some text alternating between Arabic and French.

In other words, the

17

first request should translate to Arabic, second to French, third to Arabic, and so on. We

define the SYSTEM role content as follow:

”You are a helpful translator. You can do translation to Arabic and French in alternative way.

Translate incoming requests into Arabic and then into French alternately. Start with Arabic

for the first request, then translate the second request into French, and continue alternating

between Arabic and French for subsequent requests. Which means the requests with odd

numbers (request 1, request 3, etc.) are translated to Arabic while requests with even

numbers (request 2, request 4, etc.) are translated to French.”

We then provide it with USER role content with some text to translate.

Figure 10: Example of persistent context with Playground

As you can see, the Playground automatically handles session management and maintains

conversation context, providing a seamless conversational experience. It understands that

the translation should alternate between Arabic and French. This is because the model

reads the entire conversation before responding to the last message.

To do the same task via the API endpoint, we need to store the entire conversation and pass

it to every new request. The code snippets below demonstrate two examples how to interact

with the chat completion API.

18

5.2 API stateless interaction

First let’s take a look at an example where we do not pass the entire conversation history to

the model.

1 from openai import OpenAI

2 client = OpenAI ()

3

4 system_prompt = """ Translate incoming requests into Arabic and

then into French alternately . Start with Arabic for the first

request , then translate the subsequent request into French ,

and continue alternating between Arabic and French for

subsequent requests . """

5

6 def get_response ( text_to_translate ) :

response = client . chat . completions . create (

model = " gpt -3.5 - turbo " ,

messages =[

{ " role " : " system " , " content " : system_prompt } ,

{ " role " : " user " , " content " : text_to_translate } ,

] ,

max_tokens =150 ,

temperature =0.7

)

return response . choices [0]. message . content

7

8

9

10

11

12

13

14

15

16

17

18 texts = [

" Good morning my dear . " ,

" Are you happy today ? " ,

" Where did you go yesterday ? " ,

" I am very sorry . " ,

" life is a journey not a destination "

19

20

21

22

23

24 ]

25

19

26 responses = [ get_response ( text ) for text in texts ]

27 for response in responses :

28

print ( response )

In this example we demonstrate how to send independent requests to the API endpoint.

When running the snippet code above, we got the following response:

Figure 11: API requests: stateless interaction

The system instruction is repeated with each call to the get response() function. However,

The function does not maintain a history of previous responses. Each call is independent,

with only the current user message and a repeated system instruction included. This makes

the session stateless, where each interaction is treated in isolation without any memory of

previous messages. Therefore the model did not translate requests according to system

instructions correctly.

This is solved by passing the conversation history to the model with each new request.

1 from openai import OpenAI

2

3 class Translator :

4

5

6

def __init__ ( self ) :

self . client = OpenAI ()

self . messages = [{ " role " : " system " , " content " : """ You are a

helpful translator . You can do translation to Arabic and

French in alternate ways . Translate incoming requests into

Arabic and then into French alternately . Start with

Arabic for the first request , then translate the second

request into French , and continue alternating between

Arabic and French for subsequent requests . This means the

requests with odd numbers ( request 1, request 3, etc .) are

20

translated to Arabic while requests with even numbers (

request 2, request 4, etc .) are translated to French .

""" }]

def get_response ( self , text_to_translate ) :

# Append the new user message to the existing conversation

self . messages . append ({ " role " : " user " , " content " :

text_to_translate })

response = self . client . chat . completions . create (

model = " gpt -4 o " ,

messages = self . messages ,

)

# Append the model ’s response to the conversation

self . messages . append (

{ " role " : " assistant " , " content " : response . choices [0].

message . content })

return response . choices [0]. message . content

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24 texts = [

" Good morning my dear . " ,

" Are you happy today ? " ,

" Where did you go yesterday ? " ,

" I am very sorry . " ,

" Life is a journey , not a destination . " ,

25

26

27

28

29

30 ]

31

32 translator = Translator ()

33 responses = []

34 for text in texts :

35

response = translator . get_response ( text )

21

responses . append ( response )

36

37

38 for response in responses :

39

print ( response )

When running the snippet code above, we got the following response:

Figure 12: API requests: stateful interaction

Passing the entire conversation to the model allows the model to be aware of which lan-

guage it should be translating into next, adhering more consistently to the alternating lan-

guage pattern.

In the upcoming sections, we will explore and explain each API endpoint of the OpenAI

platform.

6 Create chat completions

API endpoint: POST https://api.openai.com/v1/chat/completions

Function: client.chat.completions.create()

Model endpoint compatibility: GPT-3.5-Turbo and GPT-4 models

OpenAI’s GPT-3.5-Turbo and GPT-4 models are designed to interpret inputs formatted as

dialogues within their chat.completions endpoint.

For these models, input is structured using messages parameter that consists of an ar-

ray of message objects, each outlined by a specific role to organise the conversation.

In

Python, this array is implemented as a list of dictionaries, where each dictionary represents

a message with a designated role.

An example of the format of a message object is:

22

{”role”: ”system”, ”content”: ”You are assistant.”},

{”role”: ”user”, ”content”: ”Hello, how can you assist me today?”},

{”role”: ”assistant”, ”content”: ”I’m here to help! Please tell me your query.”}

6.1 System role

The system role, often referred to as the system message, is an optional but highly valuable

component that can be positioned at the beginning of the messages array in the conversa-

tion.

This initial message sets the stage for the interaction, offering the model explicit guidance

on how to handle the forthcoming conversation. The system role can encompass a variety

of directives and information, each aimed at optimising the model’s performance according

to specific user needs or scenarios. Here are several examples of what you might include

in a system message:

• Specific instructions or rules: You can direct the model to adhere to specific conversa-

tional rules or instructions, for example, explicitly instructs the model to format its response

in JSON:

1 response = client . chat . completions . create (

model = " gpt -4 - turbo " ,

response_format : { type : " json_object " } ,

messages =[

" role " : " system " ,

" content " : " Answer in JSON format . "

" role " : " user " ,

" content " : " ... "

{

} ,

{

}

] ,

...

2

3

4

5

6

7

8

9

10

11

12

13

14

15 )

23

Let’s try this scenario in the Playground:

Figure 13: Example of system role instruction to the model

• Brief description of the assistant: Outline the character or type of assistant that the

model should emulate, such as a technical support agent, a friendly advisor, or a formal

consultant. This helps the model adjust its tone and mannerisms accordingly.

1 { " role " : " system " , " content " : " Assistant is trained to answer

all your history questions in less than 100 words . " } ,

2 { " role " : " user " , " content " : " Who is Hammurabi ? " }

We can try the above example in the Playground:

Figure 14: OpenAI Playground

• Personality traits: Specify certain personality traits you wish the assistant to exhibit dur-

ing the conversation.

24

1 {

2

3

4 }

" role " : " system " ,

" content " : " The assistant is friendly and patient , encourages

users , and avoids technical jargon unless requested . "

• Preloaded data or context: This can include essential background information that the

assistant needs to know before starting the conversation, such as details from a cus-

tomer’s profile, key points from an FAQ, or contextual data relevant to the current inter-

action. This information can be crucial for the assistant to provide accurate and relevant

responses. An example:

1 { " role " : " system " ,

2 " content " : " Assistant is knowledgeable about electric vehicles

and their technology . Respond to inquiries using the

information below :

3 Context :

4 - Electric vehicles ( EVs ) use electric motors powered by

rechargeable battery packs .

5 - Major advantages of EVs include reduced emissions and lower

running costs compared to traditional internal combustion

engine vehicles .

6 - Common concerns about EVs involve battery life , charging

infrastructure , and initial purchase costs . " } ,

7 { " role " : " user " , " content " : " How do electric vehicles help the

environment ? " }

6.2 Few-shot learning with chat completion

Few-shot learning is a machine learning approach that requires only a small amount of data

to train models. Typically, machine learning models need large datasets to learn effectively,

but gathering such extensive data can be costly, time-consuming, or sometimes unfeasible.

Few-shot learning addresses these challenges.

25

When you provide the model with a few examples, or “prompts,” it can generate responses

that are aligned with the information provided in these prompts. This is essentially few-shot

learning in action.

You can now include a series of messages between the user and the assistant in the

prompt as few-shot examples.

The example below illustrates how we specify the expected model response by providing an

assistant role content.

The messages object includes a key example specified in the assistant’s role content, which

serves as a shot for the model’s few-shot learning approach. This example, which defines

the virtue of patience guides the model in generating a tailored and contextually relevant

assistant’s response based on the provided shot and parameters.

1 from openai import OpenAI

2 client = OpenAI ()

3

4 def get_response ( question ) :

5

6

7

8

9

10

11

12

13

response = client . chat . completions . create (

model = " gpt -4 o " ,

messages =[

{ " role " : " system " , " content " : " Answer in a consistent

style . " } ,

{ " role " : " user " , " content " : " Teach me about patience . "

} ,

{ " role " : " assistant " , " content " : " Patience is a virtue

that involves waiting calmly in the face of

frustration or adversity . Anywhere there is

frustration or delay , you have the opportunity to

practice it , whether you are stuck in traffic ,

waiting at the doctor ’s office , or dealing with a

slow computer . " } ,

{ " role " : " user " , " content " : question } ,

] ,

max_tokens =150 ,

26

temperature =0.7

)

return response . choices [0]. message . content

14

15

16

17

18 questions = [

" Teach me about the ocean . " ,

" Teach me about sadness . " ,

" Teach me about living a happy life . "

19

20

21

22 ]

23 responses = [ get_response ( question ) for question in questions ]

24 for response in responses :

25

print ( response )

For full details on Chat API and all the parameters and the return values, visit https://

platform.openai.com/docs/api-reference/chat/create.

7 Audio

7.1 Create speech

API endpoint: POST https://api.openai.com/v1/audio/speech

Function: client.audio.speech.create()

Model endpoint compatibility: TTS models - tts-1 or tts-1-hd

Text-to-Speech (TTS) models, like OpenAI’s tts-1 and tts-1-hd are designed to convert

written text into spoken words, effectively enabling computers to read text aloud.

This example demonstrates how to use the OpenAI Python library to convert a given text

into speech using the ”tts-1” model with the ”alloy” voice, and then save the output as an

MP3 file named ’speech.mp3’.

1 from openai import OpenAI

2

3 client = OpenAI ()

4 file_name = " speech . mp3 "

27

5

6 response = client . audio . speech . create (

model = " tts -1 " ,

voice = " alloy " ,

input = " Oh , the curious feline , mysterious and sly , Leaping

and bounding , oh so spry "

7

8

9

10 )

11

12 response . stream_to_file ( file_name )

For more details about create speech API visit:

https://platform.openai.com/docs/api-reference/audio/createSpeech.

7.2 Create transcription

API endpoint: POST https://api.openai.com/v1/audio/transcriptions

Function: client.audio.transcriptions.create()

Model endpoint compatibility: whisper-1

The OpenAI transcription API utilises advanced models like Whisper to convert spoken lan-

guage in audio files into accurate written text, supporting a variety of common audio formats

such as mp3, m4a, webm, mp4, mpga, wav, and mpeg.

This code snippet uses the OpenAI API to transcribe spoken words from an MP3 audio file

into text using the Whisper model.

1 from openai import OpenAI

2

3 client = OpenAI ()

4 audio_file = open ( " speech . mp3 " , " rb " )

5

6 transcript = client . audio . transcriptions . create (

model = " whisper -1 " ,

file = audio_file

7

8

9 )

28

10 print ( transcript . text )

For full details of this API visit:

https://platform.openai.com/docs/api-reference/audio/createTranscription.

7.3 Create translation

API endpoint: POST https://api.openai.com/v1/audio/translations

Function: ’client.audio.translations.create()’

Model endpoint compatibility: whisper-1

The Translations API accepts audio files in various supported languages and, if required,

converts the spoken content into English text. This is distinct from the Transcriptions end-

point, which outputs text in the same language as the input audio, rather than translating it

into English.

For the list of supported languages, see the OpenAI documentation.

This code snippet utilises the OpenAI API to translate spoken words from an Arabic MP3

audio file into English text using the Whisper model.

1 from openai import OpenAI

2

3 client = OpenAI ()

4 audio_file = open ( " arabic_conversation . mp3 " , " rb " )

5

6 translation = client . audio . translations . create (

model = " whisper -1 " ,

file = audio_file

7

8

9 )

10 print ( translation . text )

For all the details of this API visit

https://platform.openai.com/docs/api-reference/audio/createTranslation

29

8 Embeddings

API endpoint: POST https://api.openai.com/v1/embeddings

Function: client.embeddings.create()

Model endpoint compatibility:

text-embedding-3-small, text-embedding-3-large, text-embedding-ada-002

Words and phrases carry meaning that is related to other words and phrases. For example,

”king” and ”queen” are both royalty, ”apple” and ”orange” are both fruits. In programming, es-

pecially in tasks involving language (like making a chatbot or searching through documents),

it’s useful to capture these relationships.

Embeddings help by turning words into vectors (lists of numbers) in such a way that similar

meanings are captured by numerically similar vectors. This means that words with similar

meanings will have vectors that are close together in the space where these vectors exist.

OpenAI provides pre-trained models that can generate embeddings. These models have

been trained on a diverse range of internet text, so they are good at capturing a wide variety

of language nuances.

Example 1: Generating an embedding for a single input

In this example, the customer review ”Will have to discard as the package had a hole in it.” is

being processed using OpenAI’s text embedding model (text-embedding-3-small) to convert

the text into a numerical representation suitable for machine learning tasks. The dimensions

parameter Indicates the number of dimensions (lenght) for the output embedding vector.

Here it’s set to 10.

1 from openai import OpenAI

2

3 client = OpenAI ()

4

5 response = client . embeddings . create (

6

7

8

input = " Will have to discard as the package had a hole in it . " ,

model = " text - embedding -3 - small " ,

dimensions =10

30

9 )

10

11 print ( response . data [0]. embedding )

Here, we create an embedding for a single sentence using the text-embedding-3-small

model. The input parameter is a single string, and the response contains the embedding

vector which we print out. This method is straightforward and ideal for quick analyses of

individual text entries. The output is:

[ -0.29325512051582336, 0.40246352553367615,

0.0701608657836914, -0.0892515555024147,

-0.19374793767929077, 0.12687857449054718,

-0.6463808417320251, 0.08973661810159683,

-0.5044652819633484, -0.07178929448127747 ]

Example 2: Generating embeddings for multiple texts in a batch

1 import json

2 from openai import OpenAI

3

4 client = OpenAI ()

5

6 # Function to load reviews from a JSON file

7 def load_reviews ( filename ) :

with open ( filename , " r " ) as file :

data = json . load ( file )

return data

8

9

10

11

12 # Function to save embeddings to a JSON file

13 def save_embeddings ( data , filename ) :

with open ( filename , " w " ) as file :

json . dump ( data , file , indent =4)

14

15

16

17 # Function to get embeddings for all reviews in a batch

31

18 def get_embeddings ( reviews ) :

# Prepare a list of texts for embedding

texts = [ review [ " review " ] for review in reviews ]

# Send a single API request for all texts

response = client . embeddings . create (

model = " text - embedding -3 - small " ,

input = texts ,

dimensions =10

)

print ( response )

print ( " \ n \ n " )

# Combine the original reviews with their embeddings

embeddings = []

for i , review in enumerate ( reviews ) :

embedding_vector = response . data [ i ]. embedding

embeddings . append ({

" score " : review [ " score " ] ,

" review " : review [ " review " ] ,

# Assume embeddings are returned in order

" embedding " : embedding_vector

})

return embeddings

19

20

21

22

23

24

25

26

27

28

29

30

31

32

33

34

35

36

37

38

39

40

41 # Main execution function

42 def main () :

reviews = load_reviews ( " review . json " )

embeddings = get_embeddings ( reviews )

save_embeddings ( embeddings , " embeddings . json " )

print ( " ---------- DONE ------------ " )

43

44

45

46

47

48

49 if __name__ == " __main__ " :

50

main ()

32

Note: ’review.json’ used in this example can be downloaded from: https://github.com/

scriptfairy/Introduction-to-OpenAI-Models/tree/main/json GitHub directory.

This script demonstrates processing multiple text at once. It loads reviews from a JSON file

review.json, sends them in a batch ’texts’ to the Embeddings API, and saves the resulting

embeddings along with their original reviews and scores in a file embeddings.json. The

batch approach is particularly useful for applications like sentiment analysis or content cate-

gorisation where processing efficiency is crucial. The file embeddings.json consists of 10

items with the following structure:

{

"score": "False",

"review": "Will have to discard as the package had a hole in it.",

"embedding": [

-0.29325512051582336,

0.40246352553367615,

0.0701608657836914,

-0.0892515555024147,

-0.19374793767929077,

0.12687857449054718,

-0.6463808417320251,

0.08973661810159683,

-0.5044652819633484,

-0.07178929448127747

]

},

8.1 Using embeddings for sentiment analysis

In this section, we’ll explore how to use pre-generated embeddings for sentiment analysis,

where we classify sentiments as positive (True) or negative (False) based on text reviews.

We’ll use a RandomForestClassifier, a popular and effective machine learning model for

classification tasks. We will use the file embeddings.json generated in the previous exam-

ple to train our model.

Note: ’embeddings.json’ used in this example can be downloaded from the following GitHub

33

repo:

https://github.com/scriptfairy/Introduction-to-OpenAI-Models/tree/main/json.

1 import pandas as pd

2 import json

3 from sklearn . model_selection import train_test_split

4 from sklearn . ensemble import RandomForestClassifier

5 from sklearn . metrics import accuracy_score

6

7 # Load embeddings and labels

8 def load_data ( filename ) :

with open ( filename , " r " ) as file :

data = json . load ( file )

X = [ item [ " embedding " ] for item in data ]

# Convert scores to boolean : True for positive , False for

negative

y = [ item [ " score " ] == " True " for item in data ]

return X , y

9

10

11

12

13

14

15

16 X , y = load_data ( " embeddings . json " )

17 # print ("-------- X = \n ", X [1])

18 X_train , X_test , y_train , y_test = train_test_split (

X , y , test_size =0.2 , random_state =42)

19

20

21 # Create and train the model

22 model = RandomForestClassifier ( n_estimators =100 , random_state =42)

23 model . fit ( X_train , y_train )

24

25 # Predict on the test set

26 y_pred = model . predict ( X_test )

27

28 # Calculate accuracy

29 accuracy = accuracy_score ( y_test , y_pred )

34

30 print ( f " Model Accuracy : { accuracy :.2 f } " )

31 print ( " Testing realy amazing \ n " )

32

33 # " really amazing " victor

34 e1 = [

0.343048632144928 ,

-0.3309374749660492 ,

-0.5637745261192322 ,

0.04711998626589775 ,

0.11376921832561493 ,

-0.31761518120765686 ,

-0.28869980573654175 ,

0.44205737113952637 ,

-0.1346609741449356 ,

0.20498140156269073

35

36

37

38

39

40

41

42

43

44

45 ]

46 preds = model . predict ([ e1 ])

47

48 print ( preds )

This example performs sentiment analysis using a RandomForestClassifier, a popular ma-

chine learning model used for classification tasks.

• The ”load data” function reads from a JSON file where embeddings and sentiment scores

are stored. It extracts embeddings into X and converts sentiment scores (’True’ for posi-

tive, ’False’ for negative) into boolean values (y).

• The data is split into training (X train, y train) and testing (X test, y test) sets. 20% of the

data is reserved for testing to evaluate the model’s performance.

• A RandomForestClassifier is instantiated and trained on the training data.

• The accuracy of the model

is calculated by comparing the predicted values (y pred)

against the actual values (y test), and the result is printed. Model Accuracy was 0.50.

• Additionally, the model used to predict a vector e1 which represents the embeddings of

35

the string ’realy amazing’ to test the model with new, unseen data. The model prediction

was [True] which is positive sentiment.

Note: all code snippets and embedding json files are provided from Introduction to OpenAI

Models GitHub repository

For full details of this API visit

https://platform.openai.com/docs/api-reference/embeddings

9 Images

9.1 Create images

API endpoint: POST https://api.openai.com/v1/images/generations

Function: client.images.generate()

Model endpoint compatibility: dall-e-2, dall-e-3

This example demonstrates how to use the OpenAI API for generating images.

1 import requests

2 from openai import OpenAI

3

4 client = OpenAI ()

5 response = client . images . generate (

model = " dall -e -3 " ,

prompt = " a ginger kitten " ,

size = " 1024 x1024 " ,

quality = " standard " ,

n =1 ,

6

7

8

9

10

11 )

12

13 # Extract the image URL from the API response

14 image_url = response . data [0]. url

15

16 # Send a GET request to download the image data

36

17 image_data_response = requests . get ( image_url )

18

19 # If the request was successful

20 if image_data_response . status_code == 200:

21

22

23

24

25

26

27

28

# Specify local file where to save the image

local_file_path = " ginger_kitten . jpg "

# Write the image data to a local file

with open ( local_file_path , " wb " ) as file :

file . write ( image_data_response . content )

print ( f " Image saved successfully as ’{ local_file_path } ’ " )

29 else :

30

31

print ( " Failed to download the image . Status code : " ,

image_data_response . status_code )

In this example an image of ginger kitten (see below) is created with the prompt ’a ginger

kitten’ in the request. The parameter n=1 means requesting only 1 image. Each image can

be returned as either a URL (default) or Base64 data, using the response format parameter.

URLs will expired after an hour.

37

Figure 15: A cute ginger kitten.

For full details of this API visit

https://platform.openai.com/docs/api-reference/images.

9.2 Create image edit

API endpoint: POST https://api.openai.com/v1/images/edits

Function: client.images.edit()

Model endpoint compatibility: dall-e-2

This example demonstrates how to use DALL-E-2 to modify an existing image by specifying

which part of the image to change and describing the desired changes in text.

Note: The input image must be a square PNG image less than 4MB in size

1 import requests

38

2 from openai import OpenAI

3

4 client = OpenAI ()

5 response = client . images . edit (

model = " dall -e -2 " ,

image = open ( " Son_of_Man_detail_resized . png " , " rb " ) ,

prompt = " complete the face of the man in the painting . " ,

size = " 1024 x1024 " ,

n =1 ,

6

7

8

9

10

11 )

12

13 image_url = response . data [0]. url

14

15 # Send a GET request to download the image data

16 image_data_response = requests . get ( image_url )

17

18 # Check if the request was successful ( status code 200)

19 if image_data_response . status_code == 200:

20

21

22

23

24

25

local_file_path = " son_of_man_processed . png "

# Write the image data to a local file

with open ( local_file_path , " wb " ) as file :

file . write ( image_data_response . content )

print ( f " Image saved successfully as ’{ local_file_path } ’ " )

26 else :

27

28

print ( " Failed to download the image . Status code : " ,

image_data_response . status_code )

Initially, we started with an image, in our example we used an image called ’Son of Man de-

tail.png’, which is Ren ´e Magritte’s famous painting ”The Son of Man”. This image featured

an apple obscuring the face of the man. Let’s break down the process of preparing the orig-

inal image below for editing with DALL-E using Photoshop or any similar tool (I personally

used GIMP):

39

Figure 16: Son of Man.png

• Erasing specific areas of the image: First, open the image ’Son of Man.png’ in Photo-

shop or GIMP or any other image editing software. Identify the areas of the image that you

want to make transparent or remove. In this example, we chose to remove the apple and

make the area transparent. Then make the image square by adjusting the canvas size.

• Saving as PNG: Once we’ve finished editing, save the image in PNG format.

• Uploading to DALL-E: After saving the image as a PNG with transparent areas, we can

upload it to DALL-E 2 for editing.

40

Figure 17: Image with transparent area, resized, and saved as png

Figure 18: Image processed by DALL-E 2

DALL-E 2 will recognise and interpret the transparent pixels in the uploaded image as ed-

itable regions. We prompt DALL-E to ”complete the face of the man in the painting.” and

it produced the in Figure 18.

41

9.3 Create image variations

API endpoint: https://api.openai.com/v1/images/variations

Function: client.images.create.variation()

Model endpoint compatibility: dall-e-2

Note: Similar to the edits endpoint, the input image must be a square PNG image less

than 4MB in size

The image variations endpoint allows you to generate a variation of a given image. A varia-

tion simply prompts DALL-E-2 model with an image, rather than a prompt.

In response to the image provided, DALL-E-2 creates an image of what it thinks is pretty

similar to the one provided. This example demonstrates how to upload a photo of a person

and in response we get variations of the photo after each API call.

1 import requests

2

3 from openai import OpenAI

4

5 client = OpenAI ()

6 response = client . images . create_variation (

model = " dall -e -2 " ,

image = open ( " martin_1024 . png " , " rb " ) ,

size = " 1024 x1024 " ,

n =1 ,

7

8

9

10

11 )

12 # Extract the image URL from the API response

13 image_url = response . data [0]. url

14 print ( " Image URL : " , image_url )

15

16 # Send a GET request to download the image data

17 image_data_response = requests . get ( image_url )

18

19 # Check if the request was successful ( status code 200)

20 if image_data_response . status_code == 200:

42

21

22

23

24

25

26

27

28

29

# Specify the local file path where you want to save the

image

# Change the file name and extension as needed

local_file_path = " martin_variation_v1 . png "

# Write the image data to a local file

with open ( local_file_path , " wb " ) as file :

file . write ( image_data_response . content )

print ( f " Image saved successfully as ’{ local_file_path } ’ " )

30 else :

31

32

print ( " Failed to download the image . Status code : " ,

image_data_response . status_code )

The original photo look like this:

Figure 19: Original photo uploaded to DALL-E-2 to get variations

And after calling the variation API three times:

43

(a) Version 1

(b) Version 2

(c) Version 3

Figure 20: Martin Variations

10 Moderation

API endpoint: POST https://api.openai.com/v1/moderations

Function: client.moderations.create()

Model endpoint compatibility:

text-moderation-stable, text-moderation-latest

The OpenAI Moderation API offers powerful tools for content moderation, enabling devel-

opers to filter and assess text for various levels of appropriateness and compliance with

guidelines. The API can assess text for potential offensive, inappropriate, or sensitive con-

tent based on predefined criteria.

This example demonstrates how to use the Moderation API by sending text inputs to the

API endpoint, and receive moderation results that indicate the level of appropriateness or

potential issues detected in the text.

1 from openai import OpenAI

2 import json

3

4 # Initialize the OpenAI client

5 client = OpenAI ()

6

7 # Call the moderation API

8 response = client . moderations . create ( input = " I love kittens . " )

9 output = response . results [0]

10

44

11 # Extract relevant data from the output object

12 categories_data = {

" harassment " : output . categories . harassment ,

" harassment_threatening " : output . categories .

harassment_threatening ,

" hate " : output . categories . hate ,

" hate_threatening " : output . categories . hate_threatening ,

" self_harm " : output . categories . self_harm ,

" self_harm_instructions " : output . categories .

self_harm_instructions ,

" self_harm_intent " : output . categories . self_harm_intent ,

" sexual " : output . categories . sexual ,

" sexual_minors " : output . categories . sexual_minors ,

" violence " : output . categories . violence ,

" violence_graphic " : output . categories . violence_graphic ,

" self_harm_intent " : output . categories . self_harm_intent ,

" self_harm_instructions " : output . categories .

self_harm_instructions ,

" harassment_threatening " : output . categories .

harassment_threatening

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27 }

28

29 category_scores_data = {

30

31

32

33

34

35

36

37

" harassment " : output . category_scores . harassment ,

" harassment_threatening " : output . category_scores .

harassment_threatening ,

" hate " : output . category_scores . hate ,

" hate_threatening " : output . category_scores . hate_threatening ,

" self_harm " : output . category_scores . self_harm ,

" self_harm_instructions " : output . category_scores .

self_harm_instructions ,

" self_harm_intent " : output . category_scores . self_harm_intent ,

" sexual " : output . category_scores . sexual ,

45

" sexual_minors " : output . category_scores . sexual_minors ,

" violence " : output . category_scores . violence ,

" violence_graphic " : output . category_scores . violence_graphic ,

" self_harm_intent " : output . category_scores . self_harm_intent ,

" self_harm_instructions " : output . category_scores .

self_harm_instructions ,

" harassment_threatening " : output . category_scores .

harassment_threatening

38

39

40

41

42

43

44 }

45 # Create a serializable dictionary from extracted data

46 json_data = {

" categories " : categories_data ,

" category_scores " : category_scores_data ,

" flagged " : output . flagged

47

48

49

50 }

51 # Convert the dictionary to JSON format

52 json_output = json . dumps ( json_data , indent =4)

53

54 # Specify the file path to save the JSON output

55 file_path = " moderation_output . json "

56

57 # Save the JSON output to a file

58 with open ( file_path , " w " ) as json_file :

json_file . write ( json_output )

59

60

61 print ( f " JSON output saved to { file_path } " )

The ’flagged’ attribute in the moderation result is false, indicating that the text is considered

appropriate and does not violate the predefined moderation guidelines for the specified

categories.

46

11 File API

This endpoint enables uploading, listing, retrieving and deleting files. Those files can be

used for text processing, fine-tuning jobs or batch operations.

11.1 Upload files

API endpoint POST https://api.openai.com/v1/files

Function: client.files.create()

Files uploaded will be stored under user’s organisation account. This example demonstrates

uploading jsonl file for batch processing job.

1 from openai import OpenAI

2 client = OpenAI ()

3

4 file_name = " batch_movies_categories . jsonl "

5

6 batch_file = client . files . create (

file = open ( file_name , " rb " ) ,

purpose = " batch "

7

8

9 )

10 print ( batch_file )

• ”purpose” is the intended purpose of the uploaded file. This allows OpenAI to validate the

format of the uploaded file is correct for intended purpose.

• You can check the physical file uploaded in your account https://platform.openai.com/

storage/files. The file uploaded in this example was batch movies categories.jsonl.

We are going to use this file in our next section Batch API.

• The upload file request returns file object:

file_obj = FileObject(

id=’file-UtpG0tLcAaJzUyPG16RcbK18’,

bytes=22335,

created_at=1715204968,

47

Figure 21: Oraganisation account storage

filename=’batch_movies_categories.jsonl’,

object=’file’,

purpose=’batch’,

status=’processed’,

status_details=None

)

The id is file identifier, which can be referenced in the API batch endpoint.

11.2 List files

API endpoint GET https://api.openai.com/v1/files

Function: client.files.list()

This example demonstrates how to list all files uploaded to your organisation account.

1 from openai import OpenAI

2

3 client = OpenAI ()

4 files = client . files . list ()

5

6 print ( files )

The request returns a list of file objects.

We can also retrieve files that are used for batch processing by passing the ’purpose’

parameter.

1 from openai import OpenAI

2

48

3 client = OpenAI ()

4 files = client . files . list (

purpose = " batch "

5

6 )

7 print ( files )

Another method to access files within the organisation’s account is by visiting https://

platform.openai.com/storage (see Figure 7).

11.3 Delete file

API endpoint DELETE https://api.openai.com/v1/files/file id

Function: client.files.delete(file id)

This example demonstrates how to delete a file stored in your organisation account.

1 from openai import OpenAI

2

3 client = OpenAI ()

4 file_id = " file - tqNcExjzNqpZaARzbkGNhLGt "

5 delete_status = client . files . delete ( file_id )

6

7 print ( delete_status )

Another method to delete a file within the organisation’s account is by visiting https://

platform.openai.com/storage and choose the file to delete by clicking on it and press

Delete icon.

Figure 22: Delete file

49

12 Batch API

The Batch API was developed as a cost-effective solution with a promise of a 50% discount

on usage. This is particularly useful for processing tasks where immediate responses are

not necessary.

If you are sending multiple requests to the same endpoint, you can batch the prompts to be

sent in the same request. This will reduce the number of requests you need to make. The

prompt parameter can hold up to 20 unique prompts. For now, the only available endpoints

for batching are /v1/chat/completions (Chat Completions API including vision models) and

/v1/embeddings (Embeddings API). The batch request will be processed within 24 hours. It

can support up to 50,000 requests per batch.

The following steps explains how to create, retrieve and cancel batch job to OpenAI Chat-

Completion endpoint.

12.1 Example without batch job

First, let’s send 20 requests to the ChatCompletion API as synchronous requests and get

immediate result.

1 import pandas as pd

2 from openai import OpenAI

3 client = OpenAI ()

4

5 file_path = " movies . csv "

6

7 system_prompt = """

8 Your goal is to extract movie categories .

9 You will be provided with a movie title and description , and you

will output a json object containing the following information

:

10

11 {

12

categories : string [] // Array of categories based on the

movie description ,

50

13 }

14

15 Categories refer to the genre or type of the movie , like

16 action , adventure , comedy , crime , drama , fantasy , horror , mystery

, romance , sci -fi , thriller , etc .

17 Keep category names simple and use only lower case letters .

18 Movies can have several categories , but try to keep it under 1 -2.

19 Only mention the categories that are the most obvious based on

the description .

20 """

21

22

23 def get_categories ( title , description ) :

24

25

26

27

28

29

30

31

32

33

34

35

36

37

38

39

40

41

content = f " Movie title : { title } - Movie description : {

description } "

response = client . chat . completions . create (

model = " gpt -3.5 - turbo " ,

temperature =0.1 ,

# This is to enable JSON mode , making sure responses are

valid json objects

response_format ={

" type " : " json_object "

} ,

messages =[

{

} ,

{

" role " : " system " ,

" content " : system_prompt

" role " : " user " ,

" content " : content

51

}

] ,

)

return response . choices [0]. message . content

42

43

44

45

46

47

48 # Read the CSV file into a DataFrame

49 df = pd . read_csv ( file_path )

50

51 for index , row in df . iterrows () :

52

53

54

55

56

57

58

movie_title = row [ " Movie title " ]

movie_description = row [ " Description " ]

completion = get_categories ( movie_title , movie_description )

print ( f " Title : { movie_title }\ nDescription : {

movie_description }\ n \ nCategories : { completion } " )

print ( " \ n \n - - - - - - - - - - - - - - - - - - - - - - - - - - - -\ n \ n " )

The output of the example above for each movie looks like:

1 Title : The Fifth Element

2 Description : In the colorful future , a cab driver unwittingly

becomes the central figure in the search for a legendary

cosmic weapon to keep Evil and Mr . Zorg at bay .

3

4 Categories : {

" categories " : [ " sci - fi " , " action " ]

5

6 }

7 - - - - - - - - - - - - - - - - - - - - - - - - - - - -

8 Title : Twilight

9 Description : When Bella Swan moves to a small town in the Pacific

Northwest , she falls in love with Edward Cullen , a mysterious

classmate who reveals himself to be a 108 - year - old vampire .

10

52

11 Categories : {

" categories " : [ " romance " , " fantasy " ]

12

13 }

12.2 Example with batch job

In this example we are going to use OpenAI Batch API to send the same 20 requests to

ChatCompletion endpoint. Those 20 requests are asynchronous group which means the

12.2.1 Preparing jsonl file

The jsonl file should have one json object for each request. This is the structure of the json

object:

1 {

" custom_id " : < REQUEST_ID > ,

" method " : " POST " ,

" url " : " / v1 / chat / completions " ,

" body " : {

" model " : < MODEL > ,

" messages " : < MESSAGES > ,

// other parameters

}

2

3

4

5

6

7

8

9

10 }

The <REQUEST ID> must be unique per batch file.

1 import pandas as pd

2 import json

3 from openai import OpenAI

4 client = OpenAI ()

5

6 input_file_path = " movies . csv "

7

8 system_prompt = """

9 Your goal is to extract movie categories .

53

10 You will be provided with a movie title and description , and you

will output a json object containing the following information

:

11

12 {

13

14 }

15

categories : string [] // Array of categories based on the

movie description ,

16 Categories refer to the genre or type of the movie , like

17 action , adventure , comedy , crime , drama , fantasy , horror , mystery

, romance , sci -fi , thriller , etc .

18 Keep category names simple and use only lower case letters .

19 Movies can have several categories , but try to keep it under 1 -2.

20 Only mention the categories that are the most obvious based on

the description .

21 """

22

23 # Read the CSV file ( input file with data ) into a DataFrame

24 df = pd . read_csv ( input_file_path )

25

26 tasks = []

27

28 # Creating an array of json tasks

29 for index , row in df . iterrows () :

30

31

32

33

34

35

36

37

movie_title = row [ " Movie title " ]

movie_description = row [ " Description " ]

content = f " Movie title : {

movie_title } - Movie description : { movie_description } "

task = {

" custom_id " : f " request -{ index } " ,

" method " : " POST " ,

54

" url " : " / v1 / chat / completions " ,

" body " : {

" model " : " gpt -3.5 - turbo " ,

# you can replace this

with any model

" temperature " : 0.1 ,

# low temp to generate more

predictable responses

" response_format " : {

# response should be formatted

as json

" type " : " json_object "

} ,

" messages " : [

{

} ,

{

}

" role " : " system " ,

" content " : system_prompt

" role " : " user " ,

" content " : content

] ,

}

}

tasks . append ( task )

38

39

40

41

42

43

44

45

46

47

48

49

50

51

52

53

54

55

56

57

58

59 # Creating the jsonl file

60 batch_file_name = " batch_movies_categories . jsonl "

61

62 with open ( batch_file_name , " w " ) as f :

63

64

for obj in tasks :

f . write ( json . dumps ( obj ) + " \ n " )

55

12.2.2 Upload batch file

The file ”batch movies categories.jsonl is already uploaded to OpenAI platform in the

previous section 5.1 Uploading file. The id of the file is ”fileUtpG0tLcAaJzUyPG16RcbK18”

which we are going to use next.

12.2.3 Creating batch job

Create batch: POST https://api.openai.com/v1/batches

Function: client.batches.create()

Endpoint: /v1/chat/completions and /v1/embeddings

This example demonstrates how to create a batch process job with 20 tasks.

1 from openai import OpenAI

2 client = OpenAI ()

3

4 batch_file_id = " file - UtpG0tLcAaJzUyPG16RcbK18 "

5 batch_job = client . batches . create (

input_file_id = batch_file_id ,

endpoint = " / v1 / chat / completions " ,

completion_window = " 24 h "

6

7

8

9 )

10

11 print ( batch_job )

The request returns a batch object:

batch_obj = Batch(

id=’batch_vfcrxpxFSs6U5xinlOaoXLki’,

completion_window=’24h’,

created_at=1715212754,

endpoint=’/v1/chat/completions’,

input_file_id=’file-UtpG0tLcAaJzUyPG16RcbK18’,

object=’batch’,

status=’validating’,

56

cancelled_at=None,

cancelling_at=None,

completed_at=None,

error_file_id=None,

errors=None,

expired_at=None,

expires_at=1715299154,

failed_at=None,

finalizing_at=None,

in_progress_at=None,

metadata=None,

output_file_id=None,

request_counts=None

)

12.2.4 Checking batch status

Retrieve batch: GET https://api.openai.com/v1/batches/{batchID}

Function: client.batches.retrieve(batchID)

To check the status of the batch job using the API endpoint:

1 from openai import OpenAI

2 client = OpenAI ()

3

4 batch_job_id = " batch_vfcrxpxFSs6U5xinlOaoXLki "

5 batch_job = client . batches . retrieve ( batch_job_id )

6 print ( batch_job )

To view the batch job status and other info, navigate to https://platform.openai.com/

batches in your account and click on the batch job. The current screen shot shows the job

is in progress and non of the request has processed yet (see Figure 8).

After couple of hours I checked the batch job again. The status is completed, and there are

zero failed requests. There is also a link to download the output provided (see Figure 9).

57

Figure 23: Batch job status in progress

The batch job returns from OpenAI has the following information:

batch_obj = Batch(

id=’batch_vfcrxpxFSs6U5xinlOaoXLki’,

completion_window=’24h’,

created_at=1715212754,

endpoint=’/v1/chat/completions’,

input_file_id=’file-UtpG0tLcAaJzUyPG16RcbK18’,

object=’batch’,

status=’completed’,

cancelled_at=None,

cancelling_at=None,

completed_at=1715213179,

error_file_id=None,

errors=None,

expired_at=None,

expires_at=1715299154,

failed_at=None,

finalizing_at=1715213178,

in_progress_at=1715212754,

metadata=None,

output_file_id=’file-jZfTsfPbNa16rZQ2vk6dw3PG’,

request_counts=BatchRequestCounts(

completed=20,

58

failed=0,

total=20

)

)

Figure 24: Batch job status completed

12.3 Cancelling a batch

Delete batch: POST https://api.openai.com/v1/batches/batchID/cancel

Function: client.batches.cancel(batchID)

The following example demonstrates how to cancel or delete a batch job.

1 from openai import OpenAI , ConflictError

2

3 client = OpenAI ()

4 batch_job_id = " batch_vfcrxpxFSs6U5xinlOaoXLki "

5

6 try :

7

8

9

batch_job = client . batches . cancel ( batch_job_id )

print ( " Batch job cancellation successful ! " )

print ( batch_job )

10 except ConflictError as e :

11

12

error_message = str ( e )

print ( f " Failed to cancel batch job : { error_message } " )

59

The objective of the code is to attempt to cancel a batch job with a given ID using the

API endpoint, handling a potential conflict error (ConflictError) that may arise if the batch

job is already completed, and printing appropriate messages based on the outcome of the

cancellation attempt.

12.4 List batch

List: GET https://api.openai.com/v1/batches

Function: client.batches.list

The following example demonstrates how to list all batch jobs in your organisation.

1 from openai import OpenAI , ConflictError

2 client = OpenAI ()

3 batches = client . batches . list ()

4 print ( batches )

60

Terminology

Prompts and completions : Language Models are trained to predict natural language and

provide text outputs as a response to their inputs. The inputs are called prompts and

outputs are referred to as completions.

Token : The basic unit of text processed by models like GPT-3.5 and GPT-4. Tokens can

be as short as one character or as long as one word.

hallucinations : Hallucinations can occur if the model doesn’t have enough context or if it’s

required to ”imagine” details not explicitly provided. For example, if an AI is asked a

question about a specific document but doesn’t have access to that document, it might

generate an answer based on its training data, which could be incorrect or fabricated.

Retrieval augmented generation (RAG) : Some of the tasks performed by LLM required

additional knowledge to answer responses correctly. RAG combines an information

retrieval component with a text generator model. Before generating a response, the

model retrieves relevant information from a large external knowledge base or docu-

ment collection. This step ensures that the model has access to up-to-date and accu-

rate information (retrieval process) . The retrieved information is then used to inform

the text generation process. The language model generates responses based on both

the retrieved content and its pre-existing knowledge (augmented generation process).

61

References

• OpenAI API Reference: https://platform.openai.com/docs/api-reference/

• OpenAI Models Documentation: https://platform.openai.com/docs/models

• openai-python SDK https://github.com/openai/openai-python/blob/main/api.md

• Ultimate guide to DALL·E 2 https://dallery.gallery/dall-e-ai-guide-faq/

• OpenAI Cookbook https://cookbook.openai.com/

• OpenAI terms & policies https://openai.com/policies/

• OpenAI API Privacy Policies Explained

https://brightinventions.pl/blog/

openai-api-privacy-policies-explained/

62

