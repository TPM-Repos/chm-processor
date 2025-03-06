![](images/collapse.gif) ![](images/expand.gif) ![](images/copycode.gif) ![](images/copycodeHighlight.gif) ![](images/drpdown.gif) ![](images/drpdown_orange.gif)  
  
---  
DriveWorks SDK Documentation  |   
---|---  
Introduction   
[Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic4.md)  
  
Glossary Item Box

# Introduction

DriveWorks has a rich extensibility model enabling extension writers to extend DriveWorks in many ways.

## Getting Started

Before getting started, there are some terms you should know:

Term |  Meaning  
---|---  
Extension Library |  A .NET class library which contains one or more extensions.  
Extension |  An extension such as a Connector or a Plugin, usually implemented as a single .NET class.  
Plugin |  A specific type of extension which can customize the behavior of a DriveWorks Application.  
Service |  A capability or group of related capabilities provided by one or more DriveWorks Applications.  
  
## Types of Extension Library

The main types of extensions that can be created in a DriveWorks Extension Library are:

Extension Type |  Applies To |  Description  
---|---|---  
[Document](topic4356.md) |  All |  Allows for new document types to be added to projects.  
[Table](topic4282.md) |  All |  Allows for new table types to be added to projects.  
[Task](topic11629.md) |  All |  Allows for new specification flow task types to be added to projects.  
[Condition](topic10804.md) |  All |  Allows for new specification flow condition types to be added to projects.  
[Translator](DriveWorks.Applications.Autopilot.Extensibility~DriveWorks.Applications.Autopilot.Extensibility.ITranslator.md) |  DriveWorks Autopilot |  Supports the DriveWorks Autopilot translation mechanism for understanding specifications stored in files. This type of extension is useful when dealing with a file format DriveWorks doesn’t natively understand, e.g. specification data in an XML file formatted to a 3rd party schema.  
[Connector](DriveWorks.Applications.Autopilot.Extensibility~DriveWorks.Applications.Autopilot.Extensibility.IConnector.md) |  DriveWorks Autopilot |  Retrieves specification information from a 3rd party system and creates specifications in DriveWorks.  
[Plugin](topic2004.md) |  All |  Integrates with a DriveWorks application and has the ability to add command buttons and listen to DriveWorks events to customize DriveWorks’ behavior. This type of extension is useful when integrating DriveWorks into 3rd party systems such as PDM and ERP.  
  

