# APRIL 2023

# 2023-xmpro-product-roadmap---webinar
{% embed url="https://www.youtube.com/watch?v=XeEpso-ykMI" %}



Join XMPro Development Manager, Daniel King as he takes you through our highly anticipated product roadmap covering the Now, Next, and Later product releases.
<details>
<summary>Transcript</summary>Join XMPro Development Manager, Daniel King as he takes you through our highly anticipated product roadmap covering the Now, Next, and Later product releases.
welcome to the XM Pro product roadmap

webinar for 2023 I'm Daniel King

development manager at XM Pro I'm based

in Sunshine Coast Queensland Australia

and I'd like to thank you all for taking

the time to attend today

I have a lot to cover off today so if

you have any questions please send them

through and I'll try to answer them at

the end

2023 has been an amazing year so far and

I can't believe it's halfway already

I won't be recapping recently delivered

items in this session but I'd like to

encourage you to go to our website and

check out our latest release notes

there are three key achievements I would

like to call out though 83 of our agency

connectors have been contributed to so

far this year which is massive I'll be

partnered with Dell Technologies to

create a validated design for the

manufacturing Edge and work with Nvidia

to validate XM Pro as GPU enabled or

accelerated and Enterprise ready

I'd like to take a second here to thank

the XM pro team for their contributions

and making all this happen I know a few

of them are watching today so thank you

the intelligent digital twins framework

is a strategy for our product

Peter Van scope fake is CEO of XM Pro

and co-chair for the natural resources

of working group at the digital twin

Consortium

here goes into much more detail on our

strategy and if you haven't already

watched this previous webinar I'd highly

recommend you do so you can find it on

our XM Pro channel in YouTube

the i3c framework is a longer term view

of where we're heading

and the product roadmap represents the

items we're working on now and next to

get us there I won't be able to cover

everything on a roadmap in 30 minutes

but I'll try my best to cover as much as

I can today

four pillars of the XM Pro product are

how we execute on the i3c framework

together they support each of our three

themes faster time to Value distributed

intelligence and secure cost deployments

the triangle layout demonstrates how

each of these Builders support each

other

and the pillars have varying impact on

people processing Technology based on

their proximity to these little labels

here

the robot items will be grouped by

pillar and I'll be talking through each

roadmap item for each of these pillars

distributed intelligence is achieved

through Ai and Engineering where people

and Technology meet to innovate execute

and augment with AI

I think that's pretty cool

we're going to start today with AI and

Engineering pillar

47 of all iot applications will be AI

infused in 2027. that's a 30 increase in

under four years that's that's that's

amazing we want to enable our customers

to be part of that 47 percent

and we're doing this with a number of AI

roadmap items

so we're going to focus on Innovation

with AI first

AI is fast growing and disrupting

markets around us and it offers new

tools to do things differently but these

tools are rapidly changing this is why

we think Innovation with AI is critical

X and pro notebooks is a new product

we'll be releasing as part of our AI

offering it supports Jupiter notebooks

allowing you to use a well-established

product without having to retrain people

or refactor existing notebooks XM Pro

notebooks can be used in data science

scientific Computing and machine

learning and data scientists analysts

and Engineers will be able to access

data to innovate within the XM Pro Suite

each user will have their own dedicated

notebook actively using the product this

makes it very scalable and cost

effective as you experiment

one of the biggest challenges for data

scientists is the access to good data to

innovate with

we're adding integration to our data

stream data so excellent Pro notebooks

can access the rich and near real-time

data in transit

this scenario isn't just limited

real-time data though in data streams

you can also run simulations on your

data streams and access that same data

from Maximum code notebooks the same way

this approach also allows users to focus

on innovation without first having to

develop software and Integrations up

front

it also allows for continuous innovation

and experimentation over time

we currently support the ability to run

simulations on streams visualize the

results in apps

front running simulations is the ability

to run a simulated event just before the

real event to predict what that result

would be

and this example we're simulating an

event right before the real event to see

what the outcome would be and in this

case it would have been a bad outcome

this allows you to build functionality

into a stream to modify the path

an event takes ultimately ensuring that

you get a good outcome

so let's talk about when these things

are coming so the now Title Here

represents an item that's actively in

development or scheduled for release

soon and the next title represents work

with developers not yet commenced or is

blocked by another item

we practice hypothesis driven

development at xmpros this means that

items can shift or change the scope

based on what we learned

development for the X and pro notebooks

has completed and the team are working

on productizing it for our supported

platforms and

Cloud providers

it will be the first available on our

free trial offering which is probably

only days away at this stage or really

close and it'll become available

incrementally on our installers for

different clouds and platforms

next we'll be releasing support to

consume stream data in those notebooks

and we're in the early stages of

planning for this

front running simulations is also in the

early stages of planning

once you've innovated and produced new

AI Solutions you need a way to execute

them

running AI in our streams is one way to

do this and up until recently you'll be

limited running these on the CPU

the GPU is well suited for running

certain workloads and involve a lot of

concurrent processing

moving processing to the GPU can vastly

improve how much processing you can do

in the same time frame compared to the

CPU mathematical algorithms Machine

Vision neural networks and deep learning

are examples of workloads that involve a

lot of concurrent processing

in this example we're using a Machine

Vision to process apples and oranges

differently in our data stream

images of our fruit are ingested by a

data stream as an agent compares the

images pixel by pixel to determine if

the if it's an apple or an orange

by using the GPU to run pixel comparison

algorithms we can process a lot more

images

this stream can still be run on the edge

Fogle cloud

and it can also dynamically detect if

there's a compatible Nvidia GPU and use

it falling back to the CPU when the GPU

isn't available

there are a handful of scripting

languages that are fast becoming

standard for executing AO workloads by

supporting these scripting languages we

support customers in running their

existing Solutions in our streams this

reduces the need to refactor or retrain

staff and you can adopt new

functionality faster as is the large

open source Community currently

innovating using these scripting

languages

we're extending our current agents to

support more of these scripting

languages

we're also adding support for more

governments around these scripts in this

example you can see we can run a script

directly in an agent or reference the

latest published version of a script

from the common storage layer

for now I think of the common storage

layers kind of like GitHub and I'll talk

about this later

these scripts can be edited from the X

and pro notebooks allowing users to

operate completely in our suite of

products

data streams are executed for us to buy

our stream hosts and these stream hosts

can be run on the edge of fog and Cloud

allowing you to distribute your

processing fully strict scripts uh

providing like a very flexible and

composable architecture

thank you now we've recognize you may

have your own machine learning

operations or mlops

they're focused on streamlining the

process of taking machine learning

models to product and then maintaining

and monitoring them

mlop space it's it's growing very

quickly and there's a vast variety of

different third-party Solutions our

approach here is to create agents to

integrate these third-party Solutions

mlflow is our open source platform for

managing the end-to-end machine learning

life cycle

and is fast becoming the the most

popular in the space

we have created an ml flow agent that

can get the latest published version of

a model

and invoke it with data from the our

data stream and then return those

results back this prevents the the need

for a data science to actually go into a

data stream and update that stream each

time a new version of the model is

created

it also allows heavy processing of ml

models to be run on the customer systems

optimize already for these workloads

it also allows access to be restricted

to the data stream supporting the

principle of least privilege

mlops can be orchestrated from XM Pro

notebooks allowing you to run

experiments create models publish those

models and then invoke them directly

from The Notebook then using the results

