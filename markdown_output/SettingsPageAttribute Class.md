       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SettingsPageAttribute Class   
[Members](topic960.md) See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic959.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) : SettingsPageAttribute Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Exports a settings page from a library so that it can be shown in the settings window. 

# Object Model

![](dotnetdiagramimages/image31.png)

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <AttributeUsageAttribute(ValidOn=AttributeTargets.Assembly, 
       AllowMultiple=True, 
       Inherited=True)>
    Public Class SettingsPageAttribute 
       Inherits [DriveWorks.Extensibility.ExtensibilityAttribute](topic7177.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SettingsPageAttribute](topic959.md)  
  
C#|   
---|---  
      
    
    [AttributeUsageAttribute(ValidOn=AttributeTargets.Assembly, 
       AllowMultiple=true, 
       Inherited=true)]
    public class SettingsPageAttribute : [DriveWorks.Extensibility.ExtensibilityAttribute](topic7177.md)   
  
# Inheritance Hierarchy

System.Object  
System.Attribute  
[DriveWorks.Extensibility.ExtensibilityAttribute](topic7177.md)  
**DriveWorks.Applications.SettingsPageAttribute**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SettingsPageAttribute Members](topic960.md)   
[DriveWorks.Applications Namespace](topic16.md)

©2024 DriveWorks Ltd. All Rights Reserved.
