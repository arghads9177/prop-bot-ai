# testing/test_company_profile_checker.py
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agents.company_profile_checker import company_profile_checker_agent
from agents.state import AppState

valid_input = {
    "company_profile": """
    About the Softmeets
When someone asks what we do softmeets Info Solutions, it’s tempting to point out our four-decade track record for helping to transform the world’s great companies into sharper, smarter, better versions of themselves. It’s true, our mission is to help management teams create such high levels of economic value that together we redefine our respective industries.

We work with top executives to help them make better decisions, convert those decisions to actions, and deliver the sustainable success they desire. For forty years, we’ve been passionate about achieving better results for our clients-results that go beyond financial and are uniquely tailored, pragmatic, holistic, and enduring.

We advise global leaders on their most critical issues and opportunities: strategy, marketing, organization, operations, technology, transformations and mergers & acquisitions, across all industries and geographies.

Our unique approach to traditional change management, called Results Delivery, helps clients measure and manage risk and overcome the odds to realize results.

Providing digital transformation, SaaS, Automation, Internet of Things, Artificial intelligence & Analytics technologies.
Webel IT Park (3rd Floor), Kalyanpur Satellite Township, Asansol – 713302, Dist – Paschim Bardhaman (W.B). India
+ (91) 9434 811 929, 0341-3500346
INFO@SOFTMEETS.COM

Trusted by our Government of India customers.
Trusted by our esteemed Government of India customers, we deliver reliable, innovative solutions tailored to meet critical
operational and strategic needs. Our commitment to excellence ensures robust performance, security, and compliance,
fostering enduring partnerships built on trust and proven success.
Our customers are Indian Railways, Indian Army, SAIL, Ministry of Communication, ICMR, West Bengal Housing Board, Chittaranjan Locomotive Works, and many more.

Our Partners are Microsoft, HP, Elnova
We are CMMI Level 5 certified and ISO 27001:2013, ISO 20000-1:2018, ISO 9001:2015 certified.

Our Mission is to Transform your entire business to innovative digital business process
Embrace cutting-edge automation, advanced analytics, and seamless integrations to optimize operations, improve decision-making, and deliver exceptional customer experiences.
Visit us at https://softmeets.com/
    """
}

invalid_input = {
    "company_profile": "Looking for an AI company to collaborate with in building chatbots."
}

empty_input = {"company_profile": ""}

print("✅ Valid Company Profile Test:")
print(company_profile_checker_agent.invoke({"state": AppState(**valid_input)}))

print("\n❌ Invalid Company Profile Test:")
print(company_profile_checker_agent.invoke({"state": AppState(**invalid_input)}))

print("\n❌ Empty Company Profile Test:")
print(company_profile_checker_agent.invoke({"state": AppState(**empty_input)}))