foreign

GPU acceleration support is currently

available you can design Aid install

leverage Nvidia gpus using agent

documentation and we'll be extending

this documentation to provide more

examples and support

we're also working on adding GPU

acceleration support to some of our

existing agents

we currently have a python script and

we're close to releasing an R script

agent we'll be adding more governance

controls and integration to these to

these scripts using the common storage

layer after it's released and I'll talk

about talk more about that common source

layer layer later

we've recently developed the ml for

agent for integrating to customer lmops

and we're updating our public docs right

now before we actually release it

now the innovating and executing with AI

there's a great opportunity to augment

what we have now with these results

we currently have recommendations

capability and for those that aren't

familiar at a very high level you can

create recommendations with rules that

when are met generate alerts

we found that existing recommendations

can be augmented with AI anomalies can

be dynamically detected and visualized

with inside the recommendations

new recommendations can be automatically

generated or discovered

and rules within those recommendations

can be created or augmented

and alerts themselves can be augmented

with copilot like functionality and

assisting assisting engineers in in

resolving these alerts

chat GTP and open API services are

continuing to provide new and easier

innovative ways of doing things

accent Pro notebooks will be released

with a sample notebook demonstrating

integration to chat GTP in this sample

notebook it includes an end-to-end beer

quality example which incorporates chat

GTP and who doesn't like quality beer

data stream designer Integrations will

allow you to augment your event data

with chat GTP and app designer

Integrations will allow you to make

custom calls

from your apps enabling co-pilot like

functionality

the security of our data we will we uh

security fuel data and and how we

implement this is really important to us

we use the third-party services like GTP

takes a lot of our consideration and

we'll be factoring this into you know

how we solve these problems and deliver

these new product roadmap items

visualization of AI outputs is a really

powerful and effective way of

communicating the insights you're making

excellent Pro notebooks will allow you

to generate visualizations that you can

share in apps in this example we'll be

using chuckttp to generate a linear

regression visualization for us

it's using the data for my data streams

and it's checking to be savings a lot of

time because we're not having to find

the suitable libraries and write the

code to do this ourselves

Excel Pro notebooks will be released

with chat GTB integration support and

samples on how to get going quickly you

can currently integrate you integrate to

check GTP via our Python scripts and run

these in agents right now

and these Python scripts can be designed

and managed in X and pro notebooks

we will have importable end-to-end

Solutions as our starting point to get

you going faster for our common use

cases and additionally planning for app

designer and data stream designer

integration

as this is currently underway and it

will provide more additional no code

approaches

AI generated or discovered

recommendations is in the early stages

of planning there are some core

technical pieces that are needed before

we can start this work and the

development team are busy work on these

right now

generating analytics and visualizations

is currently available through a mix of

approaches we're currently planning on

how to extend these approaches to closer

integrate x and pro notebooks allowing

from a more seamless experiment

experience from right through from

Innovation through to augmentation and

the visualization

all these new AI roadmap items need

distributed computing and network

infrastructure management to support an

edge ecosystem

this is the cloud to Edge continuum

we currently support deployments to a

wide variety of cloud providers and

on-prem platforms using cloud and

platform native services

this creates additional overhead for us

and our customers as we add more

features demanding more capabilities in

this area

these environments can be configured in

many different ways and also change and

sometimes without our control and this

makes it difficult for us to deploy and

support our products simply as

seamlessly

there are new more modern approaches

that are quickly become industry

standard for the type of architecture

that underpins our suite of products

these more modern approaches require us

to change our deployments to embrace

them

we'll be creating a cloud agnostic

deployment for our suite of products

that will become the default deployment

method

the aim is to provide a product that is

more portable allowing for business

better business continuity planning more

reliable with self-healing properties

and more performant allowing for better

performance for Less cost

now we currently support distributed

deployment and in this example we have

products used most by our users in the

cloud in regions closest to those users

making the products feel fast and snappy

in the fog we have our AI capabilities

closest to where most of our data is

reducing the time to transmit large

volumes of data over the wire and on the

edge we have our stream hosts these are

our engines that run our data streams by

putting them on the edge we put them

closest with the devices and Edge

systems are

the challenge with this approach is

managing all these Edge deployments

without some form of centralized

monitoring alerting and management it

can become difficult and time consuming

for iot to manage these systems

this is why we're building support for

third-party systems that provides

centralized monitoring alerting and

management capabilities

we're adopting industry standards and

best practices to allow us to easily add

additional providers over time and this

also provides customers with the

flexibility to use their existing

providers if they have them

the solution would be composable with

the ability to select different

providers from different functions

instead of having to commit to one

system to do it all

we're bringing devsecops capabilities to

our sweeter products

we're not building these capabilities

into our products but again leveraging

existing industry standards and best

practices to allow you to use your own

providers

in this example we have a pre-pro

environment that we want to design our

streams and apps before we publish them

to production

these new versions of apps and streams

are automatically exported to the common

storage layer and from there UI test

automation can be run leveraging our XM

Pro test automation Library

secure testing can be performed on any

changes to say Integrations to mitigate

any potential vulnerabilities and when

all these pre-checks pass the change is

then approved and these versions can be

published to our products or your

product environment or the customer

support environment

we can take a similar approach to

upgrades to X and pro new versions can

be automatically and programmatically

installed in pre-prod manual regression

or just automated UI testing performed

and then deployed to production

we've just released automated database

installs and upgrades

which allows for a fully automated

deployment our current deployment

options required a customer though to

set up Automation in their third-party

systems

best practices have evolved since some

parts of the process were first

developed and we need to redesign these

and we'll provide be providing improved

deployment automation incrementally

product by product

we've completed several proof of

Concepts around Cloud agnostic

deployment

with commence development and are taking

our product by product approach and

we'll continue to support cloud data for

some time shifting to Cloud agnostic

deployments as default and they're done

we're looking to cater for customers who

want an out-of-the-box experiments where

they can use all the default deployment

configuration that we provide right

through to those that want to consume

the individual product artifacts and

build them into their own custom

deployment

we've completed a proof of concept I

distributed deployment management based

on our Cloud agnostic approach and we're

in the planning state of considering a

mix of internal and external third-party

tooling to be rolled out incrementally

faster time to value is achieved through

roadmap items that combine people

and process to accelerate transformation

we're providing more support for what

you have when it comes to visualizations

we use blocks to compose apps and

already have a large library of blocks

to do this however some scenarios it's

quite difficult to create a block for

example

if a customer system uses an

incompatible technology or uses an old

technology that performs slowly or is

just custom or an in-house system

meta blocks will allow us or you to

create custom blocks to overcome these

challenges

it'll allow you to run visualizations

side by side that traditionally just

wouldn't be possible

with this capability you will be able to

create an industrial metaverse that runs

on the same backbone of event data

without first needing to re-platform

your existing exist existing systems to

like a common technology

this gives you the flexibility to delay

deciding when that common technology

needs to be and what it needs to be

until that Industrial metaverse

Technologies and processes stabilize and

you can make a better decision about

that

I've mentioned the common storage layer

a number of times already in this

presentation

and that's because it will unite

artifacts across XM Pro think of it as

kind of like GitHub

except we'll be implementing it in a way

that allow you to choose the provider so

it doesn't have to be GitHub it'll also

be comprised of several different

Technologies allowing for the best

technology for the job and using best

practices to do it

the common storage layout will allow you

to collaborate faster and safer

