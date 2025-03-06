![](images/collapse.gif) ![](images/expand.gif) ![](images/copycode.gif) ![](images/copycodeHighlight.gif) ![](images/drpdown.gif) ![](images/drpdown_orange.gif)  
  
---  
DriveWorks SDK Documentation  |   
---|---  
Installation/Registration   
[Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic6.md)  
  
Glossary Item Box

# Introduction

Unlike project extenders which are discovered by DriveWorks automatically, Extension Libraries need to be registered for DriveWorks to load them.

The easiest way to register an Extension Library is using the [Install Button on the Plugin Settings screen](http://docs.driveworkspro.com/PluginSettings.md) in DriveWorks.

# Installation

Another way to register a project extender is by editing the registry directly, or creating an installer.

Extension libraries are registered in the Windows Registry in:

> HKEY_LOCAL_MACHINE\Software\DriveWorks\<Version>\Common\Libraries

To register a library, create a subkey with the same name as your .NET class library’s assembly name (e.g. MyExtensions) and then create the following values:

Name |  Type |  Required? |  Value  
---|---|---|---  
Path |  String (REG_SZ) |  Yes |  The full path to your extension library, e.g.: C:\Code\ MyExtensions\bin\debug\MyExtensions.dll  
IsCompat64 |  DWORD (REG_DWORD) |  No |  1 (the default) if the extension is architecture agnostic and works on both 32-bit and 64-bit systems. 0 if the extension entry is in the 32-bit part of the Windows Registry and the extension shouldn’t be loaded into a 64-bit process.  
  
©2024 DriveWorks Ltd. All Rights Reserved.