providing well-known interfaces and

governance controls to do this

anything you can currently export or

import can be managed here and all the

new artifacts discussed today will be

stored here

the provider you choose for the common

storage layer will also support

integration most likely and allowing you

to automate and tie in artifacts from

Max and pro into your current existing

systems

we're introducing some new artifacts the

common series later get you started

quicker and keep you innovating

blueprints are pre-built Solutions

providing end-to-end working samples

accelerators can be imported into your

environment as a starting point

from which you then can extend from

and patents are pre-configured data

streams at servers building blocks that

you can compose and extend out

you'll also be able to create your own

versions and collaborate internally and

externally

so we currently have a library

predefined Solutions in our XM Pro

GitHub project which you can now check

out

we'll also continue to add to these over

time and next we're looking at adding a

library UI into our accent pro products

to access and integrate them a little

bit more easier

we've completed a perfect concept of

meta blocks and are planning on studying

development soon and we've selected

several new and existing blocks to be

candidates for that first release

we're currently using several providers

for my common storage layer internally

for collaboration and we'll be exposing

these publicly

we're beginning planning We Begin

planning on how we'll integrate these

products in the UI shortly

where process and Technology meet we

need strong governance to be secure

across deployments and we do this with

zero trust architecture

zero trust architecture is not new for

us at X and pro and something we take

really seriously

we aim to give you more control over

what users can access with finer grained

Access Control

the product rights will align closer to

API endpoint functionality and not UI

components we'll still have product

roles to manage any additional

complexity this might introduce and in

this diagram you can see a user

accessing data via connector or

recommendations functionality previously

these would have been these five rights

here would have been three different

rights this change allows for greater

control over what users can access

and by aligning these rights to API

endpoints it makes it simpler to apply

the principle of least privilege at

scale

we currently run several security scans

every three months months and uh and

publish these results to our website

in addition to this we'll be running

incremental scans on every code change

for each product to pick up potential

vulnerabilities earlier this change will

ensure that any new vulnerabilities are

identified and addressed as soon as

possible

so XM Pro currently supports integration

to Azure ad ID provider providing an

easy way to leverage existing user

logins and security policies and

features like SSO and MFA

we're extending this functionality to

include support for more scenarios like

a Federated tenancy model

this integration has been done using

industry standards making it easier for

us to add new providers when it's

necessary

as we implement the edge to Cloud

Continuum and monitoring and managing

product performance is critical

we need it we're implementing support

for application Performance Management

tooling and we're doing this using

industry standards so adding new

providers will be easier using this

integration you'll be able to monitor

performance of our products

be alerted when there's issues and if

needed do basic troubleshooting yourself

so we're applying finer grade access

controls incrementally to each of our

products with the first product in

development now

we have continuous security scanning set

up on most of our products are in the

process of updating the remaining right

now

and we currently have support for Azure

ID and like I mentioned before we're

just extending this to support more

scenarios like a Federated tenancy model

and we're currently adding support for

Azure app insights as a APN provider

so

we'll be running webinars on the items

shown today as they become available and

diving into a lot more deeper detail

if you have any questions please send

them through and I'll try to answer them

now thanks

thanks Dan um so we've got two questions

here already

um the first one is where can we find

more information on XM Pro AI

okay great question ah thanks Sarah

so that segues really nicely uh next

month Gavin Green will be doing a

webinar on AI and he'll go into a lot

more detail

um I'd encourage you to sign up for that

and attend

um we're very close to releasing X and

pro notebooks in our free trial soon

um I think it's a couple of days away at

the stage just keep an eye out for that

uh sign up have a play around with our

free trial and the different AR

capabilities that are in there and I

also believe we're publishing a web page

specifically around Ai and our website

and the features that you can leverage

there so keep an eye out for that as

well

awesome there's another question here um

it says with Edge to Cloud continuum

providing any

s around containerized architecture

good question uh yes really really

excited about this one

um so actually we currently have Docker

images for our stream hosts these are

the engines that run our data streams

we're adding Docker images for other

products and we'll be creating a

container registry that will be

publishing these two

um we will likely do webinars on this as

this becomes available

um

so yes

awesome and then one very important

question asking will we receive a copy

of the webinar from today

yes yeah this is probably where I do the

uh like And subscribe Us on YouTube

um yes we'll be putting this on YouTube

on our XM Pro Channel all of our

webinars are on there including uh Peter

Scott fakes previous one I mentioned

please jump on there and look at it look

at it um Sarah do you know how long

it'll take for it to get up there

um hopefully we'll get it up today

sometime later on today okay

thanks

that's it for the questions

oh I head over to you oh thanks

okay

um so if you just want to change science

then

cool

thanks everyone um so thanks very much

Dan for taking us through and thanks

everyone for joining us if you're

looking for more information uh you can

contact Dan directly or the team via

these email addresses as Dan mentions

we're running these webinars monthly and

our next session will be on XM Pro AI

presented by Gavin Green so you can

register by scanning the QR code there's

a link in the chat box and I'll also be

sending the link

um shortly when we send the recording

out sometime later on today and we look

forward to seeing you all next month

thank you very much for joining

thank you
</details>


---


# how-to-create-intelligent-digital-twins-using-xmpro-ai
{% embed url="https://www.youtube.com/watch?v=li_EXCTmVOQ" %}



Welcome to our comprehensive webinar hosted by Gavin Green, our VP of Strategic Solutions, titled "How to Create Intelligent Digital Twins Using XMPro AI." We invite you to join us on this...
<details>
<summary>Transcript</summary>Welcome to our comprehensive webinar hosted by Gavin Green, our VP of Strategic Solutions, titled "How to Create Intelligent Digital Twins Using XMPro AI." We invite you to join us on this...
hello everybody and welcome to our XM

Pro AI

um for intelligent digital twins webinar

my name is Kevin green I look after

strategic solutions for XM Pro I want to

thank you for your time attending today

if you've got any questions please send

them through I'm not trying to answer

them at the at the end

in some prior webinars we went through

the four pillars of the the excellent

product I'm not going to go into detail

here

but just in a continuation of that which

pieces are we going to be focusing on

this is in line with our i3c framework

and it's in essence where we focus our

effort when we're putting the product to

Market and the different feature sets

that we are are working on

today's Focus however is going to be on

the AI side of things and what is in the

product that can help you for the

intelligent digital twins with the the

focus on the AI site

before we jump into you'll hear me

talking around intelligent digital Twins

and digital Twins and there is a

difference between the two of those

there was a paper that was written on

the evolution of digital twins

um the two fathers of digital twins

Being John Vickers and the second being

Dr Michael Greaves

um this is Dr Michael greve's vision of

the different stages of evolution of

digital twins these are some slides from

the paper the paper is available down

the bottom and if you're interested we

can send you the link where you can

access the paper as well and it outlines

the different stages and it's also used

as inspiration and a guide within our

software and what it is that we do the

the main Evolution steps you'll see them

on the right there going from zero being

traditional 2D

that evolved into transitional so you're

number one which was 3D cat that went

into number two around the conceptual

this is where

um things started becoming a lot more

model based and then that evolved into

the concept of a digital twin platform

the step number three this is where most

people are at the moment

and they are slowly moving towards the

the number four which is around

intelligent digital twins one of the

applications for intelligent digital

twins is front running simulation it's

by no means the the only one it's just

the one that's front of mind which helps

explain the intelligent aspect of that

as well

when we start comparing digital Twins

versus intelligent digital twins there

are certain characteristics of a digital

twin and then there are characteristics

of an intelligent digital twin I've just

built the slides here again I'm not

going to go into into detail here the QR

code in the middle will take you to a

video which will go into a lot more

around the digital twin capabilities and

characteristics and the intelligent on

the other side

the one piece right at the bottom is the

anticipatory or the front running

simulation side of things

keeping with the the XM Pro product

within our intelligent digital twin

suite for those of you who are familiar

you're familiar with the data stream

designer the DS the app designer which

is the ad here and the subscription

manager of the SM here

the new one which you may not have seen

is around the AI side

rounding out the intelligent digital

twin Suite here

we'll go into that quite a bit of what

I'm going to walk you through you can do

without and I'll touch on some of those

areas where you can and then also touch

on the areas where you do need the the

newest addition here which would be on

the on the AI side

we have to stop in at the tip of the

iceberg where does it slot in so when

most people look at our digital Twins

and this is true for normal digital turn

platforms all the way through to

intelligent digital turns as well as

most people look at the top and they see

the uis there's actually a lot of things

that sit underneath

which is where the recommendations come

in and this is also where we slot in the

AI aspect as well the AI integration the

notebooks as well as how you

operationalize this for the agents you

still have everything else as you are

used to you've still got your data

stream and you've got your subscription

manager as well

we're going to leave the slides here and

we're going to jump into the actual

software itself and we're going to go

through a few examples of what it is

that I'm actually talking about here

so what we put together is we created an

app which will just allow me to walk

through the different bits and pieces

that we've got

let me just get rid of my slides

and we'll come back to to this

so again this is all driven from an

overarching framework which is what we

call our i3c

um and it's broken up into a few

different areas specifically with an AI

Focus for today we're talking around

Innovative embedded and augmented but

how do they all fit together where do

they all work together

we like pictures so we like explaining

how all of these fit together

as it is right now without having to

upgrade any accent Pro you can do

everything on the right here we call

that embedded AI

from the data stream designer how do you

bring the models in maybe you've already

got some models how do you

operationalize them and use them

everything else on the left here is some

of the new capability that we've brought

in with regards to Innovative AI as well

as augmented AI it's not required you

don't have to you can choose to use this

or not use this as well

so as we go into these different areas

what do I mean when I start talking

around Innovative AI we start going into

Excel Pro notebooks and there's two main

items in here the one is around the

ability to discover

so you'll see on the left we have a new

tool and that'll open up what we call

accent Pro notebooks

within here for those who are familiar

and comfortable you'll notice a familiar

environment being a Jupiter notebook

that we've got here

so this allows you to discover work

through and come up with the different

models Etc

any of the libraries that you can use

within a jupyter notebook you can use in

here this particular example I've got

here you can see this is around

predicting and the the beverage industry

using linear regression

as I build through this particular

notebook here you can see I'm going to

import certain libraries and it's going

to walk me through the different pieces

here so if there's a library that

I need for my machine learning or I want

to do some data Discovery I can load it

into the notebook not a problem at all

the other thing that as we work through

this that we've added into this is a

generative AI capability as well

what we mean by that is as I work

through this you'll notice at this point

here we've integrated chatgpt into this

environment as well so what that means

is you can actually use the chat GPT

to help augment and enrich what you're

looking for in here this example that

I've got in here what we're actually

asking

um chat GPT to do is to write me some

code on how to visualize the data that

I'm looking at I'm not an expert in how

I put this together so we're going to

ask and it'll actually generate

the items for me and if I go and run

that now you'll notice that it's going

to run and then it will generate and it

once it comes back it'll actually show

me the plot for the data that I'm

looking for

scroll a bit further down you'll

actually see what that looks like

if we keep going you can start

developing different models as well

if I come back here step one is really

what we call notebooks which allows you

to interact in an environment which is

familiar to you

you don't have to use them in here if

you do use them in here you can start

using some of the other features and the

bits and pieces that we've made

available as well if you have your own

models and you just want to use them and

plug them in by all means you can do

that already in the steps here

the second piece is really when we start

wanting to deploy models so there's two

main things that you can actually do

with the model

the one if I go into a different example

here is I can actually run this

it will generate the model I can help

discover that and the end result is I

can actually save this model to a file

that I cannot use inside the data stream

you can do the same thing right now

let's say you have a jupyter notebook

that sits outside X and pro you've

already doing Discovery you're already

generating models how do you just use

those models and bring them in you can

do that and I'll show you in a data

stream as well

the second thing that we're doing in the

prior example though is we're actually

fitting this model and passing it to a

repository and the reason for this is we

want to introduce a concept of

governance

and make sure that there is a framework

that you can actually deploy into and

that your models can live so that you

don't end up with a an Excel of machine

learning model sitting everywhere no one

knows it's got the latest version of

where it's actually sitting

if you have your own repository by all

means you can actually hook into and use

that as well this example here we're

just talking to to Mr flow as the

repository this is just one example it

is not the only example so if you've

already got one by all means you can

just plug that in and actually use that

as I continue to step through all of

this what it's doing is it's working out

the model it's working out the pieces

and then it is actually publishing that

model to my ml flow repository for me

you'll see it has already existed it's

going to created me a version 5 of that

model and now I can go into my actual

repository and decide when I want to

deploy that or elevate it to production

or not

so if we jump into that and again this

is just one example that we've got it's

not the only repository you can see the

one that we've just pushed through now

so number four is the one which is

currently in production I cannot decide

that number five is ready to go and I

can transition it to staging in a

controlled environment versus working

out well which is my live running model

which one isn't and how do you in a

governance structure move between the

different Frameworks that we're actually

looking at here

number four is currently published and

I'll show you now where that is actually

published and running

so if we come back here we call that

Innovative AI so if I come back to the

diagram that we're looking at here this

is the area that we are working in at

the moment is how do we take training

data how do we ask for specific results

that we are looking for and how do we

run that through a notebook you can't

augment that with chat GPT in this

example and then deploy that to an ml

Ops platform of your choice

you don't have to deploy it you can just

take the actual raw artifact which is a

result of that model and then use it in

a data stream as well

the

preferred or the more governance driven

process is to actually push that through

a

repository because then you get

everything that comes with the

repository as well

I mentioned you can do things right now

you don't need to upgrade or get all the

newest toys in the Box to to be able to

do this this is around the embedded AI

side so if I go into and this will open

up my data stream designer for me

you can do this right now you can drag

on this example has got a python runtime

running here which is running a model

this model was created inside the

notebook it was outputted from The

Notebook and then manually put into the

data stream and used and this is

capability that you can do as I

mentioned right now we call that how do

you use it from a manual perspective

what you'll also notice is there are a

lot of other items in the library

so if python is just being one of them

but let's say you want to use a more

standard algorithm like anomaly

detection or binary classification or

clustering

those agents already exist you can just

drag them on and use them right now

there's nothing stopping you you do not

need a repository you do not need to use

the Excel Pro notebook to take um

advantage of that particular capability

however if you do use a repository

and you actually want to integrate and

make use of that inside the data stream

what we've got here is we're performing

the analysis so this is using the Mr

flow agent so on the left you will see

here is a list of library

one of those being the ml flow

the Mr flow is talking to the repository

and here you can see the actual model

that it's talking to and everything else

is governed as well so I don't need to

remember the URLs I don't need to

remember logons passwords Etc I just

want to use that particular model and

actually just run it and execute it

again this is your governance that sits

around it it makes sure that the models

which you're using to do anomaly

detection Predictive Analytics maybe

you're using it to do forecasting or to

do front running simulation or just to

do normal simulation of current state or

past State you want to make sure that

you're running on the correct model

latest model and that you have control

of that you can do that inside the data

streams that we're looking at in here

so again if we come back

Innovative AI this is a really around

the ability to discover

go in through the particular notebooks

and then how do you use some of those

libraries in there the other example in

here is you can actually just create

models that do simulation so you don't

need to create models that do very

sophisticated

um AI number crunching and algorithms at

output you can do something as simple as

just simulation which is what this

particular example here is doing we're

creating a network we are then deploying

the same model to the repository again

you don't have to

There's an actual example of this one

running just the python itself with the

simulation on top of that as well

this one here is doing a remaining

useful life as well as a more advanced

prediction on the data coming in the one

that I just showed you is doing more

simulation so it caters to to both

there's no

you can do one and not the other

if we go into the augmented side

let me expand that a bit here so

embedded again you can do this right now

there's nothing stopping you from using

the current set of libraries and we're

expanding and adding to those all the

time

ml.net are some of those that you're

seeing in there ml flow when you're

talking to repositories maybe you want

to use some GPU enabled

um

algorithms from the the Nvidia Library

you can do all of that right now within

the embedded side of things

the Innovative is around the notebooks

but augmented is not just in the

notebook section over here

the augmented

AI you can actually use inside your apps

when you create and configure them as

well

what do I mean by that oh let's go into

an example

so I've got a particular app here and on

the right you'll see some

recommendations have triggered

these recommendations you can see

remaining useful life has been declining

and I can go a bit further down and I

can see remaining useful life has been

predicted to be below a certain

threshold again these were running

through the data stream and they can

either be Standalone python or any of

the other algorithms or read the matter

or repository and execute them as well

if I drill into that particular asset

it'll actually filter out my

recommendations for the two that I'm

interested in across the top you can

actually view the state of the model and

you can view the state of the data

that's flowing through the model so

actual versus predictive how are we

doing are we getting better we're

getting worse

if you apply this to simulation you

could have a button here that you could

click and it can actually show you the

progression of a simulation as it's

running through the uh the model itself

these recommendations here

you'll see above that there's a thing

called copilot copilot you can actually

bring into the application and use it in

here so if I was to ask it a question

let me just grab my prompt

and paste that in there

I can engage and talk with it and ask it

anything around this particular asset

that I'm interested in

this is using currently chat GPT so the

the data that I'm looking for here is

not sensitive in that regard however we

do have some OEM

Partners who have gone and taken as an

example Azure open Ai and they are using

that on their own data their documents

their manuals and they've deployed that

internally as well

this is just easier to to demonstrate

and show the concept of how you can plug

this in and where we are busy plugin the

different bits and pieces in so even

though this is using a chapter GPT API

here you could switch this out and put

azure's open AI in here as well a lot of

problem to do that

you'll see the the recommendations

coming down

you can go and expand that further and

actually pass these recommendations into

the assets themselves so here you can

see a discharge exception and I can

actually see that in this particular

Unity view as well I've got more space

for my co-pilot

um but I can still see the relevant

information that is applicable for me

if I drill into these recommendations

and I'll drill into this one as an

example and then I'll open a few others

as well

this is your quick start for

recommendations that you've configured

what I mean by quick start

so let me go all the way back here and

open up a different example for you

so when I say quick start you have

certain capability that is available out

the box you get it when you install and

you can just use it there's some other

capability that you can actually

configure within the platform as well so

we have a lot of different widgets we

have a lot of different applications

that you can just import we have a lot

of different templates

one of those templates is around

recommendations so you'll see at the top

I've actually got two sets of

recommendations on this particular page

for the Top If I go into my one example

this is the recommendations that most

people are familiar with XM Pro would

actually be looking at

this is the the Quick Start

you can't really change anything here

from an end user's experience or even

from someone who's configuring it you do

have some some control over the form and

maybe the triage instructions here but

that's about it you can't change any of

the layout you can't add anything to

this particular form maybe you want to

enhance and bring some other data in

some other capability in here as well

so how do you actually do that

if we go down the bottom

you can actually take all of that data

and make it available in different views

that your end users are interested in

consuming

same data presented a bit differently

but what this allows us to do is we can

now bring in let me hit my other prompt

there we can now bring in the copilot

into here as well and this is around dry

gas seals I can see my event data for

the event that has happened I can see

analytics so how often is this actually

happening is there something that

happens at certain times is it happening

when other events are happening as well

so we're dealing with a pressure seal

that is low we may have some high

temperatures maybe all of this is

related and there is a correlation

between these as well

however if we go a bit further down you

can bring the copilot in here as well

so now you've got a co-pilot which you

can deploy and use on an actual

application itself at an asset level or

maybe all the way up at a landing page

for your different views or you can have

a view where you can have it all the way

down with your recommendation data as

well

so now as an end user I can decide and I

can work through and work out based on

what I'm looking at based on what I've

asked and the responses I am getting do

I need to create a work request can I

capture any notes what do I actually

need to do with this recommendation that

I'm looking at here

and again this recommendation was

triggered from within the data streams

you'll see there is a run recommendation

if I go into the other example you'll

see there is a run recommendation as

well so we apply the same patterns in

our data streams irrespective or if if

you're using a model that is coming from

a repository

in this case this one is coming from a

repository or if you're using some of

the standard inbuilt

algorithms are already there or if you

just want to go and run your own model

and actually use that in here as well

they all follow the same pattern the

output of that you can pass to

recommendations and Trigger

recommendations as well because that's a

key thing for us is making sure that we

can close the loop on any of these

events that we find it's one thing to

just have a model it's how do you

operationalize the model and make it

useful

with the outputs that are coming

this view here

you can then look at the data you can

view any of the model information and

now you have a lot of different options

and how you want to react to that

if I close that

and we come back to this particular view

here

so to go through the the items that

we've just gone through

we talk around Innovation AI

embedded AI as well as augmented AI

embedded AI you can do right now

we have the libraries we have the agents

if you need specific agents for specific

algorithms they're pretty quick and easy

to create they need to talk to a certain

repository you don't want to use the one

that I've just shown here maybe you've

already got your own

those agents can be created very quickly

and deployed and used

on the augmented AI site

you can right now bring in

if I open that up again you can bring in

things like co-pilot into your

applications right now there's nothing

stopping you there's there's no

capability that you're missing to do

that the only thing that I would suggest

is make sure that whatever it is that

you want to use here

um you understand the privacy concerns

with the data again we are using chat

GPT here we are busy I can't show you

the the things on the Azure open AI side

because that's typically trained and

running on corporate data or customer

specific data for their customer

so this you would just swap out same

capability exactly the same mechanism

it's just what's sitting behind that'll

actually change for you as well you can

do that right now

The Innovation piece here this is where

you need access to the excellent Pro

notebook here

to be able to run and configure what

you're looking at we do provide if I go

back into the router we do provide a

quick start as well

the quick start for if you're not

familiar with all the different

capabilities the markup that you need to

use and how you can configure this a

quick start will actually walk you

through as well it's available as soon

as you have access to the AI designer

you'll find it in the list here and it

has a index and it'll just run you

through all the bits and pieces you need

if you're interested in some of the

other examples that we've got you by all

means reach out and happy to happy to

discuss how we can share and learn from

this as well

okay let's see if we've got any of the

the questions we do have a few questions

that came in there so first one does XM

Pro have models

um great question we get that quite a

lot when people see all the different

pieces and capabilities we don't have

specific models that we make available

we're not a data science scientist

company

however we do have certain algorithms

that we do make available so for

instance anomaly detection regression

um

classifications Etc what we do do is

give you the vehicles and the tools to

operationalize your own models whether

those are coming out of a repository as

we did with this piece here or whether

those are coming out of a data stream

and you go and configure everything

whether it's in python or even if you're

more comfortable in our script and you

want to use that you can do that as well

so we're more vehicle that allows you to

operationalize versus do we have a model

that does X on this asset

second question

um I did touch on it a few times but

just to to go through it is I have my

own models and repository do you I need

to choose yours being XM Pro

uh or can that you can keep your own you

do not have to replace what you

currently have you do not have to swap

that out and use ours you can just

integrate from ours into yours that'll

mostly get done inside the data stream

from the agent's perspective over here

again if there isn't an agent that will

connect to your repository of choice

it's pretty quick and easy to actually

create these types of Agents we can

create them on your behalf quite a few

of our partners do that as well or we

can even show you how to create these

yourself as well

the last thing I will leave you with

is just before we wrap up again thank

you for your time

um to today and we do have a webinar

coming out next month as well where

we're going to be talking about the 4.3

release

um the QR code here will take you

directly to the registration page if

you're more comfortable you can type the

link in and go from there if you have

any questions

um you can email me directly or just

sales at actionpro.com and again thank

you for the uh the time today and have a

great rest of the day

foreign
</details>


---


# monthly-webinar---accelerate-your-digital-twin-use-cases---xmpro-blueprints,-accelerators-&-patterns
{% embed url="https://www.youtube.com/watch?v=mRFfYiRelg8" %}



Description:

Welcome to XMPro's insightful monthly webinar series. In this edition, spearheaded by our expert, Gavin Green, we delve deep into the transformative world of digital twins, emphasizin...
<details>
<summary>Transcript</summary>Description:

Welcome to XMPro's insightful monthly webinar series. In this edition, spearheaded by our expert, Gavin Green, we delve deep into the transformative world of digital twins, emphasizin...
hello everybody and welcome to today's

uh webinar my name is Gavin Green I look

after strategic solutions for for exm I

want to thank you all for attending

today uh if you have any questions uh

put them into the uh the chat uh I think

there's question section as well I'll

try and get to them at the end as we go

through it so in today's webinar what

we're going to go through is how to

accelerate your digital twin use cases

using our blueprints accelerators and

pattern as

well before we start though uh we just

need to make sure that we're aligned on

some of the terminology um make sure

that when we're talking um an

accelerator or pattern everyone's on the

same page um on the topic so to do that

U it's easier if I just open it up and

we just go through this so starting from

the bottom um each of these tends to

build on each other so patterns um on

the far right here we see these as

preconfigured data streams we also see

widgets and I'll explain what the

difference is when I go into that uh

form part of the patterns um on on the

right

here the

accelerators um that is typically a

Jupiter notebook from our AI or our

notebook section um it could also be one

or two pages um it could also be a set

of recommendation s with the data Stream

So it builds on the patterns just a

little bit more and then blueprints

blueprints you could see those as

pre-built Solutions so they're typically

around a specific use case um and they

will contain data streams

recommendations um some app

visualizations templates

Etc what are some of the benefits by by

using templates um why are we having

this discussion around blue accelerators

and patterns and what does it mean for

for me and and my organization uh for

for those watching

today so some of the key benefits uh for

this is lower cost of deployment you can

integrate your Silo data um using best

practices you're going to shorten your

time to Value um and that plays into the

next one as well which is improving your

internal personal productivity you don't

have to spend a lot of time working all

the intricate details and and bits some

pieces up you can use this as your

starting platform um and then just adapt

it and change it to your own

requirements as

well you can increase your return on

your value proposition again these all

tie into the shorten time to Value piece

of the top which is really U the key

thing here around all three of them it

doesn't matter if it's a pattern an

accelerator or a blueprint it really is

how do we do things a lot quicker um and

get to our end result a lot faster the

the last one is an

interesting you can get the domain

Knowledge from our partners as well as

ourselves around certain use cases again

you can import these adapt them change

them to your own requirements um but

just some of the benefits of using the

uh the templates

themselves when it comes to our suite of

um products which pieces do these touch

it's going to touch all four them it's

going to touch the data streams the AI

the app designer and also the

recommendation manager as well so it

touches all four of them as you see them

here coming back to my um Iceberg

analogy slide patterns you'll find right

down the bottom here the the patterns

are touching the uh the data stream side

so the DS data wrangling analytics

integration orchestration when we start

talking around the accelerators

accelerators will be touching the AI

piece they could be touching the

recommendation manager piece as well as

the data stream and then you have your

Blueprints and blueprints will go from

the top all the way down whether it's

the app designer recommendations AI or

data streams the notice down the bottom

there the subscription manager we don't

actually touch anything in the

subscription manager for all three of

them so pattern accelerators or or

blueprints the subscription manager is

just where you control your access to

the different pieces so remember when

you're importing and creating your your

different uh blueprints uh or even your

accelerators make sure you set up the

correct access for your team uh if you

want to share them either read access or

write access to them as well if you

don't do that no one else will be able

to use those different components as

well so let's dive into what is it that

we're actually looking at here and and

how do I get a hold of them

if I go into our documentation website

um on the far left you will see there is

a link which says blueprints

accelerators and patents what that will

do is that'll take you to a website this

website is hosted in GitHub itself and

you can see blueprints accelerators and

pattern if we start at the bottom and

work our way all the way to the Top If

we go to patterns it will list all the

different patterns that we have

published now publish these if you wish

to contribute I will have a link right

at the end which will walk us through

how to contribute um and make your own

patterns accelerators or blueprints

available here and you can merge them in

as well pattern is broken up into two

main sections um that I have available

here the AI these will be data streams

and then widgets which will be used in

the app

designer this is a constantly evolving

site as we have new um items added in

either of the three sections they will

be added to these Pages um and you'll be

able to access them as well if you click

the view details on any of them it'll

take you down into the actual component

itself so this is the asset monitoring

using binary classification across the

top you have your visuals so if you

click into those you can actually see

what they look like from the visual

perspective just clicking out of that

will'll close them on the left you will

see all the pages will have a set of

common items the one is going to be the

import password whenever you try and

import anything it doesn't matter if it

is a widget it doesn't matter if it's a

data stream recommendation or an app you

need an import password we use the same

password for all of these items just to

make it easier for people to integrate

um and and use these all you can do is

just double click and copy this

particular password Here

and then you can use it when you're

importing if you're looking for

instructions and how to import you can

click this particular link here it will

take you to our documentation site which

will list out the import export um and

all the different components from our

documentation S as well does not matter

if it's a data stream uh recommendation

Etc it's all on this particular site

here on how to import it'll walk you

through the different details um for

that as well and then lastly there'll be

a file section which will contain the

various components that you are going to

need this particular example has two

there's a SQL script and there's a data

stream if you go and open the script

you'll notice that it'll actually take

you to the uh repository at the back

which has the components that you need

to actually run it so in this example

this would be the SQL script so you can

just copy the actual text here run this

against your SQL environment go back and

now you can and open up the data stream

and again you can just download the

actual data stream to import it as

well it does not matter if this is a

full blueprint and I'll show you a few

examples on that as well it follows the

same principle here with regards to the

section on the left components in the

middle you'll see a table of contents

will allow you to jump around different

items that we're looking at the data

stream will just highlight what are some

of the items that are used used in the

data Stream So if you want to learn a

little bit more you want to get a bit

more comfortable with the particular

pattern in this example which of the

agents are we using and again each of

these will take you and allow you to

drill down into that

particular um documentation and you can

find out more information as as you want

to or or need to right at the bottom are

the typical steps to follow to import it

does not matter if this is again a

package an accelerator or a blueprint

you're going to follow the very similar

steps to import the key thing at the top

there though is making sure that you

have a set of variables defined these

variables are typically create created

when you're installing a site but again

it's just good to make sure that you

have them when you are importing so what

do I mean by by these variables you need

to have specific access and you'll

notice here on the left there is

variables I'm in the app designer right

now I just click the uh hamburger and I

click variables it'll open up the

variables for

me what we're looking for is to make

sure you have the app designer URL and

the app designer integration key you

will notice that there is an app

designer URL inside the app designer and

if we go into the data streams you will

find one in there as well just a

reminder variables are shared so if you

define it in the app designer it'll be

available in the data stream and vice

versa however you do need to apply your

variables in both systems the reason for

that is each of them is using a

different encryption key um specifically

when you are encrypting the values in

here so just keep that in mind when you

are actually creating or confirming the

variables that you set them in both

environments you'll see here in the app

designer I can go down and I can see my

integration key if I go into the data

stream you can see I've set them as well

if you have not set them how do you know

you can see all the items here which

have the Chevron next to them have not

been set in the app designer whereas in

the data stream designer they have been

set so that's how you can very quickly

tell have they' been configured or not

do you need to configure them in both

environments it depends on your use case

and how you're going to use these

particular

variables inside the app designer I'm

not going to be using the actual too or

the ml flow capabilities but inside my

data stream I am that's why they are

configured for me in

here so important across the top make

sure that you have these defined to be

able to use this um data stream in this

example you'll notice that we're talking

around SQL username password down here

the reason we are is a lot of the

accelerators and pattern um are set to

specific data sources that we have

defined now when you are actually

loading in these accelerators by just

open up this particular one that we are

looking at

here you will see in this data stream we

have two items one which is going to be

where's my data coming from but two

where is my context coming from if you

want to change your context you can U

just make sure that over here you

obviously creating the variables to

whatever system you are changing it to

when you load it in so step one is

really just confirming your variables

where are you going to be getting your

data from um to to be able to do

anything the app designer these two here

is required when you are trying to run a

recommendation using a recommendation

manager or you are looking to pass data

to our visuals that is why you've

defined the two of those if you do not

have that def you will not be able to

use these two agents on this particular

data stream

itself second run the SQL script so here

you will see the smart meter again if I

open that up in another window you will

see what it is you actually creating and

configuring again do you have to use

this um in your own environment no by

all means you can swap that piece out

and drag on another context Provider

from the library as you need to or want

to bring it

in second importing the data

stream so first thing that you would

need to do is make sure that you

download the data stream uh from this

particular environment here so you can

see here is the data stream um itself

the extension U uh Fu so here I can just

click the download and it'll download

the actual carile for me to be able to

use

all

next thing we want to import that

particular data string it follows the

same process um if you go into the data

streams you will see there is an import

option if you click that it's going to

ask you for a file key this file key is

this key that we've copied across the

top here which is the input password

again we use the same password for all

three sections just to make it a lot

easier for folks to to use so you just

put the key in there and now you can

actually please select the file to to uh

to

upload and now we can say upload what

this will do is it will check your site

as well and it'll do the same for

recommendations it'll do the same for

for apps um if it picks up that there is

already a version of that it's going to

ask you a question you want to import it

as a new version what you want to import

it is a completely new entity of that

then this one is a data stream so I'm

going to get the option there it'll do

the same for a recommendation it'll do

the same for an app as well if you want

to just say a new version uh it'll just

increment the version and create this

system new version even if that app

recommendation or data stream is

published it'll create a new version but

it's not going to take that version live

you still need to go in and edit it and

change it because this is a data stream

it's going to ask me where do I actually

want to uh run it and I can put it into

the correct collection make sure that

you are following the um the actual

blade itself it's going to ask you

different question depending on what it

is that you want to import for the

different areas if I go into my new data

stream I can give it a name put it in a

category but again I slap my collection

designation um as

well once we've imported that then it is

available for for our use and as I go

into this particular

example

you can now change and configure it so

next step once we've imported it assign

access to others as required again

applies to all the different areas um as

well you need to decide who else is

going to be using this uh with you

because this is the data stream we can

go into the manage access and make sure

you're giving access to the correct

people also Define what type of access

you want to give them you want to give

them read access write access or coowner

access uh to it as well read access will

just allow you to view the co components

and content right will allow you to edit

and co-owner access will typically allow

you to change other people's access

rights to it as well if you have read

access to items you cannot publish or

unpublish uh that component whether it

is a data stream whether it's a

recommendation or whether it's an actual

app itself all you can do is edit and by

edit I mean you can go in and configure

and see what the items are you can make

changes to it it'll give you the little

ascts that will ask you to say but as

soon as you try and save it'll tell you

you do not have access to that and you

will not be able to save it um as

well

important have a look at the different

components that you and this is

specifically important with regards to

the the data streams themselves when

you're importing them you need to make

sure that you double click anything that

that is a exm Pro app and it's correctly

configured to use the URL and the key

the same for the recommendation make

sure that it is correctly set up to use

the uh the key and the uh the URL as

well what you also need to do is make

sure that your context provider is

pointing to whatever data source it is

that you've defined this one is pointing

to the SQL um because we've loaded the

SQL um across the top into there as well

so you need to make sure that that's

been defined as well the recommendation

make sure it's pointing to the correct

URL key just click apply save um and

that should be all you need to do the

entity items um the different components

down here you don't need to remap those

or reset those all you really need to do

is just make sure that your connection

properties are set typically your URL in

your key if I come into the SQL again

make sure that it's pointing to the

correct instances here making sure it's

your correct database your correct and

it'll automatically start filling in the

rest of the items for you as

well and then right at the bottom just

clicking apply publish and ensure that

you are getting data coming through for

for all of these but once you've

configured everything and it is ready to

go make sure you hit publish go to the

live view um and

typically pick the uh the item before

the Run recommendation as well as the

the app so here you'll see predict is

the the item coming out the AI post

elemetry is coming out of the action

agent depending on the data stream that

you've configured it'll take a bit um

just to run this one's running a

predictive model loading a lot of data

and contextual data so it'll take a

little bit of time to come through make

sure you've got the data flowing through

this particular section here before you

continue onwards I.E going in loading an

app loading a recommendation

Etc you can see the data is coming

through now across the top which means

we've configured this correctly and we

can either leave it running um and

continue on to the next step or we can

unpublish it depending on what the use

case for this item

is

accelerators if I go into into the top

we'll tend to build on patterns but

before we go into accelerators there's

this another area on P which is around

widgets now what a widget is is it is

into the realm of the app designer and

it really is how do I create individual

components that I don't have to spend a

lot of time trying to move everything

Pixel Perfect uh for it so what we've

done here is we've curated a list of a

lot of different widgets that we tend to

reuse over and over again just to make

it quicker and easier for folks to

actually use inside the app designer

again it's going to follow the same

principle across the top you will have

your um visuals these visuals here you

will see uh this is what the actual run

space will look like there is the

configure space um as well because this

is inside the app designer there's two

themes there's a light theme and a dark

theme on the left you have your same

thing which is importing the password as

well as a file as well as a widget so if

I open up that particular widget you'll

see it will take me again back into the

uh GitHub repo and it'll allow me to

download those particular um files

themselves so where are these uh widgets

and and how do I use them inside the app

designer if I go into a particular

application so I'm going to go into my

one example here if you go into the edit

mode as if you were configuring a

particular app

itself on this particular area here here

you'll see under blocks on the left

there's a widget section you have two

icons here which will allow you to

export a widget or import a widget if

you tell it you want to

import it's going to ask you for a key

this is the same key that we've got

across the top that is what we're

interested in so you paste the key there

and then you upload the actual widget

file itself that you are interested in

all of the widgets have a file that will

allow you to import that particular

widget so the depending on what it is

that you are looking to actually use and

reuse in your applications you just load

the appropriate widget for that where

the widgets actually appear is if you

expand

the the accordion you'll see all your

widgets will appear here as

well if I drag one on you will notice

that it will drag the item in for me as

well most of the widgets that we

configure will be from a Content card

perspective so you'll see here we have

card and here is a Content card that

will actually drag it in if I drag in

the other one you'll see this one is

dynamic and this one is

static why do we have two of these items

depending on your use case the one on

the right here means I have a static

view it's not going to change um I'm

only going to have so many columns you

can now come in and change as you want

to or need to so if you are not

interested in having all the columns you

can come in and actually remove a column

now I've only got three

columns each of these if you click on an

item and go to page layers you will

notice that there is typically a data

source that's been defined in the page

layer themselves so if I click the data

source it will allow me to bind this to

a particular data source itself so here

I can go into the page data create

myself a u data source typically

pointing to a data stream and if I go to

the block properties I can actually bind

this this particular data source um to

it and now I can come in and start

binding as I would normally the actual

text to any of the properties coming in

from that particular data source

itself all the widgets function in a

very similar faction where anything that

has data sources will allow you to map

them and move them as well again this is

a static this one's a little bit more

Dynamic what that means is you'll notice

this section here we've only to find one

the data source is going to dictate how

many columns it's actually going to be

creating for me and you'll find this

pattern follows through in a lot of the

actual widgets themselves there will

typically be a static one but there will

also be a dynamic one whether it's

columns or rows which will allow you to

grow um the actual um app pieces itself

if I click in here and go to the page

layers you'll see there is the total

data source and there is the child data

source so this is typically where you

would put the data source um itself and

then you just map the items and then

it'll configure everything for you I

mentioned two themes the widgets unless

otherwise specified will function in

both themes themselves so if I go into

the dark theme and I drag these two

widgets in as well you will notice that

they will be colored appropriately um

and they will match that particular

theme itself so if I go and actually

launch this you can see there are my um

items if I go to my live theme there are

my items as well because I bound this

one to the data source you will notice

that it's actually going to duplicate

the items so let's go in there let's

remove the data source for the uh the

moment and we can then have a look

at how this is actually rendering so

this is what it would look like in the

live theme this is what it would look

like in the dark

I didn't have to change anything um I

didn't have to edit anything I can just

drag them on use them and configure them

as I need to and that follows the same

for pretty much all the widgets um in

here and there's a lot of different

widgets um in here um this list is

constantly being added to we're

constantly growing it um if you have

something that you feel You' like to put

in here by all means send it to send it

in or contribute it um as well um to

this particular list the last it I'll

touch on is blueprints so inside

blueprints we're building on the other

two um items themselves so pattern

typically you have your um data streams

and widgets inside accelerators you will

see here these are typically onepage

apps so this one here would be um I've

just got a visual which is just showing

me 3D items and how do I bind them to a

Unity view so there is an app over here

and there is a data stream again it'll

walk you through what are some of the

key pieces in it but the steps you'll

notice is very similar to what we've uh

just gone through with the the patent

confirming your variables importing what

you need to do importing the application

um and then just running it from from

there inside the accelerators there is

an AI section as well so here if I open

this up we'll load the um quick start

guide or um our Jupiter notebooks or our

notebooks ourselves any of the other U

notebooks that we make available will

appear in here as well and we'll

function under the

accelerator coming into blueprints

you'll notice they just keep building on

each other here so the blueprints

themselves if I go into a particular

example in here across the top you have

your visuals again you can click through

that and see what all the different

components are in that um blueprint

itself on the left you just just have a

lot more items to

import you still got the same

instruction you still have the same

password here you have your application

and template there are the

recommendations data stream and any um

data scripts that are needed same

principle applies here when you are

importing your data streams you can

adjust and change where your data is

coming from you can also adjust and

change your recommendations so if the

thresholds are not to your liking change

and adjust them as well you'll see same

pattern make sure your variables are

defined running any of your scripts U

that need to be run there is a sequence

to importing a

blueprint um typically you will import

your data streams then you'll import

your

recommendations uh there are times when

you may be importing a second data

stream in between the two especially if

it's working on a recommendation that

will be called out in the actual steps

themselves and then last you'll import

your application for it when you're

importing your application you'll notice

down here it'll call out specific steps

that you need to do this is when you're

linking to

recommendations um and where you need to

do that the reason for doing application

last is if you were to do application

first one of the options on an import is

going to ask you to bind it to the

different data streams if you've not

imported those data streams left you can

leave it blank but you're going to have

to go and manually set that up

afterwards that's why the application is

typically lost because you already

imported your data streams you've

imported your recommendations and you

should just be able to match everything

when you import it it makes the

experience a lot quicker and a lot more

pleasant when you are loading those

in if we come back to to the items um

that we've got here again there's three

areas that typically build on top of

each other patents accelerators and and

blueprints so how do I contribute and

where do I get access uh to these so for

contributions um the link across the top

that QR code will take you straight to

that particular link itself or for

direct access you can click that link at

the bottom as well um if you don't want

to remember those particular links what

you can do is just go to our

documentation website documentation.

xo.com click the uh the link on the left

and it'll take you to that website as

well perfect um while I keep this up

here let's see if we've got any

questions from from anyone on the

audience we do okay so the one question

here is is around contrib okay so if you

want to contribute there's two ways you

can contribute um to it uh if you're not

comfortable loading them into the

repository or where to put it or how to

style it by all means you can send it to

us whether it's a pattern an accelerator

or blueprint what we'll do is um load it

ourselves and give you the um correct

attributes as to where it came from to

to load it in there if you are more

comfortable uh what you can do is you

can Fork the repository uh check it in

and then we can actually merge that in

uh once it's been rated and checked and

then it'll be available for everyone

else to to load in as

well next steps uh just before we wrap

up here um to remember to to register

for next month's webinar again there's

two options for it um here we'll be

hosting a a hoty Q&A session around

predictive maintenance and continue uh

condition monitoring as well any

questions you can reach out to our um or

our team for more information and again

thank you all for attending today have a

great rest of uh rest of your day
</details>